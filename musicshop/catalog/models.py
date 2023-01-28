from django.db import models


# Create your models here.
class Catalog(models.Model):
    name = models.CharField(max_length=255)
    price = models.TextField()
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    # показывает квари сет в виде имени вместо ключа
    def __str__(self):
        return self.name
