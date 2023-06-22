from django.contrib import admin
from panel.models import (Marks, Models, Articles, Manufacturer)

# Register your models here.
@admin.register(Marks)
class MarkTable(admin.ModelAdmin):
    list_display = ("mark_id", "name")
    fields = ["name"]

@admin.register(Models)
class ModelTable(admin.ModelAdmin):
    list_display = ("model_id", "mark_id", "name")
    fields = ["mark_id", "name"]

@admin.register(Manufacturer)
class ManufacturersTable(admin.ModelAdmin):
    list_display = ("manufacturer_id", "name")
    fields = ["name"]

@admin.register(Articles)
class ArticlesTable(admin.ModelAdmin):
    list_display = ("article_id", "manufacturer_id", "article", "article_clean",
                    "name", "quantity", "stock_status", "price")
    fields = ["manufacturer_id", "article", "article_clean",
                    "name", "quantity", "stock_status", "price"]