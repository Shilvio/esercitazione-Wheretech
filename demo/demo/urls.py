from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('vendita_libri.urls')),  # Includi gli URL della tua app
]
