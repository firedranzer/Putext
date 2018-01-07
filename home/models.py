from django.db import models



class Post(models.Model):
    text_input = models.CharField(max_length=1000)

