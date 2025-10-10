from django.shortcuts import render, redirect
import datetime
from django.http import Http404
from django import forms
from .forms import ContactForm
from django.contrib import messages

ARTICLES = [
    {'id': 1, 'title': 'Первая статья', 'content': 'Текст 1', 'date': datetime.date.today()},
    {'id': 2, 'title': 'Вторая статья', 'content': 'Текст 2', 'date': datetime.date(2025, 1, 1)},
]

def index(request):
    return render(request, 'index.html', {'articles': ARTICLES})

def about(request):
    return render(request, 'blog/about.html')

def contacts(request):
    return render(request, 'blog/contacts.html')

def feedback(request):
    context = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Доступ к очищённым данным:
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message_text = form.cleaned_data['message']
            # Здесь можно обработать данные: отправить письмо, сохранить в БД и т.п.
            # Например: send_mail(...), Model.objects.create(...)

            messages.success(request, "Спасибо! Сообщение отправлено.")
            return redirect('feedback')  # замените на имя вашего URL или на redirect(request.path)
    else:
        form = ContactForm()
    return render(request, 'blog/feedback.html', {'form': form})

def news(request, id):
    article = next((a for a in ARTICLES if a['id'] == id), None)
    if not article:
        raise Http404("Статья не найдена")
    return render(request, 'blog/news.html', {'article': article})