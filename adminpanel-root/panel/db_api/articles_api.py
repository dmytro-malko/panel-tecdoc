from panel.models import Articles


def get_all() -> Articles:
    
    records = Articles.objects.order_by("article_id")
    return records