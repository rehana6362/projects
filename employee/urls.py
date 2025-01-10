from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),  # List of all employees
    path('employees/', views.all_employees, name='all_employees'),
    path('employee/<int:employee_id>/', views.employee_detail, name='employee_detail'),  # Employee details
    path('metrics/', views.performance_metrics, name='performance_metrics'),  # Performance metrics list
    path('performance_summary/', views.performance_summary, name='performance_summary'),  # Performance summary
    path('tasks/', views.all_tasks, name='all_tasks'),  # List of tasks
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),  # Task detail view
    path('task/create/', views.create_task, name='create_task'),  # Create task
    path('task/update/<int:task_id>/', views.update_task, name='update_task'),  # Update task
    path('task/delete/<int:task_id>/', views.delete_task, name='delete_task'),  # Delete task
    path('dashboard/', views.performance_dashboard, name='performance_dashboard'),
    path('search_employee/', views.search_employee, name='search_employee'),

]
