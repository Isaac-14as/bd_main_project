from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('print_table/<slug:table>/<int:page_number>/<slug:sorth>', print_table, name='print_table'),
    path('delete/<slug:table>/<int:id>/', delete, name='delete'),
    path('add/<slug:table>/', add, name='add'),
    path('redaction/<slug:table>/<int:id>/', redaction, name='redaction'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),

    path('register/', register, name='register'),
    path('register_profile/', register_profile, name='register_profile'),
    path('editing_profile/', editing_profile, name='editing_profile'),
    path('account/', account, name='account'),
    # path('login/', user_login, name='login'),
    # path('logout/', user_logout, name='logout'),

]