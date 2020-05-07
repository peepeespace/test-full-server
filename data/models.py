from django.db import models
from django.conf import settings

class ControlState(models.Model):
    user = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    want_state = models.CharField(max_length=10)

    def __str__(self):
        return self.user

class ToolState(models.Model):
    user = models.CharField(max_length=100)
    tool_state = models.CharField(max_length=10)

    def __str__(self):
        return self.user