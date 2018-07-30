from django.db import models
from clipboard.models import Clipboard
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()
class Post(models.Model):
	title = models.CharField(max_length = 200)
	by = models.ForeignKey(User, related_name = 'posts', on_delete = models.CASCADE,)
	meme = models.FileField( null=False)
	clipboard = models.ForeignKey(Clipboard,related_name="posts",blank=True,null=True,on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now = True)
	likes = models.ForeignKey(User,related_name='likes',blank=True,null=True,on_delete=models.CASCADE)

	
	def get_absolute_url(self):
		return reverse('posts:post_detail',kwargs={'pk':self.pk})
	
	
	def __str__(self):
		return self.title
		
	class Meta:
		ordering = ['-created_at']
			
		
		
		
class Comment(models.Model):
	commenter = models.ForeignKey(User,related_name='comments',on_delete=models.CASCADE)
	text = models.TextField()
	post = models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
	commented_at = models.DateTimeField(auto_now=True)			
	
	class Meta:
		ordering = ['-commented_at']
				
				
				