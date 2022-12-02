from django.db import models
import pymysql
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver
# class User(AbstractUser):
#     ROLE_LIST = (
#         ('Посетитель', 'Посетитель'),
#         ('Администратор', 'Администратор'),
#     )
#     id_user = models.AutoField(primary_key=True)
#     id_hotel_room = models.ForeignKey('ski_resort.hotel_room', on_delete=models.SET_NULL, null=True)
#     role = models.CharField(max_length=30, verbose_name='Роль', choices=ROLE_LIST, default='Посетитель')
#     class Meta:
#         verbose_name = "Пользователь"
#         verbose_name_plural = "Пользователи"
 
#     def __str__(self):
#         return self.username




# class Profile(models.Model):
#     ROLE_LIST = (
#         ('Посетитель', 'Посетитель'),
#         ('Администратор', 'Администратор'),
#     )
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     id_hotel_room = models.ForeignKey('main_part.hotel_room', on_delete=models.SET_NULL, null=True)
#     role = models.CharField(max_length=30, verbose_name='Роль', choices=ROLE_LIST, default='Посетитель')

#     @receiver(post_save, sender=User)
#     def create_user_profile(sender, instance, created, **kwargs):
#         if created:
#             Profile.objects.create(user=instance)

#     @receiver(post_save, sender=User)
#     def save_user_profile(sender, instance, **kwargs):
#         instance.profile.save()

#     class Meta:
#         verbose_name = "Пользователь"
#         verbose_name_plural = "Пользователи"