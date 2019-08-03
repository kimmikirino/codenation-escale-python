from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def publish(self):
        self.publish_at = timezone.now()
        self.save()
    
class Product(models.Model):
    description = models.CharField(max_length=100)
    final_price = models.DecimalField(max_digits=10, decimal_places=2)
    suggested_price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="imgs/products/", null=True)
    has_offer = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    publish_at = models.DateTimeField(null=True, blank=True)
    category = models.ForeignKey(Category, related_name='Category', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.description

    def publish(self):
        self.publish_at = timezone.now()
        self.save()
