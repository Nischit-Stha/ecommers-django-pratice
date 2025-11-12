from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=300)
    logo = models.CharField(max_length=300, blank=True)
    slug = models.SlugField(max_length=300, unique=True)
    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=300)
    logo = models.CharField(max_length=300, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=300, unique=True)

    def __str__(self):
        return self.name
        
class Slider(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media')
    description = models.TextField(blank=True)
    url = models.URLField(max_length=300, blank=True)

    def __str__(self):
        return self.name

class AD(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media')
    rank = models.IntegerField()
    url = models.URLField(max_length=300, blank=True)

    def __str__(self):
        return self.name 

class Brand(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media')
    rank  = models.IntegerField()

    def __str__(self):
        return self.name    


class Customer(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media', blank=True)
    post = models.CharField(max_length=300)
    star = models.IntegerField(default=5)
    comment = models.TextField()

    def __str__(self):
        return self.name
LABELS =  (('new', 'new'), ('hot', 'hot'), ('sale', 'sale'), ('', 'default'))
class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.IntegerField()
    discounted_price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='media')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=500, unique=True)
    description = models.TextField(blank=True)
    specification = models.TextField(blank=True)
    labels = models.CharField(choices=LABELS, max_length=50, blank=True)
    stock = models.BooleanField(default=True)
    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
    subject = models.CharField(max_length=300)
    message = models.TextField()

    def __str__(self):
        return self.name
