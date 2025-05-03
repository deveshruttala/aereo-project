from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
import django_filters
from .models import Task
from .serializers import TaskSerializer

class TaskFilter(django_filters.FilterSet):
    # Define filters for 'completed' and 'date'
    completed = django_filters.BooleanFilter(field_name='completed')
    date = django_filters.DateFilter(field_name='date')

    class Meta:
        model = Task
        fields = ['completed', 'date']

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    # Using two filter backends: DjangoFilterBackend for filtering and OrderingFilter for ordering
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    
    # Associating the TaskFilter for filtering tasks based on 'completed' and 'date'
    filterset_class = TaskFilter
    
    # Enabling ordering by the 'date' field
    ordering_fields = ['date']
    ordering = ['date']  # Default ordering is ascending by 'date'
