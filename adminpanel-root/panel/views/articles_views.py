from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.contrib import messages

from panel.db_api import articles_api, manufacturers_api, cars_api
from panel.models import Cars_to_Articles, Articles_Images


def show(request):
    if not request.user.is_authenticated:
        return redirect("/login/")
    
    if request.method == "GET":
        manufacturers = manufacturers_api.get_all()

        if request.GET.get("search_article"):
            articles = articles_api.get_by_article(request.GET.get("search_article"))
            return render(
                request=request,
                template_name="articles/info.html",
                context={
                "articles" : articles,
                "manufacturers" : manufacturers,
                }
            )

        articles = articles_api.get_all()
        paginator = Paginator(articles, 50)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(
            request=request,
            template_name="articles/info.html",
            context={
            "articles" : page_obj.object_list,
            "manufacturers" : manufacturers,
            "page_obj": page_obj
            }
        )
    
    if request.method == "POST":
        manufacturer_id = request.POST['manufacturer_id']
        article = request.POST['article']
        name = request.POST['name']
        article_id = articles_api.create(manufacturer_id, article, name)
        if article_id:
            return redirect(f"/articles/update/{article_id}")
        else:
            messages.error(request, 'Такой уже есть')
            return redirect("/articles/")
    
def update(request, article_id: int):
    if not request.user.is_authenticated:
        return redirect("/login/")
    
    if request.method == "POST":
        # articles_api.update(
        #     article_id,
        #     name=request.POST['manufacturer_name']
        # )

        print(request.POST)
        print(article_id)
        if request.POST['delete_file'] == 'true':
            try:
                print(request.FILES['welcome_image'])
            except:
                pass
        return redirect(f"/articles/update/{article_id}")

    if request.method == "GET":
        article = articles_api.get(int(article_id))
        cars = Cars_to_Articles.objects.filter(article_id=article_id).order_by('car_id')
        images = Articles_Images.objects.filter(article_id=article_id)
        marks = cars_api.get_all_marks()

        if not article:
            return redirect("/articles/")

        return render(
            request=request,
            template_name="articles/update.html",
            context={
                "article" : article,
                "cars": cars,
                "marks": marks,
                "images": images
            }
        )
    
def delete(request, article_id: int):
    if not request.user.is_authenticated:
        return redirect("/login/")
    
    if request.method != "GET":
        return

    articles_api.delete(
        article_id
    )
    return redirect(f"/articles/")
