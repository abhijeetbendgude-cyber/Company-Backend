from django.contrib import admin
from django.urls import path,include
from api.views import CompanyViewSet, EmployeeViewSet, ProjectViewSet
from rest_framework import routers 
from api.views import CustomAuthToken

router=routers.DefaultRouter()
router.register(r'companies',CompanyViewSet)
router.register(r'employees',EmployeeViewSet)
router.register(r'projects',ProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
     path('login/', CustomAuthToken.as_view(), name='api-login'),
]
