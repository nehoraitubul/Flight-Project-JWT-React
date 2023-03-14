from django.urls import path, include

from flight_app.views import *

urlpatterns = [
    path('api/auth/', include('flight_app.urls.auth')),
    path('api/flights/', include('flight_app.urls.flight')),
    path('api/orders/', include('flight_app.urls.order')),
]