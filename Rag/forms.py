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

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'id': 'user-input' })