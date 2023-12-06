



from core.models import RefModel
from django.db import models



class Person(RefModel):
    
    class Meta:
        verbose_name_plural='افراد'
    
    name = models.CharField(max_length=100, verbose_name="نام فرد", help_text="نام قرد سفارش دهنده")
    

    def __str__(self) -> str:
        return self.name