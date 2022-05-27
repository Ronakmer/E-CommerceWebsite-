from contextvars import Context
from http.client import OK
from turtle import update
from django.contrib import messages
from unittest import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import  signup,Product,User
from django.contrib.auth import logout,login,authenticate,update_session_auth_hash
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import PasswordChangeForm
from django.db.models import Q

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

def cart(request):
    product=Product.objects.all()
    # product = Product.objects.filter(product_name=request.GET['product_name'])[0]
    
    return render(request,'cart.html',{'product':product})
    
    # results = []

    # if request.method == "GET":

    #     query = request.GET.get('search')

    #     if query == '':

    #         query = 'None'

    #     results = Product.objects.filter(Q(product_name=query) | Q(product_des=query))

    # return render(request, 'search.html', {'query': query, 'results': results})
        


# def delete(request, id):
#   member = Members.objects.get(id=id)
#   member.delete()
#   return HttpResponseRedirect(reverse('index'))





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
    
    # print(product_name,"============")
    return render(request,'orderproduct.html',{'Product':product})

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
        # p=make_password(request.POST['pass1'])
        p=request.POST['pass1']
      
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