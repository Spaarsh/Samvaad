from django.contrib import admin
from users.models import Room, Message
# Register your models here.

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass