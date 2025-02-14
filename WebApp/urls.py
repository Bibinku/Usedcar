from django.urls import path
from WebApp import views

urlpatterns=[
    path('',views.homepage,name="homepage"),
    path('carpage/',views.carpage,name="carpage"),
    path('contactpage/',views.contactpage,name="contactpage"),
    path('blogpage/',views.blogpage,name="blogpage"),
    path('aboutpage/',views.aboutpage,name="aboutpage"),
    path('savecontact/',views.savecontact,name="savecontact"),
    path('carfilter/<CarName>/',views.carfilter,name="carfilter"),
    path('singlecar/<int:Cid>/',views.singlecar,name="singlecar"),
    path('cartpage/',views.cartpage,name="cartpage"),
]