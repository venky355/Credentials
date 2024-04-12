from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_home, name='main_home'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.logout_view, name='logout'),
    path('category_list/', views.category_list, name='category_list'),
    path('category_detail/<int:category_id>/', views.category_detail, name='category_detail'),
    path('add_category/', views.add_category, name='add_category'),
    path('update_category/<int:category_id>/', views.update_category, name='update_category'),
    path('delete_category/<int:category_id>/', views.delete_category, name='delete_category'),
    path('user_home/', views.user_home, name='user_home'),
    path('change_password/', views.change_password, name='change_password'),
    path('update_user_details/', views.update_user_details, name='update_user_details'),
    path('product_list/', views.product_list, name='product_list'),
    path('add_product/', views.add_product, name='add_product'),
    path('update_product/<int:product_id>/', views.update_product, name='update_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('add_to_wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove_from_wishlist/<int:wishlist_item_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('product_search/', views.product_search, name='product_search'),
]
