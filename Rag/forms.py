from django import forms
from .models import Article , Question_and_Answer

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__' #['title', 'content'] 


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question_and_Answer
        fields = ['message']