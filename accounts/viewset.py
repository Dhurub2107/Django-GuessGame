from rest_framework import viewsets
from . import models
from . import serializer

class EmployeeViewset(viewsets.ModelViewSet):
    queryset=models.employees.objects.all()
    serializer_class=serializer.employeeSerializer
class showdataViewset(viewsets.ModelViewSet):
    queryset=models.Data.objects.filter(emp_id=18)
    serializer_class=serializer.showdata 
