from rest_framework import viewsets
from .models import *
from .serializers import *

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class=Employeeserializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class=Departmentserializer

class LeavesViewSet(viewsets.ModelViewSet):
    queryset = Leaves.objects.all()
    serializer_class=Leavesserializer

class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class=Projectsserializer