import pprint
from django.shortcuts import render, get_object_or_404, redirect
from .services import JobService
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .forms import *
from .models import *


def index(request):
    template = "main_part/index.html"
    return render(request, template)



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
        elif table == "user_info":
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
        elif table == "user_info":
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
        elif table == "user_info":
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
        elif table == "user_info":
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

def register(request):
    template = "main_part/register.html"
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            if user.is_staff is False:
                return redirect('register_profile')
            else:
                return redirect('index')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    context = {
        'form': form,
    }
    return render(request, template, context)

def register_profile(request):
    template = "main_part/register_profile.html"
    bd = JobService()
    user_cr = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        form = AddUser(request.POST)
        if form.is_valid():
            m = []
            for i in bd.get_columns_names('user_info')[1::]:
                m.append(request.POST[i])
            id_created = bd.add_record('user_info', m)
            user_info_cr = UserInfo.objects.get(id_user_info=id_created)
            UserInfoUser.objects.create(user_info=user_info_cr, user=user_cr)
            return redirect('index')
    else:
        form = AddUser()
    context = {
        'form': form,
    }
    return render(request, template, context)


def user_login(request):
    template = "main_part/login.html"
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = UserLoginForm()
    context = {
        'form': form,
    }
    return render(request, template, context)


def user_logout(request):
    logout(request)
    return redirect('login')


def editing_profile(request):
    template = "main_part/editing_profile.html"
    bd = JobService()
    prof = UserInfoUser.objects.get(user=request.user)
    if request.method == 'POST':
        form = AddUser(request.POST)
        if form.is_valid():
            m = []
            for i in bd.get_columns_names('user_info')[1::]:
                m.append(request.POST[i])
            bd.redaction_record('user_info', m, prof.user_info.id_user_info)
            return redirect('print_table', 'user_info', 0, 'id_user_info')
    else:
        form = AddUser()
    context = {
        'form': form,
    }
    return render(request, template, context)

def account(request):
    template = "main_part/account.html"
    bd = JobService()
    print(request.user.is_staff)
    if request.user.is_staff is False:
        prof = UserInfoUser.objects.get(user=request.user)
        user_info_a = prof.user_info
        hotel_room_a = bd.get_room_by_id(user_info_a.id_hotel_room.id_hotel_room)
        context = {
            'user_info_a': user_info_a,
            'hotel_room_a': hotel_room_a,
        }
    else:
        context = {
        }
    return render(request, template, context)



# функция для вывода всех таблиц
def print_table(request, table, page_number, sorth):
    template = "main_part/print_table.html"
    search_pattern = request.GET.get('search_pattern')

    # seatch_query = request.GET.get
    if search_pattern is None:
        search_pattern = ""
    print(search_pattern)
    bd = JobService()
    if table not in ['employee', 'user_info', 'event']:
        context = bd.get_table_for_print(table, page_number, sorth, search_pattern)
    elif table == 'employee':
        context = bd.get_table_employee(page_number, sorth, search_pattern)
    elif table == 'user_info':
        context = bd.get_table_user(page_number, sorth, search_pattern)
    elif table == 'event':
        context = bd.get_table_event(page_number, sorth, search_pattern)
    else:
        context = {}
    return render(request, template, context)