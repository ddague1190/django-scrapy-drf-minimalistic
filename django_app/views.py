from rest_framework import generics
from django_app.models import Bike, Manufacturer
from django_app.serializers import BikeSerializer
from django_filters import rest_framework as filters

class BikeFilter(filters.FilterSet):
    year = filters.NumberFilter(
        field_name='year',
        method='year_filter',
        label='Year'
    )

    def year_filter(self, queryset, name, value):        
        queryset = queryset.filter(start_year__lte=value, end_year__gte=value)
        return queryset           

    class Meta:
        model = Bike
        fields = ("mfg", "year")

class BikeList(generics.ListAPIView):
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BikeFilter

    def __str__(self):
        return self.title