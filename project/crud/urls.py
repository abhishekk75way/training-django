from django.urls import path
from .views import home, item_list, item_create, item_update, item_delete, signup


urlpatterns = [
    path('', home, name='home'),
    path('item-list/', item_list, name='item_list'),
    path('item-create/', item_create, name='item_create'),
    path('item-update/<int:pk>/', item_update, name='item_update'),
    path('item-delete/<int:pk>/', item_delete, name='item_delete'),
    path("signup/", signup, name="signup"),
]