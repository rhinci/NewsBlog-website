from django.shortcuts import render
import datetime
from django.http import Http404

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
    
    return render(request, 'blog/feedback.html')

def news(request, id):
    article = next((a for a in ARTICLES if a['id'] == id), None)
    if not article:
        raise Http404("Статья не найдена")
    return render(request, 'blog/news.html', {'article': article})