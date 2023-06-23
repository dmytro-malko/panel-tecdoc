from django.db import models

# Create your models here.
class Marks(models.Model):
    mark_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name="Mark name")

# class Models(models.Model):
#     model_id = models.AutoField(primary_key=True)
#     mark_id = models.IntegerField(null=True)
#     name = models.CharField(max_length=255, verbose_name="Model name")


class MarksModels(models.Model):
    car_id = models.AutoField(primary_key=True)
    mark = models.CharField(max_length=255, verbose_name="Mark name")
    model = models.CharField(max_length=255, verbose_name="Model name")

class Manufacturer(models.Model):
    manufacturer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name="Manufacturer name")

class Articles(models.Model):
    article_id = models.AutoField(primary_key=True)
    manufacturer_id = models.IntegerField(null=True)
    article = models.CharField(max_length=255)
    article_clean = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    quantity = models.CharField(max_length=5, null=True)
    stock_status = models.CharField(max_length=5, null=True)
    price = models.DecimalField(max_digits = 10 , decimal_places = 2 , null=True)
    price_poland = models.DecimalField(max_digits = 10 , decimal_places = 2 , null=True)