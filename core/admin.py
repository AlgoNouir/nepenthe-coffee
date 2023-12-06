





from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from models.person.models import Person
from models.menu.models import Menu
from models.orderCount.models import OrderCount
from models.order.models import Order



@admin.register(Person)
class PersonPanel(admin.ModelAdmin):
    list_display = ['pk', "name"]

@admin.register(Menu)
class MenuPanel(admin.ModelAdmin):
    list_display = ['pk', "name", "orderCount"]



@admin.action(description="تماما پرداخت کارتخوان این سفارشات")
def pay_orders(modeladmin, request, queryset):
    for order in queryset:
        order.cash = order.orderPrice()
        order.save()

    
@admin.action(description="تماما پرداخت نقدی این سفارشات")
def cash_orders(modeladmin, request, queryset):
    for order in queryset:
        order.cash = order.orderPrice()
        order.save()

class OrderCountPanel(admin.StackedInline):
    list_display = ['pk', 'status', 'orderTime']
    model = OrderCount

@admin.register(Order)
class OrderPanel(admin.ModelAdmin):
    list_display = ['pk', "person", "orderPrice"]
    inlines = [OrderCountPanel]
    list_filter = ["created_at"]
    search_fields = ["person__name"]
    actions = [cash_orders, pay_orders]
    