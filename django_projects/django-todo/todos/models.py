from django.db import models
from django.utils import timezone

class TodoItem(models.Model):
    item = models.CharField(max_length=128)
    completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    completed_date = models.DateTimeField(blank=True, null=True)

    def complete(self):
        self.completed = True
        self.completed_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.item
