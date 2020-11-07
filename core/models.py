from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Book(models.Model):
    class Status(models.IntegerChoices):
        UNKNOWN = -1
        AVALIABLE = 0 
        ISSUED =  1
        ON_SITE = 2
        TEMPONARY_UNAVAILABLE = 3 
        MISSING = 4
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    added_date = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=Status.choices)
    cover = models.CharField(max_length=200, blank=True, null=True, default=None)
    signature = models.CharField(max_length=30)
    
class Reader (models.Model):
    user = models.OneToOneField(to=User, on_delete =models.CASCADE)
    is_suspended = models.BooleanField(default=False)
    account =  models.DecimalField(max_digits=8,decimal_places=2, default=0)
    issue_limit = models.IntegerField(default=10)
    books_issued = models.ManyToManyField(to=Book)
    
class Request(models.Model):
    user =models.ForeignKey(to=Reader, on_delete=models.SET_NULL, null=True)
    date= models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)