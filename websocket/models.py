from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Messages(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    message = models.TextField()
    to = models.ForeignKey(to=User, related_name="send_to", on_delete=models.CASCADE, null=True, blank=True)
    by = models.ForeignKey(to=User, related_name="sent_from", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['-created']