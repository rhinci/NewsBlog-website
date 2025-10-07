from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),                    # /
    path('about/', views.about, name='about'),              # /about
    path('contact/', views.contact, name='contact'),        # /contact
    path('feedback/', views.feedback, name='feedback'),     # /feedback
    path('news/<int:id>/', views.news, name='news'),  # /news/<int:id>
]