from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
import pymysql
from .services import JobService

from .forms import *

def index(request):
    template = "main_part/index.html"
    return render(request, template)


# def job_title(request):
#     template = "main_part/job_title.html"
#     bd = JobService()
#     context = {
#         'job_titles': bd.get_job_title_list(),
#         'table': 'job_title',
#     }
#     return render(request, template, context)


# def add_job_title(request):
#     template = "main_part/add_job_title.html"
#     bd = JobService()
#     if request.method == 'POST':
#         form = AddJobTitle(request.POST)
#         if form.is_valid():
#             bd.add_job_title(request.POST['job_title_name'], request.POST['salary'])
#             return redirect('job_title')
#     else:
#         form = AddJobTitle()
#     context = {
#         'form': form,
#     }
#     return render(request, template, context)

# def hotel_rooms(request):
#     template = "main_part/hotel_rooms.html"
#     bd = JobService()
#     context = {
#         'hotel_rooms': bd.get_hotel_rooms_list(),
#     }
#     return render(request, template, context)


# def trails(request):
#     template = "main_part/trails.html"
#     bd = JobService()
#     context = {
#         'trails': bd.get_trails_list(),
#     }
#     return render(request, template, context)


# def employees(request):
#     template = "main_part/employees.html"
#     bd = JobService()
#     context = {
#         'employees': bd.get_employees_list(),
#     }
#     return render(request, template, context)


# def users(request):
#     template = "main_part/users.html"
#     bd = JobService()
#     context = {
#         'users': bd.get_users_list(),
#     }
#     return render(request, template, context)


# def inventory(request):
#     template = "main_part/inventory.html"
#     bd = JobService()
#     context = {
#         'inventory': bd.get_inventory_list(),
#     }
#     return render(request, template, context)


# def event(request):
#     template = "main_part/event.html"
#     bd = JobService()
#     context = {
#         'event': bd.get_event_list(),
#     }
#     return render(request, template, context)



# функция для вывода всех таблиц
def print_table(request, table):
    template = "main_part/print_table.html"
    bd = JobService()
    context = bd.get_table_for_print(table)
    return render(request, template, context)

# функция работает для всех таблиц
def delete(request, table, id):
    template = "main_part/delete.html"
    bd = JobService()
    if request.method == 'POST':
        bd.delete(table, id)
        return redirect('print_table', table)
    return render(request, template)


# def add(request):
#     template = "main_part/add.html"
#     bd = JobService()
#     if request.method == 'POST':
#         form = AddJobTitle(request.POST)
#         if form.is_valid():
#             bd.add_job_title(str(request.POST['job_title_name']), float(request.POST['salary']))
#             return redirect('job_title')
#     else:
#         form = AddJobTitle()
#     context = {
#         'form': form,
#     }
#     return render(request, template, context)