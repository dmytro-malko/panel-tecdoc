from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from panel.db_api import articles_api

def show(request):
    if not request.user.is_authenticated:
        return redirect("/login/")
    
    if request.method == "GET":

        articles = articles_api.get_all()
        paginator = Paginator(articles, 50)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(
            request=request,
            template_name="articles/info.html",
            context={
            "articles" : page_obj.object_list,
            "page_obj": page_obj
            }
        )