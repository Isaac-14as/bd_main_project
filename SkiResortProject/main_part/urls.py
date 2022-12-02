from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('print_table/<slug:table>/<int:page_number>/', print_table, name='print_table'),
    path('delete/<slug:table>/<int:id>/', delete, name='delete'),
    path('add/<slug:table>/', add, name='add'),
    path('redaction/<slug:table>/<int:id>/', redaction, name='redaction'),

]