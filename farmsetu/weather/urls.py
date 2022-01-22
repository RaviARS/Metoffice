from django.urls import path
from .views import WeatherListView, WeatherDetailView
from .views import ClimateAPI

urlpatterns = [

    path('climate/', ClimateAPI.as_view()),

    path('weather/', WeatherListView.as_view()),
    path('weather/<int:id>/', WeatherDetailView.as_view()),

]
