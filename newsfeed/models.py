from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class savedpost(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile')
    #marked_news = ArrayField( models.CharField(max_length=100, blank=True),size=10)
