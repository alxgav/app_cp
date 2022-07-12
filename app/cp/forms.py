from django import forms
from .models import Order, Work_place


# class OrderForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = ("num_order",
#                   'time_job',
#                   'notes')


class OrderForm(forms.ModelForm):
    class Meta:
        model = Work_place
        fields = (
            "id_order",
            'day_today',
            'psc',
            'job_time',
            'pre_time',
        )
