from django.urls import path
from . import views
app_name = 'login'
urlpatterns = [
    path('', views.LoginCbv.as_view()),
]