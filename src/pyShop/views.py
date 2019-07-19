from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    context = {
        "uhuh" : "i wanna die"
        "title" : "homePage"
    }
    return render(request, "homePage.html", context)

def aboutPage(request):
    context = {
        "title" : "aboutPage"
        "uhuh" : "y tho ???????"
    }
    return render(request, "homePage.html", context)

def contactPage(request):
    context = {
        "title" : "contactPage"
        "uhuh" : "becuz life"
    }
    return render(request, "homePage.html", context)