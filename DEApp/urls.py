from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('covid_plot/', views.covid_plot, name='covid_plot'),
    path('advanced_analysis/', views.advanced_analysis, name='advanced_analysis'),
    path('predictions/', views.predictions, name='predictions'),
]
