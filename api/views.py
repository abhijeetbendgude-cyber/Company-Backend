from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from api.serializer import CompanySerializer,EmployeeSerializer,ProjectSerializer
from api.models import Employee,Project,Company
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User



class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
     #companies/{company_id}/employees
    @action(detail=True,methods=['get'])
    def employee(self,request,pk=None):
        try:
            company=Company.objects.get(pk=pk)
            emps=Employee.objects.filter(company=company)
            emps_serializer=EmployeeSerializer(emps,many=True,context={'request':request})
            return Response(emps_serializer.data)
        except Company.DoesNotExist:
            return Response({'error':'Company does not exist'})
    pass

#Employee Viewset
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

#Project Viewset

class ProjectViewSet(viewsets.ModelViewSet):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer

class CustomAuthToken(ObtainAuthToken):
    """
    Custom Auth Token class to handle token generation and user authentication.
    """
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key,
                         'user_id':token.user.id,
                         'username': token.user.username,
                         }
                        )