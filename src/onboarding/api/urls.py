from django.urls import path

from .import views as api_views


urlpatterns = [
    path('', api_views.EmployeeListCreateAPIView.as_view(), name=api_views.EmployeeListCreateAPIView.name),
    path('<int:pk>/', api_views.EmployeeRetrieveUpdateDestroyAPIView.as_view(), name=api_views.EmployeeRetrieveUpdateDestroyAPIView.name),
    path('onboard/<int:pk>/', api_views.EmployeeMarkAsOnboardedAPIView.as_view(), name=api_views.EmployeeMarkAsOnboardedAPIView.name),
]
