from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    address=models.CharField(max_length=200,null=True,blank=True)
    phone=models.CharField(max_length=200,null=True,blank=True)
    profile_pic=models.ImageField(upload_to="profilepics",null=True,blank=True)

    def __str__(self):
        return self.user.username

class Category(models.Model):
    options=(
        ("metal","metal"),
        ("plastic","plastic"),
        ("paper","paper"),
        ("electronic","electronic"),
        ("textile","textile"),
        ("glass","glass"),
        ("organic","organic"),
        ("rubber","rubber")
    )
    name=models.CharField(max_length=200,choices=options)

    def __str__(self):
        return self.name

class Scraps(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="userscrap")
    name=models.CharField(max_length=200)
    condition=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    picture=models.ImageField(upload_to="scrapimage")
    place=models.CharField(max_length=200)
    category=models.ForeignKey(Category,related_name="scrapcategory")
    created_date=models.DateField(auto_now_add=True)
    options=(
        ("forsale","forsale"),
        ("underbiding","underniding"),
        ("soldout","soldout")
    )
    status=models.CharField(max_length=200,choices=options,default="available")

    def __str__(self):
        return self.name
    



