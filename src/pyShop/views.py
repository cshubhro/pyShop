from django.http import HttpResponse
from django.shortcuts import render

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
    context = {
        "title" : "contactPage",
        "uhuh" : "becuz life",
    }
    if request.method == "POST":
        print(request.POST)

    return render(request, "contact/view.html", context)