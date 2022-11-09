from django import forms
from .models import Author


class AutorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'surname', 'nationality', 'description']
            
        ...