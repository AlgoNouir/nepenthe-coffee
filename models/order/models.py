


from django.db.models import Sum
from datetime import datetime, timedelta
from django.contrib import admin
from core.models import RefModel
from django.db import models
from django.core.validators import MinValueValidator

from models.orderCount.models import OrderCount



class Order(RefModel):
    
    class Meta:
        verbose_name_plural='سفارش'
    
    person = models.ForeignKey('person.Person', on_delete=models.CASCADE, verbose_name="فرد سفارش دهنده", help_text="فردی که سفارش داده است")
    cash = models.IntegerField(verbose_name="پرداختی نقدی", default=0, help_text="پرداخت نقدی فرد برای سفارشات", validators=[MinValueValidator(0)])
    pay = models.IntegerField(verbose_name="پرداخت کارتخوان", default=0, help_text="پرداختی کارتخوان برای این کاربر", validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"سفارش {self.person}"

    @admin.display(description="مبلغ باقی مانده")
    def orderPrice(self):
        orders = OrderCount.objects.filter(order_id=self.pk)
        price = orders.aggregate(Sum("menu__price"))["menu__price__sum"]
        return price - self.cash - self.pay
    