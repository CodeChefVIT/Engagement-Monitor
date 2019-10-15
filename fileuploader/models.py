from django.db import models
import uuid
import os

# Create your models here.
def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('media/', filename)


class MyMedia(models.Model):
    upload = models.FileField(upload_to=get_file_path)




    
class Post(models.Model):
    user_name = models.CharField(max_length=200, unique=False)
    slug = models.SlugField(unique=True, default=uuid.uuid1)
    file_name = models.TextField()
    one = models.CharField( max_length = 100 )
    two = models.CharField( max_length = 100 )
    three = models.CharField( max_length = 100 )
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_on']

    