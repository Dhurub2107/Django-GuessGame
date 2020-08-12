from django.db import models
# Create your models here.

class account(models.Model):
    user_id= models.AutoField(primary_key=True)
    user_name=models.CharField(max_length=30)
    email=models.EmailField(max_length=255,unique=True)
    password=models.CharField(max_length=200)
    def __str__(self):
        return self.user_name
class score(models.Model):
    score=models.IntegerField()

