from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from panel.db_api import manufacturers_api


def show(request):
    if not request.user.is_authenticated:
        return redirect("/login/")
    
    if request.method == "GET":

        if request.GET.get("search_manufacturer"):
            manufacturer = manufacturers_api.get_by_name(request.GET.get("search_manufacturer"))
            return render(
            request=request,
            template_name="manufacturers/manufacturers.html",
            context={
            "manufacturer" : manufacturer
            }
        )

        manufacturers = manufacturers_api.get_all()
        paginator = Paginator(manufacturers, 25)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(
            request=request,
            template_name="manufacturers/manufacturers.html",
            context={
            "manufacturers" : page_obj.object_list,
            "page_obj": page_obj
            }
        )
    
    if request.method == "POST":

        manufacturer_id = request.POST['manufacturerId']
        name = request.POST['manufacturerName']

        manufacturers_api.create(manufacturer_id, name)
        return redirect("/manufacturers/")
    
def update(request, manufacturer_id: int):
    if not request.user.is_authenticated:
        return redirect("/login/")
    
    if request.method == "POST":
        manufacturers_api.update(
            manufacturer_id,
            name=request.POST['manufacturer_name']
        )
        return redirect(f"/manufacturer/update/{manufacturer_id}")

    if request.method == "GET":
        manufacturer = manufacturers_api.get(int(manufacturer_id))
        if not manufacturer:
            return redirect("/manufacturers/")

        return render(
            request=request,
            template_name="manufacturers/update.html",
            context={
                "manufacturer" : manufacturer
            }
        )
    
def delete(request, manufacturer_id: int):
    if not request.user.is_authenticated:
        return redirect("/login/")
    
    if request.method != "GET":
        return

    manufacturers_api.delete(
        manufacturer_id
    )
    return redirect(f"/manufacturers/")