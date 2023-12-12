
from django.db import models

class GeneratedDescription(models.Model):
    product_name = models.CharField(max_length=255)
    keywords = models.TextField()
    description = models.TextField()
