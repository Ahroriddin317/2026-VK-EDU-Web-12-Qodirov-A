from django.urls import path

from questions import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('ask', views.ask, name = "ask" ),
]