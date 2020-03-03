from django.db import models


# Create your models here.
class Product(models.Model):

  title = models.CharField(max_length = 200)
  price = models.FloatField()
  discount_price = models.FloatField()
  category = models.CharField(max_length = 200)
  description = models.TextField()
  image = models.CharField(max_length = 300)

  def __str__(self):
    return self.title


class Order(models.Model):

  items = models.CharField(max_length = 1000)
  total = models.FloatField()
  name = models.CharField(max_length = 200)
  email = models.CharField(max_length = 200)
  address = models.CharField(max_length = 1000)
  city = models.CharField(max_length = 200)
  state = models.CharField(max_length = 200)
  zipcode = models.CharField(max_length = 20)

  def __str__(self):
    return f'Order from {self.name}'
