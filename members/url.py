
from django.urls import path
from . import views


urlpatterns = [
    path('admin_login', views.admin_login, name='admin_login'),
    path('admin_logout', views.admin_logout, name='admin_logout'),
    path('add_member', views.add_member, name='add_member'),
    path('update_member/<int:id>', views.update_member, name='update_member'),   #updated
    path('delete_member/<int:id>', views.delete_member, name='delete_member'),
    path('add_plan', views.add_plan, name='add_plan'),
    path('view_plans', views.view_plans, name='view_plans'),
    path('edit_plan/<int:id>', views.edit_plan, name='edit_plan'),
    path('delete_plan/<int:id>',views.delete_plan, name='delete_plan'),
    path('view_members', views.view_members, name='view_members'),
    path('add_trainer_staff', views.add_trainer_staff, name='add_trainer_staff'),
    path('view_all_trainers_staff', views.view_all_trainers_staff, name='view_all_trainers_staff'),
    path('view_single_trainer_staff/<int:id>', views.view_single_trainer_staff, name='view_single_trainer_staff'),
    path('edit_trainer_staff/<int:id>', views.edit_trainer_staff, name='edit_trainer_staff'), #updated
    path('delete_trainer_staff/<int:id>', views.delete_trainer_staff, name='delete_trainer_staff') #updated


]
