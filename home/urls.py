from django.contrib import admin
from django.urls import path,include
from home import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name="home"),
    path('index', views.index, name="index"),
    path('CustomerService', views.CustomerService, name="CustomerService"),
    path('order', views.order, name="order"),
    path('about', views.about, name="about"),
    path('signup', views.signupuser, name="signupuser"),
    path('login', views.loginuser, name="loginuser"),
    path('logout', views.logoutUser, name="logoutUser"),
    path('nav', views.nav, name="nav"),
    path('cart', views.cart, name="cart"),
    path('search', views.search, name="search"),
    path('customerorder', views.customerorder, name="customerorder"),
    path('orderproduct', views.orderproduct, name="orderproduct"),
    path('ResetPassword', views.ResetPassword, name="ResetPassword"),

  
    
    

]
urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)