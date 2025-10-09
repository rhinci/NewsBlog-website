from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),                    # /
    path('about/', views.about, name='about'),              # /about
    path('contacts/', views.contacts, name='contacts'),        # /contacts
    path('feedback/', views.feedback, name='feedback'),     # /feedback
    path('news/<int:id>/', views.news, name='news'),  # /news/<int:id>
]