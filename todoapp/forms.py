from django import forms
from .models import *
class TodoForm(forms.ModelForm):
    
    class Meta:
        model = TodoModel
        fields = '__all__'
        

    # title=forms.CharField(max_length=100, required=False)
    # created=forms.DateField( required=False)
    # desc=forms.CharField( max_length=250, required=False)
    # status=forms.BooleanField(default=False)


