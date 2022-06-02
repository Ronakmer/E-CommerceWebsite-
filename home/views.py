from contextvars import Context
from email import contentmanager
from http.client import OK
from itertools import product
from multiprocessing import context
from turtle import update

from django.contrib import messages
from unittest import loader
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render,redirect
from .models import   signup,User,Product
from django.contrib.auth import logout,login,authenticate,update_session_auth_hash
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import PasswordChangeForm
from django.db.models import Q

from django.contrib.auth.decorators import login_required
from cart.cart import Cart

@login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("/")


@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_detail(request):
    return render(request, 'cart.html')

    

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

# def addtocart(request):
    # if request.method == 'POST':
        # if request.user.is_authenticated:
            
            # prod_id=int(request.POST.get('product_id'))
            # product_check=Product.objects.get(id=prod_id)
            # if(product_check):
            #     if(Cart.objects.filter(user=request.user.id,product_id=prod_id)):
            #         return JsonResponse({'status':"product already in cart"})
            #     else:
            #         prod_qty=int(request.POST.get('product_qty'))
            #             # return JsonResponse({'status':"no"})

            #         if product_check.quantity >= prod_qty:
            #             Cart.objects.create(user=request.user,product_id=prod_id,product_qty=prod_qty)
            #             return JsonResponse({'status':"add product"})
            #         else:
            #             return JsonResponse({'status':"only"})
            # else:
            #     return JsonResponse({'status':"no such product found"})

        # else:
        #      return JsonResponse({'status':"login must"})

       

    # return redirect('/')
    
# def cart(request):
#     # cart = Cart.objects.filter(product_id=request.GET['product_id'])[0]
#     cart=Cart.objects.filter(user=request.user)
#     context={'cart':cart}
#     return render(request,'cart.html',context)





def order(request):
   return render(request,'order.html')

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
    # product = Product.objects.filter(product_category=request.GET['product_category'])[0]
    # product = Product.objects.filter(product_name=request.GET['product_name'], product_category=request.GET['product_category'])[0]
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
      
        form =signup()
        # form=User()
        form.first_name=f   
        form.last_name=l
        form.username=u
        # form.gmail=g
        # form.address=a
        # form.city=c
        form.password=p
        
        form.save()
        form=User()
        form.first_name=f   
        form.last_name=l
        form.username=u
        form.password=p
        form.save()
        
      
        return redirect('/')
        # return render(request, "index.html")

   




   
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






            
#             try:
#                 return redirect(request.GET.get('return'))
#             except:
#                 return redirect('/')
#         else:
#             messages.error(request, 'Invalid Credentials, Please try again')
#             try:
#                 return redirect(request.GET.get('return'))
#             except:
#                 return redirect('/')
#     else:
#         pageView(request, True)
#         return render(request, '404.html')



# def loginuser(request):  
#     if request.method=="POST":
#         x= request.POST.get('username') 
#         y= request.POST.get('password')

#         member=signup.objects.filter(user_name=x,password=y).values()
#         Context={"myval":member}
#         for i in member:
#             if("username" in i):
#                 template=loader.get_template('index.html')
#                 return HttpResponse(template.request(Context,request))
#         return HttpResponse('no')

  
#    def password_confirm_view(request, uidb64, token):
# context = {}
# if request.method == 'POST':
#     form = SetPasswordForm(data=request.POST, user=request.user)
#     if form.is_valid():
#         form.save() #I have error
#         update_session_auth_hash(request, form.user)
#         return redirect('password_reset_done')
# else:
#     form = SetPasswordForm(user=request.user)
# context['form'] = form
# return render(request, 'mdm/registration/password_confirm.html', context)