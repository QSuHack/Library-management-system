from django.db import models

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
    added_date = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=Status.choices)
    cover = models.CharField(max_length=200, blank=True, null=True, default=None)
    signature = models.CharField(max_length=30)
    
class Reader (models.Model):
    is_suspended = models.BooleanField(default=False)
    account =  models.DecimalField(decimal_places=2, default=0)
    books_issued = models.ManyToManyField(to=Book, on_delete=models.SET_NULL, null=True, blank=True)
class Request(models.Model):
    user =models.ForeignKey(to=Reader, on_delete=models.SET_NULL)
    date= models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE)
