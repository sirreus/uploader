from django.db import models

# Create your models here.


class Document(models.Model):
    title = models.CharField(max_length=120)
    name = models.TextField()
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title
