
from django.db import models
import base64

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=150)
    def __str__(self):
        return self.title

'''products '''

class Products(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    author = models.CharField(max_length=150)
    characteristic = models.CharField(max_length=150)

    image = models.ImageField(upload_to='images')

    base_64 = models.CharField(max_length=500000, blank = True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.base_64 = base64.b64encode(self.image.read()).decode('utf-8')
        super(Products, self).save()
###################
class Comment(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.product.author} on {self.created_at}'
