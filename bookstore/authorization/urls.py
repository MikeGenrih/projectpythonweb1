from django.urls import path
from . import views

urlpatterns = [
    path('aut/', views.aut, name='aut'),
    path('reg/', views.registration_view, name='reg'),
]