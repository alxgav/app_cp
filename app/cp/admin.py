from django.contrib import admin

from cp.models import Order, Work_place



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('num_order', 'time_job', 'notes')


@admin.register(Work_place)
class Work_placeAdmin(admin.ModelAdmin):
    list_display = ('id_order', 'day_today', 'psc', 'pre_time', 'total')
