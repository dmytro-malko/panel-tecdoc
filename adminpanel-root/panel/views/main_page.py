from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render


def show(request):
    if not request.user.is_authenticated:
        return redirect("/login/")
    
    if request.method == "GET":
        return render(
            request=request,
            template_name="panel/index.html"
        )