from django.urls import path
from . import views

app_name = "myapp"
urlpatterns = [
    path('dd1', views.fun1, name="home"),
    path('dd2', views.fun2, name="second"),
    path('employee/<int:pk>', views.EmployeeView.as_view(), name="employee_detail_view"),
    path('employee_list', views.EmployeeList.as_view(), name="employee_list"),
    path('employee_update/<int:pk>', views.EmployeeUpdate.as_view(), name="employee_update"),
]
