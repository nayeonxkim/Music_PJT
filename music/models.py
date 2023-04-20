from django.db import models

# Create your models here.
class Music(models.Model):
    title = models.TextField()
    singer = models.TextField()
    release_date = models.DateField()

    def __str__(self):
        return self.title