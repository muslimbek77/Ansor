
from django.urls import path
from blog import views

urlpatterns = [
     path('', views.home, name='home'),
     path('about_detail/<int:pk>',views.about_detail, name='about_detail'),
     path('about_course',views.about_course, name='about_course')
]
