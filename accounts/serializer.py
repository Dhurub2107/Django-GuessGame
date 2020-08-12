from rest_framework import serializers
from .models import employees,Data

class employeeSerializer(serializers.ModelSerializer):

    class Meta:
        model=employees
        fields='__all__'
        #fields = ['emp_id', 'firstname']
class showdata(serializers.ModelSerializer):
    class Meta:
        model=Data
        fields='__all__'
