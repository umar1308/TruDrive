from django.shortcuts import render,get_object_or_404
from .forms import booklocation
from .models import operators
import pyrebase

config={
    "apiKey": "AIzaSyCpC0GJDfTsOvkL92LfObIqBnbEgpe6cUQ",
    "authDomain": "hackthon-project-fc739.firebaseapp.com",
    "database":"https://hackthon-project-fc739-default-rtdb.firebaseio.com/",
    "projectId": "hackthon-project-fc739",
    "storageBucket": "hackthon-project-fc739.appspot.com",
    "messagingSenderId": "112040387457",
    "appId": "1:112040387457:web:19285b1c351c6d6619be80"
}


# Create your views here.

def index(request):
    return render(request,'app1/index.html')

def booking(request):
    if request.method=="POST":
        f=booklocation(request.POST)
        if f.is_valid():
            name=f.cleaned_data['Name']
            location=f.cleaned_data['location']
            type=f.cleaned_data['type']
            people = operators.objects.all()
            return render(request,'app1/operatorlist.html',{'name':name,'location':location,'type':type,'people': people})
    else:
        f=booklocation();
    return render(request,'app1/book.html',{'f':f})

def operatorlist(request):
    return render(request,"app1/operatorlist.html")

def person_detail(request, id):
    person = get_object_or_404(operators, id=id)
    return render(request, 'app1/person_detail.html', {'person': person})
