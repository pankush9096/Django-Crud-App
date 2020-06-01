from django.contrib import admin
from django.urls import path

from myapp import views

urlpatterns = [
    path('welcome', views.home),
    path('about', views.about),
    path('contactus', views.contact),
    path('templaterendering',views.templaterendering),
    path('register', views.form_view, name= 'register'),
    path('thanks', views.thanks, name= 'thanks'),
    path('api/', views.LoginList.as_view()),
    path('json', views.json),

    # name is non essential parameter whcih will allocate memory to subjected view

]