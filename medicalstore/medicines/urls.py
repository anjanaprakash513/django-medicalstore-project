from . import views
from django.urls import path

urlpatterns = [
        path('create/',views.product_create,name='createproduct'),
        path('retrieve/',views.product_read,name='retrieveproduct'),
        path('edit/<int:pk>',views.product_update, name='edit'),
        path('delete/<int:pk>',views.product_delete,name='delete'),
    ]