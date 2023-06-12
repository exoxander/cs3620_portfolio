from django.db import models

# Create your models here.
class hobby(models.Model):

    def __str__(self):
        return self.name + "\n" + self.desc

    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)