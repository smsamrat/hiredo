from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from profile_settings.models import Profile


User = get_user_model()
# Create your models here.

class Category(models.Model):
    name= models.CharField(max_length=100)
    parent = models.ForeignKey('self',blank=True, on_delete=models.SET_NULL, null=True ,related_name='children')
    image = models.ImageField(upload_to='category_images/', null=True)
    created=models.DateTimeField(auto_now_add=True,null=True)
    popularity = models.IntegerField(default=0)


    class Meta:
        ordering = ['-id']
        verbose_name_plural = "Categories"


    def get_categories(self):
        if self.parent is None:
            return self.name
        else:
            return self.parent.get_categories() + ' -> ' + self.name

    def __str__(self):
            return self.get_categories()

class Location(models.Model):
    name= models.CharField(max_length=100)

    class Meta:
        ordering = ['-id']
        verbose_name_plural = "Locations"


    def __str__(self):
        return self.name




class Questions(models.Model):
    cat = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='cat_name')
    qs= models.CharField(max_length=100)


    class Meta:
        ordering = ['-id']
        verbose_name_plural = "Questions"


    def __str__(self):
        return self.qs


class Answer(models.Model):
    question = models.ForeignKey(Questions,on_delete=models.CASCADE,related_name='answers',null=True)
    options= models.CharField(max_length=100)
    credit= models.IntegerField(default=0,null=True)
    created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return f"{self.options}_x_{self.credit}"

    class Meta:
        ordering = ['-id']
        verbose_name_plural = "Answers"

class Post(models.Model):
    post_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='post_user',blank=True,null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='post_category',blank=True,null=True)
    location = models.CharField(max_length=200,blank=True,null=True)
    question = models.ForeignKey(Questions,on_delete=models.CASCADE,related_name='post_qs',blank=True,null=True)
    p_answer= models.ForeignKey(Answer,on_delete=models.CASCADE,related_name='post_ans',blank=True,null=True)
    created = models.DateTimeField(default=timezone.now())


    class Meta:
        ordering = ['-id']
        verbose_name_plural = "Posts"


    def __str__(self):
        return self.post_user.email


class PostList(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='many_post_user',blank=True,null=True)
    location = models.CharField(max_length=500,blank=True,null=True)
    latitude = models.CharField(max_length=500,blank=True,null=True)
    longitude = models.CharField(max_length=500,blank=True,null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='postlist_category',blank=True,null=True)
    post_object = models.ManyToManyField(Post,related_name='post',blank=True)
    post_credit =  models.IntegerField(null=True)
    created = models.DateTimeField(default=timezone.now())
    post_type = models.BooleanField(default=False)
    response_count = models.IntegerField(default=0)
    is_response = models.BooleanField(default=False)
    not_interested_users = models.ManyToManyField(User, related_name='not_interested_posts', blank=True)


    class Meta:
        ordering = ['-id']
        verbose_name_plural = "Post Lists"

    def __str__(self):
        return self.category.name


class RecieverEmailTemplate(models.Model):
    to_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='reciever_user',blank=True,null=True)
    from_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='sender_user',blank=True,null=True)
    post_list = models.ForeignKey(PostList,on_delete=models.CASCADE,related_name='post_lists',blank=True,null=True)
    template_name = models.CharField(max_length=500)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True,null=True)


    class Meta:
        ordering = ['-id']
        verbose_name_plural = "Reciever Email Templates"

    # def __str__(self):
    #     return self.user.to_user +

class WishlistProfileService(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='wishlist_user',blank=True,null=True)
    wished_user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='item_user',blank=True,null=True)


    class Meta:
        ordering = ['-id']
        verbose_name_plural = "Wishlist Profile Services"


    # def __str__(self):
    #     return self.user.email


class WishlistFeatureService(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='wishlist_user_cat',blank=True,null=True)
    category_service = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='category_services',blank=True,null=True)
    # def __str__(self):
    #     return self.category_service.name


    class Meta:
        ordering = ['-id']
        verbose_name_plural = "Wishlist Feature Services"




#added by swesadiqul
class MyResponse(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Hired', 'Hired'),
        ('Archived', 'Archived'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_responses')
    posts = models.ForeignKey(PostList, on_delete=models.CASCADE, related_name='user_posts', null=True)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True, null=True)


    class Meta:
        ordering = ['-id']
        verbose_name_plural = "My Responses"


class PostRequestList(models.Model):
    post = models.ForeignKey(PostList, on_delete=models.CASCADE, null=True, related_name='posts')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='request_user')
    rating = models.FloatField(default=0)
    request_accepted = models.BooleanField(default=False)


    class Meta:
        ordering = ['-id']
        verbose_name_plural = "Post Request Lists"

    def __str__(self):
        return self.profile.user.email


class RealTimeBookNowService(models.Model):
    question = models.ForeignKey(Questions,on_delete=models.CASCADE,related_name='real_time_book_qs',blank=True,null=True)
    p_answer= models.ForeignKey(Answer,on_delete=models.CASCADE,related_name='real_time_book_ans',blank=True,null=True)
    created = models.DateTimeField(default=timezone.now())

    # def __str__(self):
    #     return self.post_user.email

    class Meta:
        ordering = ['-id']
        verbose_name_plural = "RealTime Book Now Services"


class RealTimeBookNow(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='book_user',blank=True,null=True)
    booked_in_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='booked_user',blank=True,null=True)
    location = models.CharField(max_length=500,blank=True,null=True)
    latitude = models.CharField(max_length=500,blank=True,null=True)
    longitude = models.CharField(max_length=500,blank=True,null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='RealTime_service_category',blank=True,null=True)
    realtime_post_object = models.ManyToManyField(RealTimeBookNowService,related_name='RealTime_service_obj',blank=True)
    post_credit =  models.IntegerField(blank=True,null=True)
    post_type = models.BooleanField(default=False)
    response_count = models.IntegerField(default=0)
    is_response = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now())


    class Meta:
        ordering = ['-id']
        verbose_name_plural = "RealTime Book Now"



class CreditReduceTransaction(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='credit_user')
    lead_post_id = models.CharField(max_length=30)
    lead_post_credit = models.FloatField()
    date = models.DateTimeField(default=timezone.now())


    class Meta:
        ordering = ['-id']
        verbose_name_plural = "Credit Reduce Transactions"



