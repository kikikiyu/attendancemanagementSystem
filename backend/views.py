from django.db.models import Count
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from  backend.models import Employee,Attendance,Overtime,Leave,Department
from django.middleware.csrf import get_token
from django.core import serializers
import json


def index(request):
    return HttpResponse("here is backend")

def employee_check(request):
    Employee_list = Employee.objects.all()
    result ={}
    jsondata = serializers.serialize('json',Employee_list)
    jsondatautf8 = json.loads(jsondata,encoding = 'utf-8')
    result = {
        "code":200,
        "data":{
            "total":len(Employee_list),
            "items":jsondatautf8
        }
    }
    return  JsonResponse(result)

def employee_add(request):
    employeeid_add=request.GET.get('employeeid')
    employeename_add = request.GET.get('employeename')
    superioremployeeid_add = request.GET.get('superioremployeeid')
    did = Department.objects.get(departmentid = request.GET['departmentid'])
    #departmentid_add = request.GET.get('departmentid')
    Employee.objects.create(employeeid=employeeid_add,employeename=employeename_add,superioremployeeid=superioremployeeid_add,departmentid=did)
    result = False
    if Employee.objects.filter(employeeid=employeeid_add,employeename=employeename_add,superioremployeeid=superioremployeeid_add,departmentid=did):
        result = True
    return HttpResponse(json.dumps(result))

def employee_delete(request):
    employeeid_delete = request.GET['employeeid']
    Employee.objects.filter(employeeid__contains= employeeid_delete).delete()
    result= True
    if Employee.objects.filter(employeeid__contains = employeeid_delete).exists():
        result = False
    return  HttpResponse(json.dumps(result))

def employee_change(request):
    employeeid_before = request.GET.get('employeeidbefore')
    employeeid_change = request.GET.get('employeeid')
    employeename_change = request.GET.get('employeename')
    superioremployeeid_change = request.GET.get('superioremployeeid')
    did = Department.objects.get(departmentid=request.GET['departmentid'])
    Employee.objects.filter(employeeid__contains=employeeid_before).update(employeeid=employeeid_change,employeename=employeename_change,superioremployeeid=superioremployeeid_change,departmentid=did)
    result=False
    if Employee.objects.filter(employeeid=employeeid_change,employeename=employeename_change,superioremployeeid=superioremployeeid_change,departmentid=did).exists():
        result = True
    return  HttpResponse(json.dumps(result))


def overtime_check(request):
    #employeeid_check=request.GET.get('employeeid')
    #result= Overtime.objects.filter(employeeid=employeeid_check)
    result = Overtime.objects.all()
    context = {"ls": result}
    return render(request, "overtime.html", context)

def leave_check(request):
    #employeeid_check=request.GET.get('employeeid')
    #result= Leave.objects.filter(employeeid=employeeid_check)
    result=Leave.objects.all()
    context = {"ls": result}
    return render(request, "leave.html", context)

#系统主页面
def system(request):
    return render(request,"AttendanceManagementSystem.html")

#出勤表页面
def attendance_check(request):
    result= Attendance.objects.all()
    context={"ls":result}
    return render(request,"attendance.html",context)

#按编号查找结果
def find_attendance(request):
    employeeid_check = request.GET.get('employeeid')
    result = Attendance.objects.filter(employeeid=employeeid_check)
    context={"ls":result}
    return render(request,'checkattendance.html',context)

#打开添加页面
def addattendance(request):
    return render(request, "addattendance.html")

#保存
def save_attendance(request):
    attendancedate_add = request.GET.get('attendancedata')
    employeeid_add = Employee.objects.get(employeeid=request.GET['employeeid'])
    did = Department.objects.get(departmentid=request.GET['departmentid'])
    attendancetime_add = request.GET.get('attendancetime')
    retiredtime_add =request.GET.get('retiredtime')
    confirmsymbol_add =request.GET.get('confirmsymbol')
    confirmname_add = request.GET.get('confirmname')
    status_add =request.GET.get('status')
    # departmentid_add = request.GET.get('departmentid')
    Attendance.objects.create(attendancedate=attendancedate_add,employeeid=employeeid_add,
                           departmentid=did,attendancetime=attendancetime_add,retiredtime=retiredtime_add,confirmsymbol=confirmsymbol_add,confirmname=confirmname_add,status=status_add)
    result = False
    if  Attendance.objects.create(attendancedate=attendancedate_add,employeeid=employeeid_add,
                           departmentid=did,attendancetime=attendancetime_add,retiredtime=retiredtime_add,confirmsymbol=confirmsymbol_add,confirmname=confirmname_add,status=status_add).exists():
        result = True
    return HttpResponse(json.dumps(result))

#删除页面
def attendance_delete(request):
    attendanceid_delete = request.GET['attendanceid']
    Attendance.objects.filter(attendanceid__contains= attendanceid_delete).delete()
    result= True
    if Attendance.objects.filter(attendanceid__contains = attendanceid_delete).exists():
        result = False
    return render(request,"attendance.html")

