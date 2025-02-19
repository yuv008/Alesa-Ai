from django.db import models


class DreamInterpretation(models.Model):
    dream_description = models.TextField()
    interpretation = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
