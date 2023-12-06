from django.db import models


class RefModel(models.Model):
    created_at = models.DateTimeField(
        auto_now=True, editable=False, verbose_name="تاریخ ایجاد"
    )

    class Meta:
        abstract = True
