


from django.contrib import admin
from core.models import RefModel
from django.db import models
from models.orderCount.models import OrderCount
from datetime import datetime, timedelta



class Menu(RefModel):
    
    class Meta:
        verbose_name_plural='منوی کافه'
    
    name = models.CharField(max_length=100, verbose_name="نام سفارش", help_text="")
    price = models.IntegerField(verbose_name="قیمت محصول", help_text="")
    
    @admin.display(description="تعداد سفارش امروز")
    def orderCount(self):
        return OrderCount.objects.filter(menu_id=self.pk, orderTime__date__gte=(datetime.now() - timedelta(days=1))).count()
    
    def __str__(self) -> str:
        return self.name