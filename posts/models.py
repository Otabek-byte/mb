from django.db import models

# Create your models here.
class Post(models.Model):
    text = models.TextField()
    def __str__(self):
        """Строковое отоброжение модели"""
        return self.text[:50]
