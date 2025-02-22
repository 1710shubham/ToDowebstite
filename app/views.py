from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def InsertPageView(request):
    return render(request,"app/insert.html")


def InsertData(request):
    #Data come from HTML to View
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    contact = request.POST['contact']

    #creating Object Of Model Class
    #Inserting Data into Table
    newuser = Student.objects.create(Firstname=fname,Lastname=lname,Email=email,Contact=contact)

    #After Insert render on showpage View
    return redirect('showpage')

#show page view
def ShowPage(request):
    #select * from tablename
    #For fetching all the data of the table
    all_data=Student.objects.all()
    return render(request,"app/show.html",{'key1':all_data})


# Edit Page View
def EditPage(request,pk):
    # Featching The Data Of Particular ID
    get_data = Student.objects.get(id=pk)
    return render(request,"app/edit.html",{"key2":get_data})



# Update Data View
def UpdateView(request,pk):
    udata = Student.objects.get(id=pk)
    udata.Firstname = request.POST['fname']
    udata.Lastname = request.POST['lname']
    udata.Email = request.POST['email']
    udata.Contact = request.POST['contact']
    # Query For Update
    udata.save()
    #render to ShowPage
    return redirect('showpage')


# Delete Data View
def DeleteData(request,pk):
    ddata = Student.objects.get(id=pk)
    # Query For Delete
    ddata.delete()
    return redirect('showpage')