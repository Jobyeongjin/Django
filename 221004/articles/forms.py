from dataclasses import field
from inspect import classify_class_attrs
from django import forms
from .models import Article # model class인 Article 연결


# 새롭게 정의하는 모델 폼 💡
class ArticleForm(forms.ModelForm):
    
    class Meta:
        # Article 모델의 특정 필드 사용하여 폼 만들기 💡
        model = Article
        fields = ['title', 'content']