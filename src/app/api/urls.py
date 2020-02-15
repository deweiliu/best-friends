from django.urls import path
from app.api import views 
urlpatterns = [path('',views.api,name="api"),]
