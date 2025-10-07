from django.shortcuts import render

def index(request):
    context = {'articles': []} 
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')

def feedback(request):
    
    return render(request, 'blog/feedback.html')

def news(request, id):
    return render(request, 'blog/news_detail.html', {'id': id, 'title': f'Статья {id}'})