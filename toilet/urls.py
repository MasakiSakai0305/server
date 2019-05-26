from django.urls import path

from . import views

app_name = 'toilet'
urlpatterns = [
    path('', views.index, name='index'),
    path('papirus', views.papirus, name = 'papirus'),
    
]