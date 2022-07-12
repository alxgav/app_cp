import json
from datetime import datetime
from django.views.generic.list import ListView

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import OrderForm
from .models import Work_place, Order

from django.core.serializers import serialize

from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView


def total(data) -> float:
    total = 0
    for item in data:
        total += item.total
    return total

def get_order_time(request):
    order_time = Order.objects.all()

    data = serialize('json', order_time, fields=['time_job'])
    
    return JsonResponse(data, safe=False )




class Index(ListView):
    model =  Work_place
    context_object_name = 'work_list'
    template_name = 'cp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_sum'] = total(context['work_list'])
        return context
    


class WorkListDetail(DetailView):
    model =  Work_place
    context_object_name = 'work_detail'
    fields = ['id_order', 'user']
    template_name = 'cp/detail.html'

''' Action with worklist'''

class WorkListCreate(CreateView):
    model = Work_place
    context_object_name = 'work_create'
    template_name = 'cp/create.html'
    fields = '__all__'
    success_url = reverse_lazy('index')


class WorkListUpdate(UpdateView):
    model = Work_place
    fields = '__all__'
    template_name = 'cp/create.html'
    context_object_name = 'work_items'
    success_url = reverse_lazy('index')


class WorkListDelete(DeleteView):
    model = Work_place
    template_name = 'cp/delete.html'
    context_object_name = 'work_items'
    success_url = reverse_lazy('index')