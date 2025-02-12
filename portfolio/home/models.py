from django.db import models


# Create your models here.

# class Home(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField(null=True, blank=True)
#     image = models.ImageField(upload_to='images/category_images/')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.title


class About(models.Model):
    image = models.ImageField(upload_to='image/img.png')
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    phone = models.IntegerField(default=0)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.name

