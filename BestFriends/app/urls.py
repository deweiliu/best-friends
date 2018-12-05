from django.urls import path
from django.conf.urls import url,include

from . import views
app_name = 'app'
urlpatterns = [path('',views.home,name="home"),
    path('api',include('app.api.urls')),
    path('home',views.home,name="home"),
    path('contact',views.contact,name="contact"),
    path('birthday',views.birthday,name="birthday"),

    path('login',views.login,name="login"),

    path('<str:user_id>/ai',views.ai,name="ai"),

    # if no url pattern matches the url from client, throw a 404 page
    url(r'',views.error404,name='404error')]
