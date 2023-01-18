from django.urls import path
from. import views

#register the app namespace
app_name = 'poll'

urlpatterns = [
    path('register/',views.register, name = 'register'),
    path('', views.index,name = 'index' ),
    path('vote/<str:pk>',views.vote,name = 'vote'),
    path('result/<str:pk>', views.result,name = 'result'),
    path('postquestion/',views.Post,name = 'question'),
    path('choice/',views.Postchoice,name = 'choice'),
    path('profile/',views.profile,name = 'profile'),
    
]
