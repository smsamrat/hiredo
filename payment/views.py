from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.generics import ListAPIView
from django.db.models import Avg,Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class SetCreditRetrive(ListAPIView):
    queryset = SetCreditPurchased.objects.all()
    serializer_class = SetCreditPurchasedSerializer

class UserCreditAmount(APIView):
    def get(self, request, format=None):
        queryset = CreditPurchasedByUser.objects.filter(user=self.request.user)
        if len(queryset) > 0:
            total_credit = CreditPurchasedByUser.objects.filter(user=self.request.user).aggregate(Sum("credit_amount"))['credit_amount__sum']
            print(total_credit)
            data ={
                'total_credit':total_credit
            }
            return Response(data)
        else:
            serializers = CurrentUserCreditAmountSerializer(queryset,many=True)
            return Response({'total_credit':0})

class UserCreditPurchased(APIView):
    def post(self, request, format=None):
        serializers = CreditPurchasedByUserSerializer(data=request.data)
        request.data['user'] = request.user.id
        if serializers.is_valid():
            credit_amount = serializers.validated_data['credit_amount']
            request.user.user_profile.credit += credit_amount
            request.user.user_profile.save()
            serializers.save()
            return Response({'status':'data save successfully'})
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
