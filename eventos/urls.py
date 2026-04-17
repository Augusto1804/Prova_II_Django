from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('novo/', views.novo_evento, name='novo'),
]
