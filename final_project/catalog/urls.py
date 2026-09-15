from django.urls import path
from . import views


app_name = 'catalog'

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('courses/', views.courses, name='courses'),
    path('course_detail/<int:pk>/', views.course_detail, name='course_detail'),
    path('authors/', views.authors, name='authors'),
    path('author_detail/<int:pk>/', views.author_detail, name='author_detail'),
    path('info/', views.info, name='info'),
]

