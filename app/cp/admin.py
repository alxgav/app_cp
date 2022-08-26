from django.contrib import admin

from .models import Order, Work_place


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('num_order', 'time_job', 'notes')
    search_fields = ('num_order',)


@admin.register(Work_place)
class Work_placeAdmin(admin.ModelAdmin):
    list_display = ('id_order', 'day_today', 'psc', 'pre_time', 'total', 'created_at')
    date_hierarchy = "created_at"
    list_filter = ('user',)
