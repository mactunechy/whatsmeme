from django.shortcuts import render
from .models import Clipboard
from .forms import ClipboardForm
from django.views import generic
# Create your views here.

class ClipboardListView(generic.ListView):
	model = Clipboard
	template_name = 'Clipboard/Clipboard_list.html'
	
	
class ClipboardDetailView(generic.DetailView):
	model = Clipboard
	template_name = 'clipboard/clipboard_detail.html'
	
	
class ClipboardCreateView(generic.CreateView):
	form_class = ClipboardForm
	template_name = 'clipboard/clipboard_form.html'
	
	
			