from django.db import models

# Create your models here.
class Hobby(models.Model):

    def __str__(self):
        return self.name + ": " + self.desc + " | "

    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    img = models.CharField(max_length=500, default="https://steamuserimages-a.akamaihd.net/ugc/106232967022720363/48DED32DECDB08B6A6377E2AC750277BCF2330A0/")

class Portfolio(models.Model):

    def __str__(self):
        return self.name + ": " + self.desc + " | "

    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    img = models.CharField(max_length=500, default="https://steamuserimages-a.akamaihd.net/ugc/106232967022720363/48DED32DECDB08B6A6377E2AC750277BCF2330A0/")

    #default image
    #https://steamuserimages-a.akamaihd.net/ugc/204179658730228724/7DA3284CED8D923FECBC5BBB11D021B5842FE4A0/
    #https://steamuserimages-a.akamaihd.net/ugc/106232967022720363/48DED32DECDB08B6A6377E2AC750277BCF2330A0/

class Message(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    message = models.CharField(max_length=1024)