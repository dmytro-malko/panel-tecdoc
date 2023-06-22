from panel.models import MarksModels, Marks
from django.db import connection

# def dictfetchall(cursor):
#     "Return all rows from a cursor as a dict"
#     columns = [col[0] for col in cursor.description]
#     return [
#         dict(zip(columns, row))
#         for row in cursor.fetchall()
#     ]

def get_model(car_id: int) -> MarksModels:

    try:
        record = MarksModels.objects.get(car_id=car_id)
    except MarksModels.DoesNotExist:
        return
    
    return record

def get_mark(mark_id: int) -> Marks:

    try:
        record = Marks.objects.get(mark_id=mark_id)
    except Marks.DoesNotExist:
        return
    
    return record

def get_all_cars():
    records = MarksModels.objects.order_by("mark")
    return records

def get_all_marks()-> Marks:
    
    records = Marks.objects.order_by("name")
    return records

def create_mark(name: str) -> Marks:

    record = Marks(name=name)
    record.save()

    return record

def create_model(mark: str, model: str) -> MarksModels:

    record = MarksModels(mark=mark, model=model)
    record.save()

    return record

def delete_mark(mark_id: int):

    record = get_mark(mark_id)
    if not record: return
    cars = MarksModels.objects.filter(mark=record.name)
    for car in cars:
        delete_model(car.car_id)
    record.delete()

def delete_model(car_id: int):

    record = get_model(car_id)
    if not record: return

    record.delete()