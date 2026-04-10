from django.urls import path

from questions import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('ask', views.ask, name = "ask" ),
    path('question', views.question, name = "question" ),
    path('profile', views.profile, name = "profile" ),
    path('login', views.login, name = "login" ),
    path('signup', views.signup, name = "signup" ),
    path('hot', views.hot, name = "hot" ),
]