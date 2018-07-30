from django import forms
from .models import Clipboard
class ClipboardForm(forms.ModelForm):
	class Meta:
		model = Clipboard
		fields = ('name','description','cover_photo')