from django.urls import path
from . import views

urlpatterns = [
    path('lesson_4/', views.lesson_4_homework, name='lesson_4_homework'),
]
