from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from onboarding.models import Employee
from .serializers import EmployeeSerializer

class EmployeeListCreateAPIView(ListCreateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    permission_classes = [IsAuthenticated]
    name = 'employee-api-list'


class EmployeeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    permission_classes = [IsAuthenticated]
    name = 'employee-api-detail'


class EmployeeMarkAsOnboardedAPIView(APIView):
    model = Employee
    name = 'employee-api-mark-onboarded'

    def get_object(self, pk=None):
        if pk:
            obj = get_object_or_404(self.model, pk=pk)
            return obj
        return None

    def post(self, request, pk):
        employee = self.get_object(pk=pk)
        if employee:
            employee.is_onboarded = True
            employee.save()
            return Response({'detail': 'Employee marked as onboarded'}, status=status.HTTP_200_OK)
        return Response({'detail': 'Employee not Found'}, status=status.HTTP_404_NOT_FOUND)