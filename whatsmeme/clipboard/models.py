from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Clipboard(models.Model):
	name = models.CharField(max_length=200,unique=True)
	description = models.TextField()
	cover_photo = models.FileField(upload_to="clipboards/")
	slug				= models.SlugField(unique="True")
	
	def save(self,*args,**kwargs):
		self.slug = slugify(self.name)
		return super().save(*args,**kwargs)
		
	def get_absolute_url(self):
		return reverse('clipboard_detail', kwargs={"slug":self.slug})		
	