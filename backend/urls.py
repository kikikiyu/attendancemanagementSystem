
from django.urls import path
import backend.views as api
from  django.conf.urls import  url ##
from  . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('employeecheck',api.employee_check),
    path('employeeadd',api.employee_add),
    path('employeedelete',api.employee_delete),
    path('employeechange',api.employee_change),

    url(r'^system/$',views.system),
    path('attendance/',views.attendance_check),
    path('overtime/',views.overtime_check),
    path('leave/',views.leave_check),
    path('addattendance/',views.addattendance),
    path('saveattendance/',views.save_attendance),
    path('checkattendance/',views.find_attendance),

]
