from django.shortcuts import render,redirect
from CarApp.models import CarDB,BrandDB,SpecificationsDB,FeatureDB
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from WebApp.models import ContactDB
from django.contrib import messages




# Create your views here.
def indexpage(req):
    return render(req,"index.html")
def cardetails(req):
    cat=BrandDB.objects.all()
    return render(req,"Cardetails.html",{'cat':cat})
def savecar(req):
    if req.method=="POST":
        a=req.POST.get('name')
        b=req.POST.get('brand')
        c=req.POST.get('model')
        img=req.FILES['image']
        d=req.POST.get('price')
        e=req.POST.get('gst')
        f=req.POST.get('insurance')
        obj=CarDB(name=a,brand=b,model=c,image=img,price=d,gst=e,insurance=f)
        obj.save()
        messages.success(req,"Details Add successfully")
        return redirect(indexpage)
def displaycar(req):
    data=CarDB.objects.all()
    return render(req,"displaycar.html",{'data':data})
def editcar(req,Cid):
    data=CarDB.objects.get(id=Cid)
    return render(req,"editcar.html",{'data':data})

def updatecar(req,Cid):
    if req.method=="POST":
        a=req.POST.get('name')
        b=req.POST.get('brand')
        c=req.POST.get('price')
        d=req.POST.get('model')
        e = req.POST.get('gst')
        f = req.POST.get('insurance')
        try:
           img=req.FILES['image']
           fs=FileSystemStorage()
           file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=CarDB.objects.get(id=Cid).image

    CarDB.objects.filter(id=Cid).update(name=a,brand=b,price=c,image=file,model=d,gst=e,insurance=f)
    return redirect(displaycar)
def deletecar(req,Cid):
    data=CarDB.objects.filter(id=Cid)
    data.delete()
    messages.warning(req,"Cardetails Deleted Successfully")
    return redirect(displaycar)
def Adminlogin(req):
    return render(req,"Adminlogin.html")

def loginin(request):
    if request.method=="POST":
        a=request.POST.get('username')
        b=request.POST.get('pass')
        if User.objects.filter(username__contains=a).exists():
            x=authenticate(username=a,password=b)
            if x is not None:
                login(request,x)
                request.session['username']=a
                request.session['password']=b
                messages.success(request,"Login Successfully")
                return redirect(indexpage)
            else:
                messages.warning(request,"Invaild password or username")
                return redirect(Adminlogin)
        else:
            messages.warning(request,"Invaild password or username")
            return redirect(Adminlogin)

def adminlogout(req):
    del req.session['username']
    del req.session['password']
    messages.success(req,"Logout Successfully")
    return redirect(Adminlogin)

def brandpage(req):
    cat=CarDB.objects.all()
    return render(req,"brand.html",{'cat':cat})

def savebrand(req):
    if req.method=="POST":
        a=req.POST.get('bbrand')


        img=req.FILES['bimage']
        b=req.POST.get('bdescription')
        obj=BrandDB(bbrand=a,bimage=img,bdescription=b)
        obj.save()

        return redirect(indexpage)

def displaybrand(req):
    data=BrandDB.objects.all()
    return render(req,"displaybrand.html", {'data':data})

def editbrand(req,Cid):
    data=BrandDB.objects.get(id=Cid)
    cat=CarDB.objects.all()
    return render(req,"Editbrand.html",{'data':data,'cat':cat})

def deletebrand(req,Cid):
    data=BrandDB.objects.filter(id=Cid)
    data.delete()
    return redirect(displaybrand)

def updatebrand(req,Cid):
    if req.method=="POST":
        a = req.POST.get('bbrand')

        b = req.POST.get('bdescription')


        try:
           img=req.FILES['bimage']
           fs=FileSystemStorage()
           file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=BrandDB.objects.get(id=Cid).pimage

    BrandDB.objects.filter(id=Cid).update(bbrand=a,bdescription=b,bimage=file)
    return redirect(displaybrand)

def displaycontact(req):
    data=ContactDB.objects.all()
    return render(req,"displaycontact.html", {'data':data})

def deletecontact(req,CONid):
    data=ContactDB.objects.filter(id=CONid)
    data.delete()
    return redirect(displaycontact)

def specification(req):
    data=SpecificationsDB.objects.all()
    return render(req,"addspecification.html",{'data':data})


def savespecification(req):
    if req.method=="POST":

        b=req.POST.get('option1')
        c=req.POST.get('option2')

        d=req.POST.get('option3')
        e=req.POST.get('option4')
        f=req.POST.get('option5')
        obj=SpecificationsDB(option1=b,option2=c,option3=d,option4=e,option5=f)
        obj.save()
        messages.success(req,"Details Add successfully")
        return redirect(indexpage)

def displayspecification(req):
    data=SpecificationsDB.objects.all()
    return render(req,"displayspecification.html", {'data':data})



def editspecification(req,Sid):
    data=SpecificationsDB.objects.get(id=Sid)
    return render(req,"editspecification.html",{'data':data})

def updatespecification(req,Sid):
    if req.method=="POST":

        b = req.POST.get('option1')
        c = req.POST.get('option2')

        d = req.POST.get('option3')
        e = req.POST.get('option4')
        f = req.POST.get('option5')


    SpecificationsDB.objects.filter(id=Sid).update(option1=b,option2=c,option3=d,option4=e,option5=f)
    return redirect(displayspecification)
def deletespecification(req,Sid):
    data=SpecificationsDB.objects.filter(id=Sid)
    data.delete()
    messages.warning(req,"Specification details Deleted Successfully")
    return redirect(displayspecification)


def features(req):
    data=FeatureDB.objects.all()
    return render(req,"addfeature.html",{'data':data})


def savefeatures(req):
    if req.method=="POST":
        a = req.POST.get('features')
        b=req.POST.get('Option1')
        c=req.POST.get('Option2')

        d=req.POST.get('Option3')
        e=req.POST.get('Option4')
        f=req.POST.get('Option5')
        obj=FeatureDB(features=a,Option1=b,Option2=c,Option3=d,Option4=e,Option5=f)
        obj.save()
        messages.success(req,"Details Add successfully")
        return redirect(indexpage)

def displayfeatures(req):
    data=FeatureDB.objects.all()
    return render(req,"displayfeature.html", {'data':data})



def editfeatures(req,Fid):
    data=FeatureDB.objects.get(id=Fid)
    return render(req,"editfeature.html",{'data':data})

def updatefeatures(req,Fid):
    if req.method=="POST":
        a = req.POST.get('features')
        b = req.POST.get('Option1')
        c = req.POST.get('Option2')

        d = req.POST.get('Option3')
        e = req.POST.get('Option4')
        f = req.POST.get('Option5')

    FeatureDB.objects.filter(id=Fid).update(features=a,Option1=b,Option2=c,Option3=d,Option4=e,Option5=f)
    return redirect(displayfeatures)
def deletefeatures(req,Fid):
    data=FeatureDB.objects.filter(id=Fid)
    data.delete()
    messages.warning(req,"Specification details Deleted Successfully")
    return redirect(displayfeatures)
