from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from cp.models import  Order

class OrderList(ListView):
    model = Order
    context_object_name = 'order_list'
    template_name = 'cp/order/order_list.html'
    ordering = ['num_order']
    paginate_by = 10

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['order_list'] = context['order_list']
    #     return context


class OrderCreate(CreateView):
    model = Order
    context_object_name = 'order_create'
    template_name = 'cp/order/create_order.html'
    fields = ['num_order', 'time_job', 'notes']
    success_url = reverse_lazy('orders')

    def form_valid(self, form):
        
        return super(OrderCreate, self).form_valid(form)

    