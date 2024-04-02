from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_home, name='main_home'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.user_login, name='login'),
    path('user_home/', views.user_home, name='user_home'),
    path('dealer_home/', views.dealer_home, name='dealer_home'),
    # path('cr/', views.create_product, name='create_product'),
    path('product_list/', views.product_list, name='product_list'),
    path('update_product/<int:product_id>/', views.update_product, name='update_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('add_to_wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('update_wishlist_item/<int:wishlist_item_id>/', views.update_wishlist_item, name='update_wishlist_item'),
    path('delete_wishlist_item/<int:wishlist_item_id>/', views.delete_wishlist_item, name='delete_wishlist_item'),
]
