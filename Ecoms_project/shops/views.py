from django.http import  JsonResponse
from django.shortcuts import redirect, render
# from shop.form import CustomUserForm
from . models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
import json
 
 
def home(request):
#   products=Product.objects.filter(trending=1)
  return render(request,"shop/index.html") #,{"products":products}

def register(request):
#   products=Product.objects.filter(trending=1)
  return render(request,"shop/register.html") #,{"products":products}