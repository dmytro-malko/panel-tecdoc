from django.urls import path

from panel import index_views

from .views import main_page, manufacturers_views, articles_views, cars_views, bots_views, olx_views

urlpatterns = [
    path('', main_page.show, name='main_page'),
    
    path('articles/', articles_views.show, name='articles'),
    path('articles/update/<int:article_id>', articles_views.update, name="article_update"),

    path('cars/', cars_views.show, name='cars'),
    path('cars/mark_delete/<int:mark_id>', cars_views.show, name='mark_delete'),
    path('cars/model_delete/<int:model_id>', cars_views.show, name='model_delete'),
    path('marks/', cars_views.show_marks, name='marks'),
    path('marks/mark_delete/<int:mark_id>', cars_views.delete_mark, name='mark_delete'),
    path('models/', cars_views.show_models, name='models'),
    path('models/model_delete/<int:car_id>', cars_views.delete_model, name='model_delete'),

    path('bots/', bots_views.show, name='bots'),
    path('olx/', olx_views.show, name='olx'),

    path('manufacturers/', manufacturers_views.show, name='manufacturers'),
    path('manufacturer/update/<int:manufacturer_id>', manufacturers_views.update, name="manufacturer_update"),
    path('manufacturer/delete/<int:manufacturer_id>', manufacturers_views.delete, name="manufacturer_delete"),
]
