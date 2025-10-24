from django import forms
from .models import Article
from .models import Comment

class ContactForm(forms.Form):
    name = forms.CharField(
        min_length=2, required=True, widget=forms.TextInput(
            attrs={'placeholder': 'Ваше имя'}
        )
    )
    email = forms.EmailField(
        required=True, widget=forms.TextInput(
            attrs={'placeholder': 'E-mail'}
        )
    )
    message = forms.CharField(min_length=2, required=True, widget=forms.Textarea(
        attrs={'placeholder': 'Сообщение', 'cols': 30, 'rows': 9}
    ))


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text'] 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author_name', 'text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Введите ваш комментарий...'}),
            'author_name': forms.TextInput(attrs={'placeholder': 'Ваше имя'})
        }