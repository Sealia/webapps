from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=30)
	description = models.TextField()

	class Meta:
		verbose_name_plural = "Categories"
	def __str__(self):
		return self.name



class Post(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
	title = models.CharField(max_length = 140)
	body = models.TextField()
	date_create = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now=True)
	date_publish = models.DateTimeField(auto_now_add=True)
	public=models.BooleanField(default=False)

	def __str__(self):
		return self.title