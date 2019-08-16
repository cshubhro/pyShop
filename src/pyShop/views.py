from django.http import HttpResponse
from django.shortcuts import render

from .forms import contactForm, loginForm

def homePage(request):
    context = {
        "title" : "homePage",
        "uhuh" : "i wanna die",  
    }
    return render(request, "homePage.html", context)

def aboutPage(request):
    context = {
        "title" : "aboutPage",
        "uhuh" : "y tho ???????",
    }
    return render(request, "homePage.html", context)

def contactPage(request):
    formHello = contactForm(request.POST or None)
    context = {
        "title" : "contactPage",
        "uhuh" : "becuz life",
        "form" : formHello
    }

    if formHello.is_valid():
        print(formHello.cleaned_data)
    return render(request, "contact/view.html", context)

def loginPage(requests):
    form = loginForm(request.POST or None)
    if form.is_valid():
        print (form.cleaned_data)
    return render(request, "auth/login.html", {})

def registerPage(requests):
    form = loginForm(request.POST or None)
    print(request.user.is_authenticated())
    if form.is_valid():
        print (form.cleaned_data)
    return render(request, "auth/register.html", {})