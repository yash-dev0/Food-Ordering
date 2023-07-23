from django.db import models
import uuid
# Create your models here.

class Product(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    product_name = models.CharField(max_length=100) 
    create_at = models.DateField(auto_created=True)
    update_at = models.DateField(auto_created=True)


class ProductImages(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    product_images = models.ImageField(upload_to='templates/product_images')
    create_at = models.DateField(auto_created=True)
    update_at = models.DateField(auto_created=True)