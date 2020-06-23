from django import forms
from .models import Todo, Details

class TodoForm(forms.ModelForm):
    class Meta:
        model=Todo
        fields='__all__'