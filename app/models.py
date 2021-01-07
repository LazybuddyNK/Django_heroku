from django.db import models

class Upload(models.Model):

    img = models.ImageField(blank=True, null=True, upload_to='pics')
    desc = models.TextField(max_length=20)