from django.db import models


class MyScreen(models.Model):
    img = models.ImageField(upload_to='myscreens/', null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)

