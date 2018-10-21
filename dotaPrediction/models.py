from django.db import models

class Hero(models.Model):
    heroApiId = models.IntegerField()
    name = models.CharField(max_length=200)                   
    localized_name = models.CharField(max_length=200)         
    url_full_portrait = models.CharField(max_length=200)      
    url_large_portrait = models.CharField(max_length=200)   
    url_small_portrait = models.CharField(max_length=200) 
    url_vertical_portrait= models.CharField(max_length=200)

    def __str__(self):
        return self.name

