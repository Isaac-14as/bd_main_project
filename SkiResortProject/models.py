# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


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


class MainPartProfile(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    userinfo = models.OneToOneField('UserInfo', models.DO_NOTHING, db_column='UserInfo_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'main_part_profile'


class MainPartProfileGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    profile_id = models.BigIntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'main_part_profile_groups'


class MainPartProfileUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    profile_id = models.BigIntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'main_part_profile_user_permissions'


class Track(models.Model):
    id_track = models.AutoField(primary_key=True)
    track_name = models.TextField(blank=True, null=True)
    difficulty_level = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'track'


class UserInfo(models.Model):
    id_user_info = models.AutoField(primary_key=True)
    user_info_name = models.TextField(blank=True, null=True)
    id_hotel_room = models.ForeignKey(HotelRoom, models.DO_NOTHING, db_column='id_hotel_room', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_info'
