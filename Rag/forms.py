from django import forms
from .models import Article , Question

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__' #['title', 'content'] 


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']