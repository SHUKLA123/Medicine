from django.shortcuts import render,redirect
from testapp.forms import SignUpForm
from django.http import HttpResponseRedirect
from testapp.models import Sell1
from testapp.forms import Sell1Form
from django.http import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from testapp.models import Buy1
from testapp.forms import Buy1Form
from django.db.models import F, FloatField, Sum
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from testapp.models import Upload_Prescription
from testapp.forms import Upload_pdf
# Create your views here.

def display(request):
    return render(request,'index.html')

def contact_us(request):
    return render(request,'contactus.html')

def upload(request):
    return render(request,'search1.html')

@login_required
def loginpage(request):
    return render(request,'loginpage.html')

def Searchbar_view(request):
    form=Sell1Form()
    if request.method =='POST':
        medicine = request.POST.get("Medicine")
        email = request.POST.get("Email")
        price = request.POST.get("Total_Amount")
        loc = request.POST.get("Location")
        pincode = request.POST.get("Pincode")
        form=Sell1Form(request.POST)
        message = "Hello Man , \n"+"\tYour Contact Information : \n"+"Your medicine name : "+medicine+".\n"+"Your amount is "+price+".\n"+"Your current register location is : "+ loc + ".\n"+"Your pincode is"+pincode+".\n"+"If you have any query contact us on  --->>> 8571909652"
        if form.is_valid():
            form.save(commit=True)
        if message and email:
            send_mail('Confermation Recipt',message,'abcdef7700000000@gmail.com',[email],fail_silently=False)
        return display(request)

    return render(request,'search.html',{'form':form})

def search(request):
    if request.method == 'POST':
        srch = request.POST['srh']

        if srch:
            match = Buy1.objects.filter(Q(Medicine__icontains=srch))

            if match:
                e = Buy1.objects.get(Medicine=srch)
                a = e.price
                return render(request, 'show.html', {'sr':match,'a':a})

            else:
                messages.error(request,'no result found')
        else:
            return HttpResponseRedirect('/search/')
    return render(request, 'search1.html')

def Buy_view(request):
    form=Buy1Form()
    if request.method =='POST':
        form=Buy1Form(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return display(request)
    return render(request,'input_medicine.html',{'form':form})

def upload_view(request):
    form = Upload_pdf()
    if request.method == "POST":
        form = Upload_pdf(request.POST , request.FILES)
        if form.is_valid:
            form.save()
            return redirect('upload')
    return render(request, 'upload.html',{'form':form})

def show(request):
    return render(request,'show.html')

def profile_view(request):
    return render(request,'profile-page.html')

def term_view(request):
    return render(request,'termandpolicy.html')

# signup process
def signup_view(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'signup.html',{'form':form})

def logout_view(request):
    return render(request,'customlogout.html')

# Alag hai taki vo log apne app se kar sake

class Buy1ListView(ListView):
    model=Buy1

class Buy1DetailView(DetailView):
    model=Buy1

class Buy1CreateView(CreateView):
    model=Buy1
    #fields=('name','taste','color','price')
    fields='__all__'
class Buy1UpdateView(UpdateView):
    model=Buy1
    fields=('Medicine','Company_Name','Number_of_Tablet','price','quantity')
class Buy1DeleteView(DeleteView):
    model=Buy1
    success_url=reverse_lazy('crud')
