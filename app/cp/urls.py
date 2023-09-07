from django.urls import path

from .views import  get_order_time,  Index
from cp.view.material_view import MaterialList, MaterialCreate, MaterialUpdate, Remove_material_list
from cp.view.login_view import CustomLogin, RegisterPage
from cp.view.work_list import WorkListCreate, WorkListUpdate, WorkListDelete , Remove_work_list

from django.contrib.auth.views import LogoutView


urlpatterns = [
    
    path('', Index.as_view(), name='index'),
    path('order_time/', get_order_time, name='order_time'),
    path('work_list_create/', WorkListCreate.as_view(), name='work_list_create'),
    path('work_list_edit/<str:pk>/', WorkListUpdate.as_view(), name='work_list_edit'),
    path('remove/<str:pk>/', Remove_work_list, name='remove'),
    path('login/', CustomLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page = 'login'), name='work_list_logout'),
    path('register/', RegisterPage.as_view(), name='work_list_register'),
    path('materials/', MaterialList.as_view(), name='materials'),
    path('material_create/', MaterialCreate.as_view(), name='materials_create'),
    path('material_edit/<str:pk>/', MaterialUpdate.as_view(), name='material_edit'),
    path('remove_material/<str:pk>/', Remove_material_list, name='remove_material'),
    
]
