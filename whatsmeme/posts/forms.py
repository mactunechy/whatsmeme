from django import forms
from . import models


class PostCreateForm(forms.ModelForm):
	class Meta:
		model = models.Post
		fields = ('meme','title',)
	
	
class CommentCreateForm(forms.ModelForm):
	class Meta:
		model = models.Comment
		fields = ('text',)
		
				