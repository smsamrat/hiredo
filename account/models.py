from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser,PermissionsMixin
from django.utils import timezone
from django.conf import settings
from django.db.models import ForeignKey, Model
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver



#create model
class UserManager(BaseUserManager):
    def create_user(self, email, full_name, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, full_name=full_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_admin', True)
        return self.create_user(email, full_name, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username = None  # Remove the username field
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    date_of_birth = models.DateField()
    corporation_name = models.CharField(max_length=255)
    corporation_number = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    stripe_customerId = models.CharField(max_length=500, blank=True, null=True)
    last_login = models.DateTimeField(auto_now=True)
    join_date  = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)
    is_professional = models.BooleanField(default=False)

    # Define email as the USERNAME_FIELD
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["full_name", "date_of_birth", "corporation_name", "corporation_number", "phone_number"]


    # OTP related fields
    otp_secret = models.CharField(max_length=16, null=True, blank=True)
    otp = models.CharField(max_length=6, null=True, blank=True)
    otp_expire_time = models.DateTimeField(null=True, blank=True)

    objects = UserManager()

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
         # The user is identified by their email address
         return self.email

    def __str__(self):
         return self.email

    @staticmethod
    def has_perm(perm, obj=None):
        return True

    @staticmethod
    def has_module_perms(app_label):
         return True


    def is_otp_valid(self, otp):
        return self.otp == otp and self.otp_expire_time > timezone.now()

    def reset_otp(self):
        self.otp_secret = None
        self.otp = None
        self.otp_expire_time = None
        self.save()



class ServiceLocation(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='locations',
        blank=True,
        null=True,
    )
    city = models.CharField(
        max_length=255,
        db_column='postal_code_or_city',
    )
    distance = models.CharField(
        max_length=255,
        db_column='distance',
    )
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']
        verbose_name_plural = 'Service Locations'
        db_table = 'service_location'


    def __str__(self):
        return f'{self.city}'

class Service(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="services", blank=True, null=True)
    service_name = models.ForeignKey('lead.Category',on_delete=models.CASCADE,max_length=255,null=True, db_column="Service Type")
    service_description = models.TextField(db_column="Service Description")
    service_location = models.ManyToManyField(ServiceLocation)
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Services"
        db_table = "Services"


    def __str__(self):
        return self.service_name.name


class SMSTemplate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    template_name = models.CharField(max_length=100)
    message = models.TextField()
    created = models.DateTimeField(default=timezone.now())
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ["id"]
        verbose_name_plural = "SMS Templates"
        db_table = "SMS Templates"


    def __str__(self):
        return self.template_name

class EmailTemplate(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    template_name = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Email Templates"
        db_table = "Email Templates"


    def __str__(self):
        return self.template_name


class OneClickResponse(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    one_click_response = models.BooleanField(default=False)
    template = models.ForeignKey(EmailTemplate, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"One-Click Response for {self.user.full_name}"


@receiver(post_delete, sender=EmailTemplate)
def update_one_click_response(sender, instance, **kwargs):
    user = instance.user
    remaining_templates = EmailTemplate.objects.filter(user=user).exists()
    if not remaining_templates:
        OneClickResponse.objects.filter(user=user).update(one_click_response=False)


class Slider(models.Model):
    image = models.ImageField(upload_to="media/slider")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Slider'


class ProfilePicture(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name = 'user_profile_pic',blank=True, null=True)
    picture = models.ImageField(upload_to ="profile_pictures/")


    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Profile Pictures"
        db_table = "Profile Pictures"


    def __str__(self):
        return self.user.full_name





