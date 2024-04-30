from django.db import models

class Plates(models.Model):
    "Plate of table"
    name = models.CharField(max_length=60, null=False)
    description = models.TextField(null=False)
    image = models.URLField()
    price = models.FloatField(max_length=30,null=False)

