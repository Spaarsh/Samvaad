from django.db import models
from django.conf import settings

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='static/room_logos/', blank=True, null=True)
    description = models.TextField()
    allowed_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='rooms', blank=True)