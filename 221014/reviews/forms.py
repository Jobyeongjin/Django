from turtle import textinput
from .models import Review
from django.forms import ModelForm, Textarea, TextInput, RadioSelect


class ReviewForm(ModelForm):

    class Meta:
        model = Review
        fields = (
            'title',
            'content',
            'gift_card',
            'grade',
            'image1',
            'image2',
            'image3',
        )
        widgets = {
            'title': TextInput (
                attrs= {
                    'class': 'form-control',
                    'style': 'max-width: 100%; border-style: solid;',
                }
            ),
            'content': Textarea (
                attrs= {
                    'class': 'form-control',
                    'style': 'max-width: 100%; border-style: solid;',
                }
            ),
            'gift_card': TextInput (
                attrs= {
                    'class': 'form-control',
                    'style': 'max-width: 100%; border-style: solid;',
                }
            ),
            'grade': RadioSelect,
        }
        