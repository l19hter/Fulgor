from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    image_url = models.URLField()

    def get_absolute_url(self):
        return f'/shop/item/{self.pk}/'
