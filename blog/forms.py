from django import forms
from .models import Post

# ModelForm을 상속받는 PostModelForm 클래스 정의
class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', )

# Form을 상속받는 PostForm 클래스 정의

def min_length_5_validator(value):
    if len(value) < 5:
        # ValidataionError 예외를 강제로 발생시킨다
        raise forms.ValidationError('text는 5글자 이상 입력해 주세요!')

class PostForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea, validators=[min_length_5_validator])