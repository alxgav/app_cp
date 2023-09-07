from datetime import datetime
from unicodedata import name
from django.views.generic.list import ListView

from django.http import  JsonResponse

from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import SearchForm

from .models import Work_place, Order

from django.core.serializers import serialize
from django.shortcuts import render

from django.core.exceptions import ImproperlyConfigured



def total(data) -> float:
    total = 0
    for item in data:
        total += item.total
    return total

def get_order_time(request):
    order_time = Order.objects.all()

    data = serialize('json', order_time, fields=['time_job'])
    
    return JsonResponse(data, safe=False )




class Index(LoginRequiredMixin, ListView):
    model =  Work_place
    context_object_name = 'work_list'
    template_name = 'cp/index.html'
    ordering = ['day_today']


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['work_list'] = context['work_list'].filter(user=self.request.user)
        
        

        date_select = self.request.GET.get('day') or ''
        if date_select:
            context['work_list'] = context['work_list'].filter(
                day_today__contains=date_select)
        else:
            last_record = context['work_list'].last()
            if last_record  is not None:
                context['work_list'] = context['work_list'].filter(day_today=str(last_record))
                context['last_day'] = last_record

        context['date_select'] = date_select
        context['total_sum'] = total(context['work_list'])
        return context
