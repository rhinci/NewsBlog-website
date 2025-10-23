from django import forms
from .models import Article

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