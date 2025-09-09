
# Create your models here.
import uuid
from django.db import models

class Product(models.Model):
    all_category = [
        ('jersey', 'Jersey'),
        ('shoes', 'Shoes'),
        ('ball', 'Ball'),
        ('gear', 'Gear'),
        ('gloves', 'Gloves'),
        ('merch', 'Merch'),
        ('bag', 'Bag'),
        ('sock', 'Sock'),
        ('shorts', 'Shorts'),
        ('hoodie', 'Hoodie'),
        ('cap', 'Cap'),
        ('bottle', 'Bottle'),
        ('net', 'Net'),
        ('cone', 'Cone'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()
    category = models.CharField(max_length=20, choices=all_category)
    thumbnail = models.URLField(blank=True, null=True)
    production_date = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)
    