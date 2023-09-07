from django import forms
from .models import Order, Work_place


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ("num_order",
                  'time_job',
                  'notes')


class DateInput(forms.DateInput):
    input_type = 'date'

class WorkForm(forms.ModelForm):
    class Meta:
        model = Work_place
        fields = (
            "id_order",
            'day_today',
            'psc',
            'job_time',
            'pre_time',
        )
        widgets = {
            'dateField': DateInput
        }

class SearchForm(forms.ModelForm):
    class Meta:
        fields = (
            "text",
            "day"
        )
