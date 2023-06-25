from panel.models import Articles


def create(manufacturer_id: int, article: str, name: str) -> Articles:

    article_clean = ''.join(char for char in article if char.isalnum())

    last_recodr = Articles.objects.last()
    number = str(int(last_recodr.number.strip('AS'))+1)
    full_number = 'AS'+str((7-len(number))*'0')+number
    print(full_number)

    record = Articles(manufacturer_id=manufacturer_id,
                      number=full_number, 
                      article=article, 
                      article_clean=article_clean, 
                      name=name)
    record.save()

    return record

def get_all() -> Articles:
    
    records = Articles.objects.order_by("article_id")
    return records

def get(article_id: int) -> Articles:

    try:
        record = Articles.objects.get(article_id=article_id)
    except Articles.DoesNotExist:
        return
    
    return record