from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
import datetime

class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=100)

def __str__(self):
    return self.username

class Posts(models.Model):
#    user = models.ForeignKey(User, on_delete=models.CASCADE)
   title = models.CharField(max_length=200)
   content  = RichTextUploadingField()
   created_at = models.DateTimeField(auto_now=True)
def __str__(self):
        return self.title