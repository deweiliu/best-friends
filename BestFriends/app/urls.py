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

    path('<str:username>/ai',views.ai,name="ai"),
    path('js_ai',views.js_ai,name="js_ai"),
    path('conversation',views.conversation,name="conversation"),
    url(r'',views.error404,name='404error')]
