from django.db import models

# Create your models here.
class Hobby(models.Model):

    def __str__(self):
        return self.name + "\n" + self.desc + "\n"

    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)

class Portfolio(models.Model):

    def __str__(self):
        return self.name + "\n" + self.desc + "\n"

    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
