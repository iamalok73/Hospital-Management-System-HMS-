import django_filters
from .models import Patient

class PatientFilter(django_filters.FilterSet):
    class Meta:
        model = Patient
        fields = ['name', 'status', 'doctor', 'bed_num']
