from django.urls import path
from carprice import views

urlpatterns = [
    path('',views.Home),
    path('carpriceprediction/', views.carpriceprediction),
    #path('carprediction/',views.carprediction),
]