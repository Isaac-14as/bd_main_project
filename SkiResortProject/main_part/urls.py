from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    # path('job_title/', job_title, name='job_title'),
    # path('hotel_rooms/', hotel_rooms, name='hotel_rooms'),
    # path('trails/', trails, name='trails'),
    # path('employees/', employees, name='employees'),
    # path('users/', users, name='users'),
    # path('inventory/', inventory, name='inventory'),
    # path('event/', event, name='event'),


    # path('add_job_title/', add_job_title, name='add_job_title'),

    # path('add_hotel_rooms', add_hotel_rooms, name='add_hotel_rooms'),
    # path('add_trails', add_trails, name='add_trails'),
    # path('add_employees', add_employees, name='add_employees'),
    # path('add_users', add_users, name='add_users'),
    # path('add_inventory', add_inventory, name='add_inventory'),
    # path('add_event', add_event, name='add_event'),


    path('print_table/<slug:table>/<int:page_number>', print_table, name='print_table'),
    path('delete/<slug:table>/<int:id>/', delete, name='delete'),
    path('add/<slug:table>/', add, name='add'),
    path('redaction/<slug:table>/<int:id>/', redaction, name='redaction'),

]