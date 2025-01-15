from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('mediatheque/', views.mediatheque, name='mediatheque'),
    path('quisommesnous/', views.quisommesnous, name='quisommesnous'),
    path('solutions/', views.solutions, name='solutions'),
    path('solutions/<slug:slug>/', views.solution_detail, name='solution_detail'),
]
