from django.shortcuts import render, get_object_or_404, redirect
from .services import JobService

from .forms import *

def index(request):
    template = "main_part/index.html"
    return render(request, template)



# функция для вывода всех таблиц
def print_table(request, table, page_number, sorth):
    template = "main_part/print_table.html"
    bd = JobService()
    if table not in ['employee', 'user', 'event']:
        context = bd.get_table_for_print(table, page_number, sorth)
    elif table == 'employee':
        context = bd.get_table_employee(page_number, sorth)
    elif table == 'user':
        context = bd.get_table_user(page_number, sorth)
    elif table == 'event':
        context = bd.get_table_event(page_number, sorth)
    else:
        context = {}
    return render(request, template, context)



# функция удаления для всех таблиц (проблема с связанными таблицами)
def delete(request, table, id):
    template = "main_part/delete.html"
    bd = JobService()
    if request.method == 'POST':
        bd.delete(table, id)
        return redirect('print_table', table, 0, 'id_' + str(table))
    return render(request, template)


def add(request, table):
    template = "main_part/add.html"
    bd = JobService()
    if request.method == 'POST':
        if table == "job_title":
            form = AddJobTitle(request.POST)
        elif table == "hotel_room":
            form = AddHotelRoom(request.POST)
        elif table == "track":
            form = AddTrack(request.POST)
        elif table == "employee":
            form = AddEmployee(request.POST)
        elif table == "user":
            form = AddUser(request.POST)
        elif table == "inventory":
            form = AddInventory(request.POST)
        elif table == "event":
            form = AddEvent(request.POST)
            
        if form.is_valid():
            m = []
            for i in bd.get_columns_names(table)[1::]:
                m.append(request.POST[i])
            bd.add_record(table, m)
            return redirect('print_table', table, 0, 'id_' + str(table))
    else:
        if table == "job_title":
            form = AddJobTitle()
        elif table == "hotel_room":
            form = AddHotelRoom()
        elif table == "track":
            form = AddTrack()
        elif table == "employee":
            form = AddEmployee()
        elif table == "user":
            form = AddUser()
        elif table == "inventory":
            form = AddInventory()
        elif table == "event":
            form = AddEvent()
        else:
            form = AddHotelRoom()
    context = {
        'form': form,
    }
    return render(request, template, context)




def redaction(request, table, id):
    template = "main_part/add.html"
    bd = JobService()
    if request.method == 'POST':
        if table == "job_title":
            form = AddJobTitle(request.POST)
        elif table == "hotel_room":
            form = AddHotelRoom(request.POST)
        elif table == "track":
            form = AddTrack(request.POST)
        elif table == "employee":
            form = AddEmployee(request.POST)
        elif table == "user":
            form = AddUser(request.POST)
        elif table == "inventory":
            form = AddInventory(request.POST)
        elif table == "event":
            form = AddEvent(request.POST)
        if form.is_valid():
            m = []
            for i in bd.get_columns_names(table)[1::]:
                m.append(request.POST[i])
            bd.redaction_record(table, m, id)
            return redirect('print_table', table, 0, 'id_' + str(table))
    else:
        if table == "job_title":
            form = AddJobTitle()
        elif table == "hotel_room":
            form = AddHotelRoom()
        elif table == "track":
            form = AddTrack()
        elif table == "employee":
            form = AddEmployee()
        elif table == "user":
            form = AddUser()
        elif table == "inventory":
            form = AddInventory()
        elif table == "event":
            form = AddEvent()
        else:
            form = AddHotelRoom()
    context = {
        'form': form,
    }
    return render(request, template, context)