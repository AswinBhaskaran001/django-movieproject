from django.shortcuts import render
from movie.models import Movie
from movie.forms import Movieform

# Create your views here.
def home(request):
    k=Movie.objects.all()
    return render(request,"home.html",{'b':k})

def addmovie(request):
    if(request.method=="POST"):
        n=request.POST['n']
        d=request.POST['d']
        y=request.POST['y']
        i=request.FILES['i']
        b=Movie.objects.create(name=n,desc=d,year=y,img=i)
        b.save
        return home(request)
    return render(request,"addmovie.html")

def moviedetail(request,p):
    b=Movie.objects.get(id=p)
    return render(request,"moviedetail.html",{'b':b})


def moviedelete(request,p):
    b=Movie.objects.get(id=p)
    b.delete()
    return home(request)

def movieedit(request,p):
    b=Movie.objects.get(id=p)
    if(request.method=="POST"):
        form=Movieform(request.POST,request.FILES,instance=b)
        if form.is_valid():
            form.save()
        return home(request)
    form=Movieform(instance=b)
    return render(request,"edit.html",{'form':form})



