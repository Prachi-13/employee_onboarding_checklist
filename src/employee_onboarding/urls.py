"""
URL configuration for employee_onboarding project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from onboarding.api import views as onboarding_api_view


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, format=None, **kwargs):
        return Response({
            'employees': reverse(onboarding_api_view.EmployeeListCreateAPIView.name, request=request, format=format),
            # 'swagger_endpoints': reverse('schema-swagger-ui', request=request, format=format),
       })


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('', include('onboarding.urls')),
]


api_urlpatterns = [

]
api_urlpatterns = [
    path('api/', include([
        path('', ApiRoot.as_view(), name=ApiRoot.name),
        path('employee/', include('onboarding.api.urls')),
    ])),
    path('api-auth/', include('rest_framework.urls'))
]

urlpatterns += api_urlpatterns