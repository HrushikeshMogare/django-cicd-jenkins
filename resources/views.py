from .serializers import EmployeeSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Employee
from rest_framework.permissions import IsAuthenticated



class EmployeeViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    
