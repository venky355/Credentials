from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_home, name='main_home'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.logout_view, name='logout'),
    path('category/', views.category_list, name='category_list'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
    path('category/add/', views.add_category, name='add_category'),
    path('category/update/<int:category_id>/', views.update_category, name='update_category'),
    path('category/delete/<int:category_id>/', views.delete_category, name='delete_category'),
    path('user/home/', views.user_home, name='user_home'),
    path('user/change-password/', views.change_password, name='change_password'),
    path('user/update-details/', views.update_user_details, name='update_user_details'),
    path('product/', views.product_list, name='product_list'),
    path('product/add/', views.add_product, name='add_product'),
    path('product/update/<int:product_id>/', views.update_product, name='update_product'),
    path('product/delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('product/search/', views.product_search, name='product_search'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('wishlist/add/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:wishlist_item_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
]