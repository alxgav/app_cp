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
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['work_list'] = context['work_list'].filter(user=self.request.user)
        context['total_sum'] = total(context['work_list'])
        return context


class WorkListDetail(LoginRequiredMixin, DetailView):
    model =  Work_place
    context_object_name = 'work_detail'
    fields = ['id_order', 'user']
    template_name = 'cp/detail.html'

''' CRUD '''


class WorkListCreate(LoginRequiredMixin, CreateView):
    model = Work_place
    context_object_name = 'work_create'
    template_name = 'cp/create.html'
    fields = ['id_order', 'day_today', 'psc', 'job_time', 'pre_time']
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(WorkListCreate, self).form_valid(form)


class WorkListUpdate(LoginRequiredMixin, UpdateView):
    model = Work_place
    fields = ['id_order', 'day_today', 'psc', 'job_time', 'pre_time']
    template_name = 'cp/create.html'
    context_object_name = 'work_items'
    success_url = reverse_lazy('index')


class WorkListDelete(LoginRequiredMixin, DeleteView):
    model = Work_place
    template_name = 'cp/delete.html'
    context_object_name = 'work_items'
    success_url = reverse_lazy('index')

'''LOGIN'''

class CustomLogin(LoginView):
    template_name = 'cp/auth/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self) -> str:
        return reverse_lazy('index')


class RegisterPage(FormView):
    template_name = 'cp/auth/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')

    def form_valid(self, form) -> HttpResponse:
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')
        return super(RegisterPage, self).get(*args, **kwargs)