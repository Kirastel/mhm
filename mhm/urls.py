from django.urls import path
from drf_spectacular.views import SpectacularSwaggerView, SpectacularRedocView


urlpatterns = [
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

