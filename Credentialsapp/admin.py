from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from .models import Product, Wishlist

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_superuser'),
        }),
    )
    list_display = ('username', 'email', 'is_staff')
    search_fields = ('username', 'email')
    ordering = ('username',)

admin.site.register(User, UserAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'quantity', 'price', 'parent')
    list_filter = ('country',)
    search_fields = ('name', 'country')
    raw_id_fields = ('parent',)

admin.site.register(Product, ProductAdmin)

class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity')
    list_filter = ('user',)
    search_fields = ('user__username', 'product__name')

admin.site.register(Wishlist, WishlistAdmin)
