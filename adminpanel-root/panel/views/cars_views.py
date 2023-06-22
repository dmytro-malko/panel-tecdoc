from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from panel.db_api import cars_api


def show(request):
    if not request.user.is_authenticated:
        return redirect("/login/")
    
    if request.method == "GET":
        marks = cars_api.get_all_marks()
        cars = cars_api.get_all_cars()
        return render(
            request=request,
            template_name="cars/cars.html",
            context={
            "cars" : cars,
            "marks" : marks,
            }
        )
    
    if request.method == "POST":

        print(request.POST)

        if 'mark_name' in request.POST:

            cars_api.create_mark(request.POST['mark_name'])
            return redirect("/cars/")
        
        if 'model_name' in request.POST:

            mark_id = request.POST['mark_id']
            model_name = request.POST['model_name']

            cars_api.create_model(mark_id, model_name)
            return redirect("/cars/")
        
def show_marks(request):
    if not request.user.is_authenticated:
        return redirect("/login/")
    
    if request.method == "GET":
        marks = cars_api.get_all_marks()
        return render(
            request=request,
            template_name="cars/marks.html",
            context={
            "marks" : marks,
            }
        )
    
    if request.method == "POST":

        cars_api.create_mark(request.POST['mark_name'])
        return redirect("/marks/")
    
def delete_mark(request, mark_id: int):
    if not request.user.is_authenticated:
        return redirect("/login/")
    
    if request.method != "GET":
        return

    cars_api.delete_mark(
        mark_id
    )
    return redirect(f"/marks/")


def show_models(request):
    if not request.user.is_authenticated:
        return redirect("/login/")
    
    if request.method == "GET":
        marks = cars_api.get_all_marks()
        models = cars_api.get_all_cars()
        return render(
            request=request,
            template_name="cars/models.html",
            context={
            "marks" : marks,
            "models" : models,
            }
        )
    
    if request.method == "POST":
        mark = request.POST['mark_name']
        model = request.POST['model_name']

        cars_api.create_model(mark, model)
        return redirect("/models/")
    
def delete_model(request, car_id: int):
    if not request.user.is_authenticated:
        return redirect("/login/")
    
    if request.method != "GET":
        return

    cars_api.delete_model(
        car_id
    )
    return redirect(f"/models/")