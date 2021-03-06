from __future__ import unicode_literals

from django.db import models

# Create your models here.
def upload_location(instance, filename):
    return "%s/%s" % ("image", filename)

class Album(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False, auto_now_add=False)

    def __unicode__(self):
        return self.title

class Image(models.Model):
    album = models.ForeignKey(Album)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to=upload_location,
            null=True,
            blank=True,
            height_field="height_field",
            width_field="width_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)