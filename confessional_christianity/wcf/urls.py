from django.urls import path

from . import views

urlpatterns = [
    path('<int:chapter>/', views.index, name='index'),
]