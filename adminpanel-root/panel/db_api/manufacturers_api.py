from panel.models import Manufacturer


def create(manufacturer_id: int, name: str) -> Manufacturer:

    record = Manufacturer(manufacturer_id, name)
    record.save()

    return record


def get(manufacturer_id: int) -> Manufacturer:

    try:
        record = Manufacturer.objects.get(manufacturer_id=manufacturer_id)
    except Manufacturer.DoesNotExist:
        return
    
    return record

def get_by_name(name: int) -> Manufacturer:

    try:
        record = Manufacturer.objects.get(name=name)
    except Manufacturer.DoesNotExist:
        return
    
    return record

def delete(manufacturer_id: int):

    record = get(manufacturer_id)
    if not record: return

    record.delete()

def get_total() -> int:

    count = Manufacturer.objects.count()
    return count

def update(
        manufacturer_id: int, name: str
    ) -> Manufacturer:

    manufacturer = get(manufacturer_id)

    if not manufacturer:
        return

    if name != "":
        manufacturer.name = name

    manufacturer.save()

    return manufacturer


def get_all() -> Manufacturer:
    
    records = Manufacturer.objects.order_by("name")
    return records