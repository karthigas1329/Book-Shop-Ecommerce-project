from django import forms
from sampleapp.models import Book,Order
class ModelForm(forms,ModelForms):
	class Meta:
		model=Book
		fields="__all__"