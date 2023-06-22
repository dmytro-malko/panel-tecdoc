from django.urls import path

from panel import index_views

from .views import main_page, users_views, manufacturers_views, articles_views, cars_views, bots_views, olx_views

urlpatterns = [
    path('', main_page.show, name='main_page'),
    path('users/', users_views.show, name='users'),
    path('manufacturers/', manufacturers_views.show, name='manufacturers'),
    path('articles/', articles_views.show, name='articles'),
    path('cars/', cars_views.show, name='cars'),
    path('bots/', bots_views.show, name='bots'),
    path('olx/', olx_views.show, name='olx'),
    path('manufacturer/update/<int:manufacturer_id>', manufacturers_views.update, name="manufacturer_update"),
    path('manufacturer/delete/<int:manufacturer_id>', manufacturers_views.delete, name="manufacturer_delete"),
]