from django.db import models

# Create your models here.
class Assignment(models.Model):
    title = models.CharField(max_length=200)
    class_name = models.CharField(max_length=100)
    due_date = models.DateTimeField()
    done = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} ({self.class_name})"
