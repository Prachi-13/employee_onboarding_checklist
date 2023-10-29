from django.urls import path

from .import views

urlpatterns = [
    path('', views.EmployeeListView.as_view(), name='employee_list'),
    path('<int:pk>/', views.EmployeeDetailView.as_view(), name='employee_detail'),
    path('create/', views.EmployeeCreateView.as_view(), name='employee_create'),
    path('update/<int:pk>/', views.EmployeeUpdateView.as_view(), name='employee_update'),
    path('delete/<int:pk>/', views.EmployeeDeleteView.as_view(), name='employee_delete'),
    path('mark-as-onboarded/<int:pk>/', views.EmployeeMarkAsOnboardedView.as_view(), name="employee_mark_as_onboarded"),
]
