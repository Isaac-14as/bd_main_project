from django import forms
from .services import JobService

class AddJobTitle(forms.Form):
    job_title_name = forms.CharField(label='Должность', widget=forms.TextInput(attrs={'class': 'form-control'}))
    salary = forms.DecimalField(label='Заработная плата', widget=forms.TextInput(attrs={'class': 'form-control'}))


class AddHotelRoom(forms.Form):
    hotel_room_name = forms.CharField(label='Номер', widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = forms.DecimalField(label='Цена за сутки', widget=forms.TextInput(attrs={'class': 'form-control'}))


class AddTrack(forms.Form):
    track_name = forms.CharField(label='Название трассы', widget=forms.TextInput(attrs={'class': 'form-control'}))
    difficulty_level = forms.IntegerField(label='Уровень сложности', widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = forms.DecimalField(label='Цена', widget=forms.TextInput(attrs={'class': 'form-control'}))

class AddEmployee(forms.Form):
    bd = JobService()
    JOB_TITLE_LIST = bd.get_id('job_title')
    employee_name = forms.CharField(label='Имя сотрудника', widget=forms.TextInput(attrs={'class': 'form-control'}))
    id_job_title = forms.ChoiceField(label='Должность', choices=JOB_TITLE_LIST)


class AddUser(forms.Form):
    bd = JobService()
    HOTEL_ROOM_LIST = bd.get_id('hotel_room')
    user_name = forms.CharField(label='Имя гостя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    id_hotel_room = forms.ChoiceField(label='Номер отеля', choices=HOTEL_ROOM_LIST)


class AddInventory(forms.Form):
    inventory_name = forms.CharField(label='Названия инвентаря', widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = forms.DecimalField(label='Цена аренды', widget=forms.TextInput(attrs={'class': 'form-control'}))


class AddEvent(forms.Form):
    bd = JobService()
    INVENTORY_LIST = bd.get_id('inventory')
    EMPLOYEE_LIST = bd.get_id('employee')
    USER_LIST = bd.get_id('user')
    TRACK_LIST = bd.get_id('track')
    id_inventory = forms.ChoiceField(label='Название инвентаря', choices=INVENTORY_LIST)
    id_employee = forms.ChoiceField(label='Имя сотрудника', choices=EMPLOYEE_LIST)
    id_user = forms.ChoiceField(label='Имя пользователя', choices=USER_LIST)
    id_track = forms.ChoiceField(label='Название трассы', choices=TRACK_LIST)