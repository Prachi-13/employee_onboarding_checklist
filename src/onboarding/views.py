from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, UpdateView, DeleteView, DetailView, CreateView, RedirectView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.http import Http404
from .models import Employee
from .forms import EmployeeForm
from django.contrib import messages

# Create your views here.
class EmployeeMixin:
    model = Employee


class EmployeeListView(LoginRequiredMixin, EmployeeMixin, ListView):
    pass
    


class EmployeeDetailView(LoginRequiredMixin, EmployeeMixin, DetailView):    
    pass


class EmployeeCreateView(LoginRequiredMixin, SuccessMessageMixin, EmployeeMixin, CreateView):
    form_class = EmployeeForm
    success_url = reverse_lazy('employee_list')
    success_message = "Employee Created Successfully!"    


class EmployeeUpdateView(LoginRequiredMixin, SuccessMessageMixin, EmployeeMixin, UpdateView):
    form_class = EmployeeForm
    success_url = reverse_lazy('employee_list')
    success_message = "Employee Updated Successfully!"


class EmployeeDeleteView(LoginRequiredMixin, SuccessMessageMixin, EmployeeMixin, DeleteView):
    success_url = reverse_lazy('employee_list')
    success_message = "Employee Deleted Successfully!"


class EmployeeMarkAsOnboardedView(LoginRequiredMixin, SuccessMessageMixin, EmployeeMixin, View):

    def get_object(self, pk=None):
        if pk:
            obj = get_object_or_404(self.model, pk=pk)
            return obj
        raise Http404('No Object found!')

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        obj = self.get_object(pk=pk)
        obj.is_onboarded = True
        obj.save()
        messages.success(request, f'Employee: {obj.first_name} {obj.last_name}(Emp_id:{obj.id}) onboaded successfully!')
        return redirect('employee_list')
