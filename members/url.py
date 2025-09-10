
from django.urls import path
from . import views


urlpatterns = [
    path('add_member', views.add_member, name='add_member'),
    path('update_member', views.update_member, name='update_member'),
    path('delete_member', views.delete_member, name='delete_member'),
    path('add_plan', views.add_plan, name='add_plan'),
    path('view_members', views.view_members, name='view_members'),
    path('add_trainer_staff', views.add_trainer_staff, name='add_trainer_staff'),
    path('view_all_trainers_staff', views.view_all_trainers_staff, name='view_all_trainers_staff'),
    path('view_single_trainer_staff/<int:id>', views.view_single_trainer_staff, name='view_single_trainer_staff'),
    path('edit_trainer_staff/<int:id>', views.edit_trainer_staff, name='edit_trainer_staff'),
    path('delete_trainer_staff', views.delete_trainer_staff, name='delete_trainer_staff')


]
