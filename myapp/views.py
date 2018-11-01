from django.shortcuts import render
from django.views.generic import DetailView, ListView, UpdateView

from .models import Employee


def fun1(request):
    return render(request, "myapp/home.html")


def fun2(request):
    return render(request, "myapp/second.html")


class EmployeeView(DetailView):
    model = Employee
    template_name = "myapp/employee_detail.html"


class EmployeeList(ListView):
    model = Employee
    template_name = 'myapp/all_employees.html'
    paginate_by = 2


class EmployeeUpdate(UpdateView):
    model = Employee
    template_name = 'myapp/update_employee.html'
    fields = ['name', 'salary']
