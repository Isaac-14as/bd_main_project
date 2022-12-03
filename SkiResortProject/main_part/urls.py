from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('print_table/<slug:table>/<int:page_number>/<slug:sorth>', print_table, name='print_table'),
    path('delete/<slug:table>/<int:id>/', delete, name='delete'),
    path('add/<slug:table>/', add, name='add'),
    path('redaction/<slug:table>/<int:id>/', redaction, name='redaction'),


    path('register/', register, name='register'),

    # path('login/', user_login, name='login'),
    # path('logout/', user_logout, name='logout'),

]