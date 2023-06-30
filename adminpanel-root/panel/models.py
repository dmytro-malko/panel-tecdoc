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

    def __str__(self):
        return self.name

class Articles(models.Model):
    article_id = models.AutoField(primary_key=True)
    number = models.CharField(max_length=255, null=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT, null=True)
    article = models.CharField(max_length=255)
    article_clean = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    quantity = models.IntegerField(null=True, default=0)
    stock_status = models.IntegerField(null=True, default=0)
    price = models.IntegerField(null=True, default=0)
    price_poland = models.IntegerField(null=True, default=0)

class Cars_to_Articles(models.Model):
    car = models.ForeignKey(MarksModels, on_delete=models.PROTECT, null=True)
    article = models.ForeignKey(Articles, on_delete=models.PROTECT, null=True)
    year_from = models.CharField(max_length=10)
    year_to = models.CharField(max_length=10)

class Articles_Images(models.Model):
    article = models.ForeignKey(Articles, on_delete=models.PROTECT, null=True)
    image = models.CharField(max_length=255, null=True)