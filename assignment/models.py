from django.db import models

# Create your models here.
class User(models.Model):
  name = models.CharField(max_length=50)

# User and Address has OnetoMany relationship
class Address(models.Model):
  user = models.ForeignKey(User, on_delete= models.CASCADE)
  address = models.TextField(max_length=255)

#User and Remark has OnetoOne relationship
class Remark(models.Model):
  user = models.OneToOneField(User,on_delete= models.CASCADE)
  remark = models.CharField(max_length=255)

