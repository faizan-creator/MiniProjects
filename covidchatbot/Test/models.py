from django.db import models

# Create your models here.
class Contact(models.Model):
    product_id = models.AutoField(primary_key=True)
    userid = models.CharField(max_length=100,default="",blank=True)
    name = models.CharField(max_length=50,default="",blank=True)
    email = models.CharField(max_length=50,default="",blank=True)
    phone = models.CharField(max_length=50,default="",blank=True)
    desc = models.CharField(max_length=5000)
    timestamp = models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return self.name

class Test(models.Model):
    question_id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=5000,default="",blank=True)
    options = models.CharField(max_length=1000,default="",blank=True)
    priority = models.CharField(max_length=500,default="",blank=True)

    def __str__(self):
        return self.question