from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render
from django.db.models import Q
from apps.models import *
from apps.forms import *

# Create your views here.

def home(request):
    return render (request, 'apps/home.html')

def books(request):
    return render (request, 'students/books.html')

def construction(request):
    return render (request, 'apps/underCon.html')

def dilosh(request):
    return render (request, 'students/dilosh.html')

@login_required
def profile(request):
    return render(request, 'apps/profile.html')

def signup(request):
    form = SignUpForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            #messages.success("yay")
            # return redirect('home')
            return redirect('extraInfo')

    return render(request, 'apps/signup.html', {'form': form})

user_form_types = {
    'student': StudentForm,
    'secretary': SecretaryForm,
    'publisher': PublisherForm,
    'eprovider': EproviderForm,
    'delivery': DeliveryForm,
}

@login_required
def extraInfo(request):
    user_form = user_form_types.get(request.user.user_type)
    form = user_form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            extra = form.save(commit=False)
            extra.user = request.user
            extra.save()
            return redirect('home')
    return render(request, 'apps/extraInfo.html', {'form': form})


def search(request):
    query = request.GET.get("q")
    if query:
        queryset_list1 = CourseBook.objects.all()
        queryset_list2 = Publisher.objects.all()
        queryset_list3 = Delivery.objects.all()


        queryset_list1 = queryset_list1.filter(Q(title__icontains=query)|Q(authors__icontains=query)|Q(ISBN__icontains=query)|Q(publisher__name=query)).distinct()
        #queryset_list1 contains titles
        queryset_list2 = queryset_list2.filter(Q(user__first_name=query)|Q(user__last_name=query)|Q(trn__icontains=query)|Q(ssn__icontains=query)|Q(house__name=query)).distinct()
        #queryset_list2 contains publishers
        queryset_list3 = queryset_list3.filter(Q(user__first_name=query)|Q(user__last_name=query)|Q(d_name__icontains=query)|Q(postal_code__icontains=query)|Q(postal_code__icontains=query)|Q(phone_number__icontains=query)).distinct()
        #queryset_list3 contains deliveries
        queryset_list= queryset_list1 or queryset_list2 or queryset_list3
        return render(request, 'apps/search.html', {'results':queryset_list, 'requested':query, 'len':len(queryset_list)})
