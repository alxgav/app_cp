from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from cp.models import Work_place
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404

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


def Remove_work_list(request, pk):
    order = Work_place.objects.get(pk=pk)
    order.delete()
    return redirect('index')