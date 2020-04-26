from django.urls import path
from . import views

urlpatterns = [
    path('emp_register', views.emp_register, name='emp_register'),
    path('emp_list', views.emp_list, name='emp_list'),
    path('update/<str:pk>',views.update_emp_list, name='update_emplist'),
    path('delete/<str:pk>',views.del_emp, name='delete_employee'),
]