from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_home, name='main_home'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/update_address/', views.update_address, name='update_address'),
    path('category/', views.category_list, name='category_list'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
    path('category/add/', views.add_category, name='add_category'),
    path('category/<int:category_id>/update/', views.update_category, name='update_category'),
    path('category/<int:category_id>/delete/', views.delete_category, name='delete_category'),
    path('user_home/', views.user_home, name='user_home'),
    path('update_user_details/', views.update_user_details, name='update_user_details'),
    path('change_password/', views.change_password, name='change_password'),
    path('product/list/', views.product_list, name='product_list'),
    path('product/add/', views.add_product, name='add_product'),
    # path('export-to-excel/', views.export_to_excel, name='export_to_excel'),
    # path('import-from-excel/', views.import_from_excel, name='import_from_excel'),
    path('upload-excel/', views.upload_excel, name='upload_excel'),
    path('product/<int:product_id>/update/', views.update_product, name='update_product'),
    path('product/<int:product_id>/delete/', views.delete_product, name='delete_product'),
    path('product/search/', views.product_search, name='product_search'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('wishlist/add/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:wishlist_item_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('cart/', views.view_cart, name='view_cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/update/<int:cart_item_id>/', views.update_cart_item, name='update_cart_item'),
    path('checkout/', views.checkout, name='checkout'),
    path('main_home/', views.main_home, name='main_home'),  
    path('update_address/', views.update_address, name='update_address'),  
    path('pending-products/', views.pending_products, name='pending_products'),
    path('approve-product/<int:product_id>/', views.approve_product, name='approve_product'),
    path('reject-product/<int:product_id>/', views.reject_product, name='reject_product'),
    path('toggle_wishlist/', views.toggle_wishlist, name='toggle_wishlist'),
    # path('update_shipping_address/', views.update_shipping_address, name='update_shipping_address'),
    path('process-payment/', views.process_payment, name='process_payment'),
    path('payment/success/', views.payment_success, name='payment_success'),
    path('wishlist_actions/', views.wishlist_actions, name='wishlist_actions'),
    
]
