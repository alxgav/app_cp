from django.contrib.auth.models import User
from uuid import uuid4
from django.db import models

from decimal import Decimal


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    num_order = models.CharField(max_length=255, blank=False, unique=True)
    time_job = models.DecimalField(max_digits=3, decimal_places=2, blank=False)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f'{self.num_order}'

    class Meta:
        verbose_name = 'Number of order'
        verbose_name_plural = 'Number of order'
        db_table = "content\".\"order"


class Work_place(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    id_order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    day_today = models.DateField(blank=False)
    psc = models.IntegerField(blank=False)
    job_time = models.DecimalField(max_digits=3, decimal_places=2, blank=False)
    pre_time = models.PositiveIntegerField(blank=False, default=0)

    @property
    def total(self):
        result = Decimal(((self.psc * self.job_time) + self.pre_time) / 60)
        result = result.quantize(Decimal("1.00"))
        return result

    def __str__(self):
        return f'{self.day_today}'

    class Meta:
        verbose_name = 'Date of the job'
        verbose_name_plural = 'Date of the job'
        db_table = "content\".\"work_place"
