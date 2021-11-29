from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class Post(models.Model):
    class Meta(object):
        db_table = 'post'

    name = models.CharField(
        'Name', blank=False, null=False, max_length=100, db_index=True, default='Anonymous'
    )

    body = models.CharField(
        'Body', blank=True, null=True, max_length=1400, db_index=True
    )

    created_at = models.DateTimeField(
        'Created DateTime', blank=True, auto_now_add=True
    )

    image = CloudinaryField("image", blank=True, null=True)


    like_count = models.IntegerField(default=0, null=True, blank=True)