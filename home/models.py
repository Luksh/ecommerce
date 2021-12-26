from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.conf import settings

# Create your models here.

LABELS = (('hot', 'hot'), ('new', 'new'), ('', 'default'))

class Category(models.Model):
	name = models.CharField(max_length = 400)
	logo = models.CharField(max_length = 200)
	slug = models.CharField(max_length = 300, unique = True)

	def __str__(self):
		return self.name

	def get_category_url(self):
		return reverse("category", kwargs = {'slug': self.slug})	

class Slider(models.Model):
	name = models.CharField(max_length = 300)
	image = models.ImageField(upload_to = 'media')
	description = models.TextField(blank = True)
	url = models.CharField(max_length = 500, blank = True)

	def __str__(self):
		return self.name

class Ad(models.Model):
	name = models.CharField(max_length = 300)
	image = models.ImageField(upload_to = 'media')
	description = models.TextField(blank = True)
	url = models.CharField(max_length = 500, blank = True)
	rank = models.IntegerField()

	def __str__(self):
		return self.name

class Brand(models.Model):
	name = models.CharField(max_length = 300)
	image = models.ImageField(upload_to = 'media')
	slug = models.CharField(max_length = 300, unique = True)

	def __str__(self):
		return self.name

class Product(models.Model):
	name = models.CharField(max_length = 300)
	image = models.ImageField(upload_to = 'media')
	price = models.IntegerField(null = True)
	discounted_price = models.IntegerField(default = 0)
	size = models.CharField(max_length = 300)
	color = models.CharField(max_length = 300)
	description = models.TextField(blank = True)
	specification = models.TextField(blank = True)
	category = models.ForeignKey(Category, on_delete = models.CASCADE)
	labels = models.CharField(choices = LABELS, max_length = 200, blank = True)
	brand = models.ForeignKey(Brand, on_delete = models.CASCADE)
	slug = models.CharField(max_length = 300, blank = True)

	def __str__(self):
		return self.name

	def get_product_url(self):
		return reverse("product", kwargs = {'slug': self.slug})

class Contact(models.Model):
	name = models.CharField(max_length = 300)
	email = models.EmailField(max_length = 400)
	subject = models.TextField()
	message = models.TextField(blank = True)	

	def __str__(self):
		return self.name

class Cart(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
	slug = models.CharField(max_length = 300)
	items = models.ForeignKey(Product, on_delete = models.CASCADE)
	quantity = models.IntegerField(default = 1)
	checkout = models.BooleanField(default = False)

	def __str__(self):
		return self.user.username