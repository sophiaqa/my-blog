from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    body = models.CharField(max_length=400)
    pub_date = models.DateTimeField(auto_now=False, auto_now_add=False)
