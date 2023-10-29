from rest_framework import serializers
from onboarding.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='employee-api-detail')
    class Meta:
        model = Employee
        fields = ['url', 'id', 'first_name', 'last_name', 'email', 'department', 'start_date', 'is_onboarded']
