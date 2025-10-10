from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'), 
    path('feedback/', views.feedback, name='feedback'),
    path('news/<int:id>/', views.news, name='news'),
#    path('feedback/success/', views.success, name='success_url'),
]