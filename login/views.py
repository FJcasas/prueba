from django.shortcuts import render
from .models import registrar
def login(request):
    regis = registrar.objects.all()

    return render(request,'login.html')# Create your views here.
