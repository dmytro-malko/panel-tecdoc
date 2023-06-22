from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render


def show(request):
    if not request.user.is_authenticated:
        return redirect("/login/")
    
    pass