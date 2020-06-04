from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Employee(models.Model):
    employeeid= models.IntegerField(db_column='employeeID',primary_key=True)
    employeename= models.CharField(db_column='employeename',max_length=45)
    superioremployeeid = models.IntegerField(db_column='superioremployeeID',null=True,blank=True)
    departmentid = models.ForeignKey('Department',models.DO_NOTHING,db_column='departmentID')

class Attendance(models.Model):
    attendanceid = models.AutoField(primary_key=True)
    attendancedate = models.DateField()
    employeeid = models.ForeignKey(Employee,models.DO_NOTHING,db_column='employeeID')
    departmentid = models.ForeignKey('Department',models.DO_NOTHING,db_column='departmentID')
    attendancetime = models.TimeField(null=True,blank=True)
    retiredtime = models.TimeField(null=True,blank=True)
    worktime = models.TimeField(null=True,blank=True)
    confirmsymbol =models.IntegerField(db_column='confirmsymbol')
    confirmname =models.CharField(db_column='confirmname',max_length=45)

    status = models.PositiveSmallIntegerField()

class Overtime(models.Model):
    overtimeid = models.AutoField(primary_key=True)
    year = models.DateField()
    month = models.DateField()
    employeeid = models.ForeignKey(Employee,models.DO_NOTHING,db_column='employeeID')
    departmentid = models.ForeignKey('Department',models.DO_NOTHING,db_column='departmentID')
    overtimekind = models.CharField(db_column='overtimekind',max_length=45)
    overtimehour = models.IntegerField(db_column='overtimehour')

class Leave(models.Model):
    leaveid =models.AutoField(primary_key=True)
    year = models.DateField()
    month = models.DateField()
    employeeid = models.ForeignKey(Employee,models.DO_NOTHING,db_column='employeeID')
    departmentid = models.ForeignKey('Department',models.DO_NOTHING,db_column='departmentID')
    leavekind = models.CharField(db_column='leavekind',max_length=45)
    leavedays = models.IntegerField(db_column='leavedays')

class Department(models.Model):
    departmentid = models.IntegerField(db_column='departmentID',primary_key=True)
    departmentname = models.CharField(db_column='departmentname',max_length=45)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'

class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
