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
    formHello = contactForm
    context = {
        "title" : "contactPage",
        "uhuh" : "becuz life",
        "form" : formHello
    }
    if request.method == "POST":
        print(request.POST.get('fullname'))
        print(request.POST.get('email'))
        print(request.POST.get('content'))

    return render(request, "contact/view.html", context)