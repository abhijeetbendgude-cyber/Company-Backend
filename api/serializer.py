from rest_framework import serializers
from api.models import Company
from api.models import Employee
from api.models import Project

class CompanySerializer(serializers.ModelSerializer):
    company_id = serializers.ReadOnlyField()

    class Meta:
        model = Company
        fields = ['company_id', 'name', 'location', 'about', 'type', 'added_date', 'active']  


class EmployeeSerializer(serializers.ModelSerializer):
    employee_id = serializers.ReadOnlyField()

    class Meta:
        model = Employee
        fields = ['employee_id', 'name', 'email', 'address', 'phone', 'about', 'position', 'company']


class ProjectSerializer(serializers.ModelSerializer):
    company = CompanySerializer()  # Nested Company Serializer
    employee = EmployeeSerializer(many=True)  # Nested Employee Serializer
    project_id = serializers.ReadOnlyField()

    class Meta:
        model = Project
        fields = ['project_id', 'title', 'description', 'start_date', 'end_date', 'company', 'employee', 'status']

