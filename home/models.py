from django.db import models


class Post(models.Model):
    text_input = models.TextField(max_length=1000)