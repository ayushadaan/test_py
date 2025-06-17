from django.db import models
import datetime

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.BigIntegerField()
    role = models.CharField(max_length=50, default="user")
    create_at = models.DateTimeField(default=datetime.date.today)
    update_at = models.DateTimeField(default=datetime.date.today)


class Order(models.Model):
    user_id = models.ForeignKey("User", on_delete=models.CASCADE)
    ice_cream = models.CharField(max_length=100)
    price = models.IntegerField(default=0 )
    order_date=models.DateTimeField(default=datetime.date.today)
    status=models.CharField(max_length=50, default="pending")
    
