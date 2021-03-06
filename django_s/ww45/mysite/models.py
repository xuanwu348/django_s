#encoding:utf-8
from django.db import models

# Create your models here.
class Maker(models.Model):
    name = models.CharField(max_length=10)
    country = models.CharField(max_length=10)

    def __str__(self):
        return "{}".format(self.name)

class PModel(models.Model):
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    url = models.URLField(default="http://localhost:8080/STD/NOKIA.png")

    def __str__(self):
        return "{}".format(self.name)

class Product(models.Model):
    pmodel = models.ForeignKey(PModel, on_delete=models.CASCADE, verbose_name="型号")
    nickname = models.CharField(max_length=15, default="Very perform mobile phone", verbose_name="昵称")
    description = models.TextField(default="No description", verbose_name="描述")
    year = models.PositiveIntegerField(default=2016, verbose_name="年份")
    price = models.PositiveIntegerField(default=0, verbose_name="价格")

    def __str__(self):
        return "{}".format(self.nickname)

class PPhoto(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.CharField(max_length=20, default="Product photo")
    url = models.URLField(default="http://localhost:8080/product/nokia.png")

    def __str__(self):
        return "{}".format(self.product)


