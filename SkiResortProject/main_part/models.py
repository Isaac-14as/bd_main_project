# from django.db import models
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import User
from django.db import models


class Employee(models.Model):
    id_employee = models.AutoField(primary_key=True)
    employee_name = models.TextField(blank=True, null=True)
    id_job_title = models.ForeignKey('JobTitle', models.DO_NOTHING, db_column='id_job_title', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'


class Event(models.Model):
    id_event = models.AutoField(primary_key=True)
    id_inventory = models.ForeignKey('Inventory', models.DO_NOTHING, db_column='id_inventory', blank=True, null=True)
    id_employee = models.ForeignKey(Employee, models.DO_NOTHING, db_column='id_employee', blank=True, null=True)
    id_user_info = models.ForeignKey('UserInfo', models.DO_NOTHING, db_column='id_user_info', blank=True, null=True)
    id_track = models.ForeignKey('Track', models.DO_NOTHING, db_column='id_track', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event'


class HotelRoom(models.Model):
    id_hotel_room = models.AutoField(primary_key=True)
    hotel_room_name = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hotel_room'


class Inventory(models.Model):
    id_inventory = models.AutoField(primary_key=True)
    inventory_name = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventory'


class JobTitle(models.Model):
    id_job_title = models.AutoField(primary_key=True)
    job_title_name = models.TextField(blank=True, null=True)
    salary = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_title'


class Track(models.Model):
    id_track = models.AutoField(primary_key=True)
    track_name = models.TextField(blank=True, null=True)
    difficulty_level = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'track'


class UserInfo(models.Model):
    # UserInfo = models.OneToOneField(User, on_delete=models.CASCADE)
    id_user_info = models.AutoField(primary_key=True)
    user_info_name = models.TextField(blank=True, null=True)
    id_hotel_room = models.ForeignKey(HotelRoom, models.DO_NOTHING, db_column='id_hotel_room', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_info'
    
    def __str__(self):
        return self.user_info_name


# class Profile(AbstractUser):
#     pass


class UserInfoUser(models.Model):
        user_info = models.OneToOneField(UserInfo, on_delete=models.CASCADE)
        user = models.OneToOneField(User, on_delete=models.CASCADE)

        #  AUTOFIELD ID (PRIMARY KEY)
        #  ONE TO ONE USER INFO 
        #  ONE TO ONE PROFILE
