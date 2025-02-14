from django.shortcuts import render,redirect
from CarApp.models import CarDB,BrandDB,SpecificationsDB,FeatureDB
from WebApp.models import ContactDB

# Create your views here.

def homepage(req):
    data=BrandDB.objects.all()
    return render(req,"home.html",{'data':data})

def carpage(req):
    data=CarDB.objects.all()
    return render(req,"car.html",{'data':data})

def contactpage(req):
    return render(req,"contact.html")

def blogpage(req):
    return render(req,"blog.html")

def aboutpage(req):
    return  render(req,"about.html")

def savecontact(req):
    if req.method=="POST":
        a=req.POST.get('name')
        b=req.POST.get('email')
        c=req.POST.get('subject')
        d=req.POST.get('message')
    obj=ContactDB(name=a,email=b,subject=c,message=d)
    obj.save()
    return redirect(contactpage)

def carfilter(req,CarName):
    data=CarDB.objects.filter(brand=CarName)
    return render(req,"carfilter.html",{'data': data})


def singlecar(req,Cid):
    data=CarDB.objects.get(id=Cid)


    return render(req,"singlecar.html", {'data':data})


def cartpage(req):
    return render(req,"cart.html")
