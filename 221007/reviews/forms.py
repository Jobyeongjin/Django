from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = '__all__'
        # fields에서 제외할 목록💡
        exclude = ('movie_pk',)
        # 폼 수정하기💡
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': '리뷰 제목은 30자 이내로 입력해주세요.',
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'placeholder': '',
                }
            ),
            'writer': forms.TextInput(
                attrs={
                    'placeholder': '',
                }
            ),
        }
        # 라벨 변경하기💡
        labels = {
            'title': '리뷰 제목',
            'content': '내용',
            'writer': '작성자',
            'review_grade': '평점',
        }

