




from core.models import RefModel
from django.db import models



class OrderCountEnum(models.IntegerChoices):
    
    DONE = 0, 'تحویل داده شده'
    
    PENDING = 1, 'در انتظار تحویل'
    
    REJECT = 2, 'کنسل شده'
    

class OrderCount(RefModel):
    
    class Meta:
        verbose_name_plural='جزيیات سفارش'
    
    menu = models.ForeignKey('menu.Menu', on_delete=models.CASCADE, verbose_name="سفارش", help_text="")
    count = models.IntegerField(verbose_name="تعداد سفارش", help_text="", default=1)
    status = models.IntegerField(choices=OrderCountEnum.choices, verbose_name="وضعیت", default=1, help_text="وضعیت تحویل سفارش")
    orderTime = models.DateTimeField(verbose_name="زمان سفارش", help_text="", auto_now=True)
    order = models.ForeignKey('order.Order', on_delete=models.CASCADE, verbose_name="سفارش", help_text="این جزئیات مربوط به کدام سفارش است")
    

    def __str__(self) -> str:
        return f"{self.menu} - {self.order}"