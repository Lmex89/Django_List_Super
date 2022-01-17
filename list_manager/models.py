from django.db import models
import uuid
# Create your models here.


class Category(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=255, )
    code = models.CharField(max_length=10, unique=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Items(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    is_done = models.BooleanField(default=False, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
