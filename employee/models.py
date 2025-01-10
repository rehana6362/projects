from django.db import models

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)  # Unique identifier for each employee
    name = models.CharField(max_length=100)          # Name of the employee
    department = models.CharField(max_length=100, blank=True, null=True)  # Department where the employee works
    email = models.EmailField(unique=True)          # Contact email of the employee
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    phone = models.CharField(max_length=15)


    def __str__(self):
        return self.name


class EmployeeRecord(models.Model):
    id = models.AutoField(primary_key=True)          # Unique identifier for each record
    employee = models.ForeignKey(
        Employee, 
        on_delete=models.CASCADE,                   # Cascade delete records when employee is deleted
        related_name="records"
    )
    record_id = models.IntegerField()               # Identifier for the CV record submitted
    submission_date = models.DateTimeField(auto_now_add=True)  # Date and time of submission
    skill = models.CharField(max_length=100, blank=True, null=True)  # Skill associated with the submitted record


    def __str__(self):
        return f"Record {self.record_id} by {self.employee.name}"


class PerformanceMetric(models.Model):
    metric_id = models.AutoField(primary_key=True)  # Unique identifier for each metric
    employee = models.ForeignKey(
        'Employee',  # Assuming the Employee model is already created
        on_delete=models.CASCADE,
        related_name='performance_metrics'
    )  # Foreign key linking to the employees table
    time_interval = models.CharField(max_length=50)  # Time interval (e.g., daily, weekly, etc.)
    total_records = models.IntegerField()           # Total number of records submitted
    target = models.IntegerField()                  # Submission target for the employee

    def __str__(self):
        return f"Metric {self.metric_id} for {self.employee.name}"



class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='tasks')  # Related to employee
    title = models.CharField(max_length=200)  # Title of the task
    description = models.TextField()  # Task description
    due_date = models.DateTimeField()  # Task deadline
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Completed', 'Completed')])  # Task status


    def __str__(self):
        return self.title