from django import forms
from .models import Article
from .models import Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

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
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Заголовок'
            }),
            'text': forms.Textarea(attrs={
                'placeholder': 'Текст вашей статьи',
                'rows': 15
            }),
            'category': forms.Select(attrs={
                'class': 'form-select'
            })
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author_name', 'text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Введите ваш комментарий...'}),
            'author_name': forms.TextInput(attrs={'placeholder': 'Ваше имя'})
        }

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)