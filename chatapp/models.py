from django.db import models

# Create your models here.
class Group(models.Model):
    groupname = models.CharField(max_length=255)
    groupid = models.CharField(max_length=3, primary_key = True)
    groupkey = models.CharField(max_length=4)

class User(models.Model):
    username = models.CharField(max_length=255, primary_key= True)
    password = models.CharField(max_length=255)
    usergroup = models.ForeignKey(Group, on_delete=models.CASCADE)

class Message(models.Model):
    
    messagecontent = models.TextField()
    messagegroup = models.ForeignKey(Group, on_delete=models.CASCADE)
    messagesender = models.ForeignKey(User, on_delete=models.CASCADE)
# author = models.ForeignKey(Author, on_delete=models.CASCADE) 


