from panel.models import Articles
from django.db.models import Q
import django.db.utils

def create(manufacturer_id: int, article: str, name: str) -> Articles:

    article_clean = ''.join(char for char in article if char.isalnum())

    last_recodr = Articles.objects.last()
    number = str(int(last_recodr.number.strip('AS'))+1)
    article_id = int(last_recodr.article_id)+1
    full_number = 'AS'+str((8-len(number))*'0')+number
    print(full_number)

    record = Articles(article_id=article_id,manufacturer_id=manufacturer_id,
                      number=full_number, 
                      article=article, 
                      article_clean=article_clean, 
                      name=name)
    try:
        record.save()
        return article_id
    except django.db.utils.IntegrityError:
        return False

def get_all() -> Articles:
    
    records = Articles.objects.order_by("article_id")
    return records

def get(article_id: int) -> Articles:

    try:
        record = Articles.objects.get(article_id=article_id)
    except Articles.DoesNotExist:
        return
    
    return record

def get_by_article(article: str) -> Articles:

    query = ''.join(char for char in article if char.isalnum())
    if query[0:2] == 'AS' and len(query) == 10:
        try:
            record = Articles.objects.filter(number=query)
        except Articles.DoesNotExist:
            return
    else:
        try:
            record = Articles.objects.filter(Q(article_clean__icontains=query))
        except Articles.DoesNotExist:
            return
    
    return record

def delete(article_id: int):

    record = get(article_id)
    if not record: return

    record.delete()