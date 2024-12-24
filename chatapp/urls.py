from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('chat/', views.chat_view, name='chat')
    ]