from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect
from shop.models import Category,Product
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.


def allcategories(request):
    c=Category.objects.all()
    context={'cat':c}
    return render(request,'category.html',context)


def allproducts(request,p):  #here p recieves the category id
    c=Category.objects.get(id=p)   #reads a particular category object  using id
    p=Product.objects.filter(category=c)   #reads all products under a particular category object
    context={'cat':c,'product':p}
    return render(request,'product.html',context)


def productdetails(request,p):
    p=Product.objects.get(id=p)
    context={'products':p}
    return render(request,'detail.html',context)


def user_login(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        print(u,p)
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return redirect('shop:categories')
        else:
            messages.error(request,"Invalid credentials")

    return render(request,'login.html')

def register(request):
    if (request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        cp= request.POST['cp']
        f= request.POST['f']
        l= request.POST['l']
        e= request.POST['e']

        if(p==cp):
            u=User.objects.create_user(username=u,password=p,first_name=f,last_name=l,email=e)
            u.save()

        return redirect('shop:categories')

        return render(request,'login.html')
    return render(request,'register.html')
def user_logout(request):
    logout(request)
    return redirect('shop:categories')



def addcategory(request):
    if (request.method == 'POST'):
        n = request.POST['n']
        d = request.POST['d']
        i = request.FILES['i']

        c = Category.objects.create(name=n, desc=d, image=i)  # create an new record
        c.save()
        return redirect('shop:categories')
    return render(request,'addcategory.html')

def addproduct(request):
    if(request.method=="POST"):
        n=request.POST['n']
        i=request.FILES['i']
        d=request.POST['d']
        s=request.POST['s']
        p=request.POST['p']
        c=request.POST['c']    #reads the category name from form field
        cat=Category.objects.get(name=c)               #category object/record matching with category name c
        p=Product.objects.create(name=n,image=i,desc=d,stock=s,price=p,category=cat)  #assigns each value to product fields
        p.save()
        return redirect('shop:categories')

    return render(request,'addproduct.html')



def addstock(request,p):
    product=Product.objects.get(id=p)
    if(request.method=="POST"):
        product.stock=request.POST['u']
        product.save()
        return redirect('shop:categories')


    context={'pro':product}
    return render(request,'addstock.html',context)


