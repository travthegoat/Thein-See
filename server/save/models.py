from django.db import models
from user.models import User
import uuid

# Create your models here.
class Save(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.URLField()
    caption = models.TextField(default="No caption")
    image = models.URLField(default="https://placehold.co/400x400")
    tag = models.CharField(max_length=50)
    saved_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} saved {self.caption}"