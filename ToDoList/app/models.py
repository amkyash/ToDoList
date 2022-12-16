from django.db import models

# Create your models here.

class List(models.Model):
    Title = models.CharField(max_length = 50)
    Date = models.DateField(blank = False)
    Completed = models.BooleanField(default = False)

    def __str__(self):
        return self.Title


