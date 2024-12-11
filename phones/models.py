from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

class Phone(models.Model):

    name = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.CharField(max_length=1000)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(null=True) 

    def __str__(self):
        return self.name
    
    def save(self,  *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Phone, self).save(*args, **kwargs)
