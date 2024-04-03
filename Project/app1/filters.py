
import django_filters
from app1.models import contactEnquiry

class OrderFilters(django_filters.FilterSet):
   class Meta:
        model = contactEnquiry
        fields = ["name","email"]
