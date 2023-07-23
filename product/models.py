from django.db import models
import uuid
# Create your models here.

class Product(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    create_at = models.DateField(auto_created=True)
    update_at = models.DateField(auto_created=True)
    product_name = models.CharField(max_length=100)