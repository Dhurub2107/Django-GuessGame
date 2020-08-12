from django.urls import path
from . import views
urlpatterns=[
path('login',views.login,name="login"),
path('register',views.register,name="register"),
path('home',views.home,name="home"),
path('logout',views.logout,name="logout"),
path('about',views.about,name="about"),
path('logic',views.logic,name="logic"),
path('Game',views.game,name="Game"),
path('score',views.score,name="score"),
path('update_score',views.update_score,name="update_score")

]