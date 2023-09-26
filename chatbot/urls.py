from django.urls import path
from . import views


urlpatterns = [
    path('', views.chatbot, name='chatbot'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('history', views.history, name='history'),
    path('logout', views.logout, name='logout'),
    # path('clear', views.clear, name='clear')
]