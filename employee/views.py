from django.shortcuts import render, get_object_or_404,redirect
from .models import Employee, EmployeeRecord, PerformanceMetric,Task
from .forms import TaskForm
from django.db.models import Sum
import json
from django.utils.timezone import now,timedelta

# import Chart from 'chart.js/auto'

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee/employee_list.html', {'employees': employees})


def employee_detail(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    records = employee.records.all()  # Fetch related employee records
    metrics = employee.performance_metrics.all()  # Fetch related performance metrics
    tasks = employee.tasks.all()  # Fetch all tasks related to the employee

    return render(request, 'employee/employee_detail.html', {
        'employee': employee,
        'records': records,
        'metrics': metrics,
        'tasks': tasks,  # Pass tasks to template
    })

def performance_metrics(request):
    metrics = PerformanceMetric.objects.all()
    return render(request, 'employee/performance_metrics.html', {'metrics': metrics})


def performance_summary(request):
    employees = Employee.objects.all()
    summary = []

    for employee in employees:
        # Total and average records for the employee
        total_records = employee.records.count()
        avg_records = EmployeeRecord.objects.all().count() / employees.count() if employees.count() else 0
        
        # Fetch performance metrics
        metrics = employee.performance_metrics.all()
        
        # Check task statuses
        tasks = employee.tasks.all()
        completed_tasks = tasks.filter(status='Completed').count()
        total_tasks = tasks.count()

        # Determine status based on tasks
        status = 'Completed' if completed_tasks == total_tasks and total_tasks > 0 else 'Pending'

        summary.append({
            'employee': employee,
            'total_records': total_records,
            'avg_records': avg_records,
            'metrics': metrics,
            'status': status,  # Add status to summary
        })

    return render(request, 'employee/performance_summary.html', {'summary': summary})





def performance_dashboard(request):
    today = now().date()
    
    # Calculate date ranges using the correct field `submission_date`
    daily_count = EmployeeRecord.objects.filter(submission_date=today).count()
    weekly_count = EmployeeRecord.objects.filter(
        submission_date__gte=today - timedelta(days=7)
    ).count()
    monthly_count = EmployeeRecord.objects.filter(
        submission_date__gte=today - timedelta(days=30)
    ).count()
    quarterly_count = EmployeeRecord.objects.filter(
        submission_date__gte=today - timedelta(days=90)
    ).count()
    half_yearly_count = EmployeeRecord.objects.filter(
        submission_date__gte=today - timedelta(days=182)
    ).count()
    yearly_count = EmployeeRecord.objects.filter(
        submission_date__gte=today - timedelta(days=365)
    ).count()

    # Pass the data to the template
    context = {
        'daily': daily_count,
        'weekly': weekly_count,
        'monthly': monthly_count,
        'quarterly': quarterly_count,
        'half_yearly': half_yearly_count,
        'yearly': yearly_count,
    }
    return render(request, 'employee/dashboard.html', context)
    
def all_employees(request):
    employees = Employee.objects.all()  # Fetch all employees
    return render(request, 'employee/all_employees.html', {'employees': employees})



# View to display all tasks
def all_tasks(request):
    tasks = Task.objects.select_related('employee')  # Optimize query with select_related
    return render(request, 'employee/all_tasks.html', {'tasks': tasks})


# View to display a single task's details
def task_detail(request, task_id):
    task = get_object_or_404(Task, task_id=task_id)  # Fetch task by its ID
    return render(request, 'employee/task_detail.html', {'task': task})

# View to create a new task
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new task to the database
            return redirect('all_tasks')  # Redirect to task list
    else:
        form = TaskForm()
    return render(request, 'employee/create_task.html', {'form': form})

# View to update an existing task
def update_task(request, task_id):
    # Use the correct primary key 'task_id'
    task = get_object_or_404(Task, task_id=task_id) 

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail', task_id=task.task_id)  # Redirect to task detail page
    else:
        form = TaskForm(instance=task)
    
    return render(request, 'employee/update_task.html', {'form': form, 'task': task})

# View to delete a task
def delete_task(request, task_id):
    task = get_object_or_404(Task, task_id=task_id)  # Fetch task by its ID
    task.delete()  # Delete the task
    return redirect('all_tasks')  # Redirect to task list after deletion

def search_employee(request):
    employee_id = request.GET.get('employee_id')
    if employee_id:
        employee = get_object_or_404(Employee, employee_id=employee_id)
        return render(request, 'employee/employee_detail.html', {'employee': employee})
    return render(request, 'employee/employee_list.html', {'error': 'Employee not found'})