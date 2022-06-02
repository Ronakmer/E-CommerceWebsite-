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
    # path('add-to-cart', views.addtocart, name="addtocart"),
    # path('cart', views.cart, name="cart"),
    path('search', views.search, name="search"),
    path('customerorder', views.customerorder, name="customerorder"),
    path('orderproduct', views.orderproduct, name="orderproduct"),
    path('ResetPassword', views.ResetPassword, name="ResetPassword"),



    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/',views.cart_detail,name='cart_detail'),


    

  
    
    

]
urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)