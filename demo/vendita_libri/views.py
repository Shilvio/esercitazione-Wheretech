from rest_framework import generics
from .models import Libro
from .serializers import LibroSerializer
from rest_framework.filters import SearchFilter
from django_filters import rest_framework as filters

# Filtro per la ricerca per titolo e nazionalità dell'autore
class LibroFilter(filters.FilterSet):
    titolo = filters.CharFilter(lookup_expr='icontains')
    autore__indirizzo__nazionalita = filters.CharFilter(field_name='autore__indirizzo__nazionalita', lookup_expr='icontains')

    class Meta:
        model = Libro
        fields = ['titolo', 'autore__indirizzo__nazionalita']


class LibroListView(generics.ListAPIView):

    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter)
    filterset_class = LibroFilter
    search_fields = ['titolo', 'autore__nome', 'autore__cognome']  # Aggiungi altre opzioni se necessario


class LibroOrderView(generics.ListAPIView):
    queryset = Libro.objects.all().order_by('-quantita', '-prezzo')
    serializer_class = LibroSerializer


