from contextvars import Context
from email import contentmanager
from http.client import OK
from itertools import product
from multiprocessing import context
from turtle import update
from unicodedata import name

from django.contrib import messages
from unittest import loader
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render,redirect
from .models import   signup,User,Product,order
from django.contrib.auth import logout,login,authenticate,update_session_auth_hash
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import PasswordChangeForm
from django.db.models import Q

from django.contrib.auth.decorators import login_required
from cart.cart import Cart

from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework import serializers,viewsets
from home.serializers import UserSerializer

# @login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    messages.success(request, 'Product Add To Cart')
    return redirect("/")


# @login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    messages.success(request, 'Product Clear ')
    return redirect("cart_detail")


# @login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


# @login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


# @login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    # messages.success(request, 'Product Clear In Cart')  
    return redirect("cart_detail")


# @login_required(login_url="/users/login")
def cart_detail(request):
    return render(request, 'cart.html')


def checkout(request):
    if request.method =='POST':
        # f=request.POST['fname']
        
        address=request.POST.get('address')
       
        state=request.POST.get('state')
        city=request.POST.get('city')
        pincode=request.POST.get('pincode')
    
        phone=request.POST.get('phone')

        cart=request.session.get('cart')
        uid=request.session.get('_auth_user_id')
        username=User.objects.get(pk=uid)
        print(cart,uid,username)
        # print(cart,User,"============")
        # print(repr(User))
        # print(order,"===========")
        #  username = User(username=User),

        for i in cart:
            a=((cart[i]['price']))
            b=cart[i]['quantity']
            total=a*b
            # print(i)
            Order=order(
                username = username,
                # username = User(username=User),
                # username = User(request.user),
                # username=User[i]['Username'],
                # user=User,
                # username=User.request,
                # username=User[i][uid],
                # username="asdasdad",
                product_name=cart[i]['name'],
                product_price=cart[i]['price'],
                product_qty=cart[i]['quantity'],
                product_image=cart[i]['image'],
                address=address,
                pincode=pincode,
                number=phone,
                total=total,
                city=city,
                state=state,
            )
            # Order=Product.objects.filter(product_id=request.GET['product_id'])[0]
            # Order.quantity=Order.quantity - cart.product_qty
            Order.save()
            # (product_name=request.GET['product_name'])[0]
            # Order=Product.objects.filter(product_id=cart.name).first()
          
            # orderproduct.save()

            
            messages.success(request, 'This is Checkout')
        request.session['cart'] = {}
            # print(Order)
            
        # print(Order.placeOrder())
        # Order.save(commit=False)

        return redirect("index")
            
    return render(request,'cart.html')


def checkouts(request):
    # if request.method =='POST':

        
    #     address=request.POST.get('address')
       
    #     state=request.POST.get('state')
    #     city=request.POST.get('city')
    #     pincode=request.POST.get('pincode')
    
    #     phone=request.POST.get('phone')
        
    #     # product=Product.objects.filter(product_name='product_name')

    #     # products=request.session.get('products')
    #     uid=request.session.get('_auth_user_id')
    #     username=User.objects.get(pk=uid)
    #     product_name=Product.objects.get(product_name=product_name)
    #     print(product_name,uid,username)

    #     # products = Product.objects.filter(product_name=request.GET['product_name'])
    #     # for i in products:
    #         # a=(int(cart[i]['price']))
    #         # b=cart[i]['quantity']
    #         # total=a*b
    #         # print(i)
    #     Order=order(
                
    #             # username = username,
    #             product_name=product_name,
    #             # product_name=products[i]['name'],
    #             # product_price=products[i]['price'],
    #             # product_qty=products[i]['quantity'],
    #             # product_image=products[i]['image'],
    #             address=address,
    #             pincode=pincode,
    #             number=phone,
    #             # total=total,
    #             city=city,
    #             state=state,
    #         )

    #     Order.save()


            
    #     messages.success(request, 'This is Checkout')



    #     return redirect("index")
            
    return render(request,'cart.html')





# Create your views here.
def index(request):
    product=Product.objects.all()
    
    # print(product,'-----------')
    return render(request,'index.html',{'product':product})
    # return render(request,'index.html').order_by('-id')  product_des__icontains=q


def search(request):
    q=request.GET['q']
    data=Product.objects.filter(Q(product_name__icontains=q) | Q(product_des__icontains=q))
    # data=Product.objects.filter(product_des__icontains=q)
    # print("======================")
    return render(request,'search.html',{'data':data})






def about(request):
    return render(request,'about.html')

def nav(request):
    product=Product.objects.all()

    return render(request,'nav.html',{'product':product})


def customerorder(request):
    return render(request,'customerorder.html')
    


def CustomerService(request):
    # customerservice=Customerservice.objects.all()
    # print(customerservice,'-----------')
    return render(request,'CustomerService.html')


def orderproduct(request):
  
   
    # product_price = Product.objects.filter(product_price=request.GET['product_price'])[1]
   
    product = Product.objects.filter(product_name=request.GET['product_name'])[0]
    category = Product.objects.filter(product_category=request.GET['product_category'])
   
    # product1 = Product.objects.filter(product_category=request.GET['product_category'])[0]
    
    # print(product_name,"============")
    return render(request,'orderproduct.html',{'product':product,'Category':category})

def pageView(request, isError=False):
    # Page View Counter
    pass 

def loginuser(request):  
    if request.method == 'POST':
        pageView(request)
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username =username, password=password)
        if user is not None and len(password)>7:
            login(request, user)
            messages.success(request, 'Successfully Logged In')
            try:
                return redirect(request.GET.get('return'))
            except:
                return redirect('/')
        else:
            messages.warning(request, 'Invalid Credentials, Please try again')
            try:
                return redirect(request.GET.get('return'))
            except:
                return redirect('/')
    else:
        pageView(request, True)
        return render(request, '404.html')

def logoutUser(request):
    if request.method == 'POST':
        pageView(request)
        logout(request)
        messages.success(request, 'Successfully Logged Out')
        try:
            return redirect(request.GET.get('return'))
        except:
            return redirect('/')
    else:
        pageView(request, True)
        return render(request, '404.html')    
        
def signupuser(request):

    if request.method =='POST':
        f=request.POST['fname']
        l=request.POST['lname']
        u=request.POST['username']
        # g=request.POST['email']
        # a=request.POST['address']
        # c=request.POST['city']
        p=make_password(request.POST['pass1'])
        # p=request.POST['pass1']
      
        # form =signup()
        # form.first_name=f   
        # form.last_name=l
        # form.username=u
        # form.password=p
        
        # form.save()
        # messages.success(request, 'User Registration Successfully')
        form=User()
        form.first_name=f   
        form.last_name=l
        form.username=u
        form.password=p
        form.save()
        # messages.success(request, 'User Registration Successfully')
        
      
        return redirect('/')
        # return render(request, "index.html")
    # else:
    #     messages.success(request, 'User Registration not')

   




   
def ResetPassword(request):
    if request.method=="POST":
        fm=PasswordChangeForm(user=request.user,data=request.POST)
        # print(fm)
        if fm.is_valid(): 
            fm.save()
            # print('====================')
            update_session_auth_hash(request,fm.user)
            return HttpResponseRedirect('/index')
    else:
        fm= PasswordChangeForm(user=request.user)
    return render(request, 'ResetPassword.html',{'form':fm})
    # return render(request, 'ResetPassword.html')




# @api_view(['GET'])
# def view_items(request):
#     if request.method == 'GET':
#         tutorials = User.objects.all()
        
#         title = request.query_params.get('title', None)
#         if title is not None:
#             tutorials = tutorials.filter(title__icontains=title)
        
#         tutorials_serializer = UserSerializer(tutorials, many=True)
#         return Response(tutorials_serializer.data)