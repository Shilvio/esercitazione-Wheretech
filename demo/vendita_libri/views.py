from rest_framework import generics
from .models import Libro
from .serializers import LibroSerializer
from rest_framework.filters import SearchFilter
from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination

# Configurazione personalizzata della paginazione
class CustomPagination(PageNumberPagination):
    page_size = 10  # Numero di elementi per pagina
    page_size_query_param = 'page_size'  # Permette al client di specificare la dimensione della pagina
    max_page_size = 100  # Numero massimo di elementi per pagina

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
    search_fields = ['titolo', 'autore__nome', 'autore__cognome']
    pagination_class = CustomPagination  # Aggiungi paginazione


class LibroOrderView(generics.ListAPIView):
    queryset = Libro.objects.all().order_by('-quantita', '-prezzo')
    filter_backends = (filters.DjangoFilterBackend, SearchFilter)
    filterset_class = LibroFilter
    search_fields = ['titolo', 'autore__nome', 'autore__cognome']
    serializer_class = LibroSerializer
    pagination_class = CustomPagination  # Aggiungi paginazione