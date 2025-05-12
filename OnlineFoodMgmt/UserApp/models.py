from django.db import models
from AdminApp.models import Food

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=20,primary_key = True)
    password = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=200,blank=True,default="Pune")
    pincode = models.CharField(max_length=10,default=00000)
    phone = models.CharField(max_length=15,default=0000)
    class Meta:
        db_table = "UserInfo"

class MyCart(models.Model):
    user = models.ForeignKey('UserInfo',on_delete = models.CASCADE)
    food  = models.ForeignKey('AdminApp.Food',on_delete = models.CASCADE)
    qty = models.IntegerField()

    class Meta:
        db_table = "MyCart"