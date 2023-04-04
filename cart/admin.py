from django.contrib import admin

# Register your models here.
from cart.models import Cart, CartItem, Order, Profile, Orderitem


class CartItemAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'cart', 'quantity', 'active']


admin.site.register(CartItem, CartItemAdmin)


class CartAdmin(admin.ModelAdmin):
    list_display = ['cart_id', 'date_added']


admin.site.register(Cart, CartAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'total_price','payment_mode','razorpay_order_id','status','tracking_no','created_at','city']


admin.site.register(Order, OrderAdmin)
class OrderitemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product','price','quantity']
admin.site.register(Orderitem, OrderitemAdmin)
admin.site.register(Profile)
