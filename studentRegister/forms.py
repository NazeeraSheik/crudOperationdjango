from django import forms
from .models import Student


class studentForm(forms.ModelForm):
	class Meta:
		model=Student
		fields="__all__"
	def __init__(self,*args,**kwargs):
		super(studentForm,self).__init__(*args,**kwargs)
		self.fields['position'].empty_label="select"
    