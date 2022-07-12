from django.urls import path

from .views import  get_order_time,  Index, WorkListDetail, WorkListCreate, WorkListUpdate, WorkListDelete

from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('order_time/', get_order_time, name='order_time'),
    path('work_list_detail/<str:pk>/', WorkListDetail.as_view(), name='work_list_datail'),
    path('work_list_create/', WorkListCreate.as_view(), name='work_list_create'),
    path('work_list_edit/<str:pk>/', WorkListUpdate.as_view(), name='work_list_edit'),
    path('work_list_delete/<str:pk>/', WorkListDelete.as_view(), name='work_list_delete'),
]
