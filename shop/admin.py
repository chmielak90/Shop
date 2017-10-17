from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Permission
from shop.models import User, Address, Order, Invoice, ShoppingCart, ProductCategory, Product, OrderLine, \
    Payment, ProductAvailability


class ProductCategoryInline(admin.TabularInline):
    model = Product.category.through


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'telephone')


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('zip_code', 'city', 'street', 'house_no', 'flat_no', 'user')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'comments', 'send_address',)


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('order', 'bill_address')


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('user',)


@admin.register(ProductCategory)
class ProductCategoriesAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'parent_category')
    inlines = (ProductCategoryInline, )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'description', 'category_list', 'image')


    def category_list(self, obj):
        return ", ".join([str(t) for t in obj.category.all()])


@admin.register(OrderLine)
class OrderLineAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'order', 'shopping_cart')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('status', 'order', 'date_time')
    exclude = ('date_time',)


@admin.register(ProductAvailability)
class ProductAvailabilityAdmin(admin.ModelAdmin):
    list_display = ('quantity', 'product')

@admin.register(Permission)
class PermisionAdmin(admin.ModelAdmin):
    list_display = ('codename', 'name')

