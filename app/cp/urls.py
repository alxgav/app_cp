from django.urls import path

from .views import  get_order_time,  Index
from cp.view.order_view import OrderList
from cp.view.order_view import OrderCreate
from cp.view.login_view import CustomLogin, RegisterPage
from cp.view.work_list import WorkListCreate, WorkListUpdate, WorkListDelete , Remove_work_list

from django.contrib.auth.views import LogoutView
from django.contrib import admin


urlpatterns = [
    
    path('', Index.as_view(), name='index'),
    path('order_time/', get_order_time, name='order_time'),
    path('work_list_create/', WorkListCreate.as_view(), name='work_list_create'),
    path('work_list_edit/<str:pk>/', WorkListUpdate.as_view(), name='work_list_edit'),
    path('work_list_delete/<str:pk>/', WorkListDelete.as_view(), name='work_list_delete'),
    path('remove/<str:pk>/', Remove_work_list, name='remove'),
    path('login/', CustomLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page = 'login'), name='work_list_logout'),
    path('register/', RegisterPage.as_view(), name='work_list_register'),
    path('orders/', OrderList.as_view(), name='orders'),
    path('orders_create/', OrderCreate.as_view(), name='orders_create'),
    
]
