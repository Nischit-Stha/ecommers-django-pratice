from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=300)
    logo = models.CharField(max_length=300)
    slug = models.CharField(max_length=300, unique=True)
    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=300)
    logo = models.CharField(max_length=300)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.CharField(max_length=300, unique=True)

    def __str__(self):
        return self.name
        
class slider(models.Model):
    name = models.CharField(max_length=300)
    image = models.imageField(upload_to='media')
    description = models.TextField(blank=True)
    url = models.UrlField(max_length=300)

    def __str__(self):
        return self.name

class AD(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media')
    rank = models.IntegerField()
    url = models.UrlField(max_length=300)

    def __str__(self):
        return self.name 

class Brands(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media')
    rank  = models.IntegerField()


    def __str__(self):
        return self.name    


class Costumer(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media')
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
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    SubCategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE)
    slug = models.TextField(unique=True)
    discription = models.TextField(blank=True)
    specification = models.TextField(blank=True)
    labels = models.CharField(choices=LABELS,max_length=50)
    stock = models.BooleanField(default=True)
    def __str__(self):
        return self.name


class Contact()(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
    subject = models.CharField(max_length=300)
    message = models.TextField()

    def __str__(self):
        return self.name
