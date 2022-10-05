from django import forms
from .models import Article

class ArticelForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['title', 'content']