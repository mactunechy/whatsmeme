from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from . import models
from . import forms

from django.views import generic 
# Create your views here.
  
class PostCreateView(generic.CreateView):
	form_class = forms.PostCreateForm
	template_name = 'posts/post_form.html'
	redirect_field_name = 'posts/post_detail.html'
	
	
	
	
class PostListView(generic.ListView):
	model = models.Post
	template_name = 'posts/post_list.html'
	
	
	
class PostDetailView(generic.DetailView):
	
	model = models.Post
	template_name= 'posts/post_detail.html'
	
	def print_meme(self):
		post = get_object_or_404(models.Post, pk= self.pk)
		return print(post.meme)
	
	
	
	
					