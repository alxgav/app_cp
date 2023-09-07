from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from cp.models import  Order
from django.shortcuts import redirect

class MaterialList(ListView):
    model = Order
    context_object_name = 'material_list'
    template_name = 'cp/order/material_list.html'
    ordering = ['num_order']
    paginate_by = 10

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['order_list'] = context['order_list']
    #     return context


class MaterialCreate(CreateView):
    model = Order
    context_object_name = 'material_create'
    template_name = 'cp/order/create_material.html'
    fields = ['num_order', 'time_job', 'notes']
    success_url = reverse_lazy('materials')

    def form_valid(self, form):
        
        return super(MaterialCreate, self).form_valid(form)


class MaterialUpdate(UpdateView):
    model = Order
    fields = ['num_order', 'time_job', 'notes']
    template_name = 'cp/order/create_material.html'
    context_object_name = 'materials'
    success_url = reverse_lazy('materials')



def Remove_material_list(request, pk):
    order = Order.objects.get(pk=pk)
    print(pk)
    order.delete()
    return redirect('materials')