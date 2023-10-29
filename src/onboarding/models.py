from django.db import models
from django.urls import reverse

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    department = models.CharField(max_length=100)
    start_date = models.DateField(auto_created=True)
    is_onboarded = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_absolute_url(self):
        return reverse('employee_detail', kwargs={'pk': self.pk})

    def get_absolute_update_url(self):
        return reverse('employee_update', kwargs={'pk': self.pk})

    def get_absolute_delete_url(self):
        return reverse('employee_delete', kwargs={'pk': self.pk})

    def get_absolute_mark_as_onboarded_url(self):
        return reverse('employee_mark_as_onboarded', kwargs={'pk': self.pk})

    