from __future__ import unicode_literals

from django.db import models

# Create your models here.
class product(models.Model):
    author = models.CharField(max_length=100)
    name = models.CharField(max_length=120)
    image = models.FileField(null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=4, decimal_places=2)


    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
