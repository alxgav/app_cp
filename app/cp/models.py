from pyexpat import model
from turtle import mode
from uuid import uuid4
from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    num_order = models.CharField(max_length=255, blank=False)
    time_job = models.DecimalField(max_digits=3, decimal_places=2, blank=False)
    notes = models.TextField(blank=False)

    def __str__(self):
        return f'{self.num_order}' 

    class Meta:
        verbose_name = 'Number of order'
        verbose_name_plural = 'Number of order'


class Work_place(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    id_order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    day_today = models.DateField(blank=False)
    job_time = models.DecimalField(max_digits=3, decimal_places=2, blank=False)
    pre_time = models.IntegerField(blank=False)
    total_time = models.DecimalField(max_digits=3, decimal_places=2, blank=False)

    def __str__(self):
        return f'{self.day_today}' 

    class Meta:
        verbose_name = 'Date of the job'
        verbose_name_plural = 'Date of the job'