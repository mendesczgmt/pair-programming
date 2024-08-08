from django.db import models
import uuid

class Livros(models.Model):
    uuid = models.UUIDField(default = uuid.uuid4, primary_key=True)
    id = models.IntegerField(blank=False, null=False)
    nome = models.CharField(max_length=100, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(max_length=100, blank=False, null=False)
