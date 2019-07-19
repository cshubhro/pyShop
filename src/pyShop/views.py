from django.http import HttpResponse
from django.shortcuts import render
from .forms import contactForm

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