from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    context = {
        "title" : "homePage"
    }
    return render(request, "homePage.html", context)

def aboutPage(request):
    context = {
        "title" : "aboutPage"
    }
    return render(request, "homePage.html", context)

def contactPage(request):
    context = {
        "title" : "contactPage"
    }
    return render(request, "homePage.html", context)