from import_export import resources
from .models import CountryGDP

class PersonResourc(resources.ModelResource):
    class Meta:
        model=CountryGDP