from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    address=models.CharField(max_length=200,null=True,blank=True)
    phone=models.CharField(max_length=200,null=True,blank=True)
    profile_pic=models.ImageField(upload_to="profilepics",null=True,blank=True,default="default.jpg")

    def __str__(self):
        return self.user.username

class Categories(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Scraps(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="userscrap")
    category=models.ForeignKey(Categories,on_delete=models.CASCADE,related_name="items",null=True)
    name=models.CharField(max_length=200)
    condition=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    picture=models.ImageField(upload_to="scrapimage",default="scrapimage/default.png",null=True,blank=True)
    place=models.CharField(max_length=200)
    created_date=models.DateField(auto_now_add=True)
    options=(
        ("instock","instock"),
        ("biding","biding"),
        ("soldout","soldout")
    )
    status=models.CharField(max_length=200,choices=options,default="instock")

    def __str__(self):
        return self.name
    
class WishList(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="userwishlist")
    scrap=models.ManyToManyField(Scraps)
    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.scrap.name
    
class Bids(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="userbid")
    scrap=models.ForeignKey(Scraps,on_delete=models.CASCADE,related_name="scrapbid")
    amount=models.PositiveIntegerField()
    options=(
        ("reject","reject"),
        ("pending","pending"),
        ("accept","accept")
    )
    status=models.CharField(max_length=200,choices=options,default="pending")

    def __str__(self):
        return self.scrap.name

class Reviews(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    scrap=models.ForeignKey(Scraps,on_delete=models.CASCADE,related_name="scrapreview")
    comment=models.CharField(max_length=200)
    rating=models.PositiveIntegerField()
    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment


def create_profile(sender,created,instance,**kwargs):

    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_profile,sender=User)