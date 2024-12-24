from django.contrib import admin

# Register your models here.
from .models import Group, User, Message

admin.site.register(Group)
admin.site.register(User)
admin.site.register(Message)

