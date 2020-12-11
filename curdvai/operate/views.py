from django.shortcuts import render,HttpResponseRedirect,redirect
from .forms import StudentRegister
from . models import User
# Create your views here.

#this function will show all items
def addshow(request):
    if request.method=='POST':
        fm=StudentRegister(request.POST)

        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']

            res=User(name=nm,email=em,password=pw)
            res.save()
            fm = StudentRegister()


    else:
        fm=StudentRegister()



    stud=User.objects.all()

    return render(request,'operate/addandshow.html',{'form':fm,'stu':stud})

def deletedata(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect("/")
#this function will update and delete

def update_data(request,id):
    if request.method=="POST":
        pi=User.objects.get(pk=id)
        fm=StudentRegister(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()

    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegister(instance=pi)


    return render(request,'operate/updatestudent.html',{'form':fm})
