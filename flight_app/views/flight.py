import time
import datetime

from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import GenericViewSet

from flight_app.models import Flight
from flight_app.serializers.flight import FlightSerializer


class GetFlights(mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):

    queryset = Flight.objects.all()

    serializer_class = FlightSerializer

    def get_queryset(self):
        qs = self.queryset

        if 'flight_num' in self.request.query_params:
            qs = qs.filter(flight_num=self.request.query_params['flight_num'])

        if 'origin' in self.request.query_params:
            qs = qs.filter(origin_country=self.request.query_params['origin'])

        if 'destination' in self.request.query_params:
            qs = qs.filter(destination_country=self.request.query_params['destination'])

        if 'is_cancelled' in self.request.query_params:
            qs = qs.filter(is_cancelled=self.request.query_params['is_cancelled'])

        if 'min_price' in self.request.query_params and 'max_price' in self.request.query_params:
            qs = qs.filter(price__range=(self.request.query_params['min_price'], self.request.query_params['max_price']))

        elif 'min_price' in self.request.query_params:
            qs = qs.filter(price__gt=(self.request.query_params['min_price']))

        elif 'max_price' in self.request.query_params:
            qs = qs.filter(price__lt=(self.request.query_params['max_price']))

        if 'min_data' in self.request.query_params and 'max_date' in self.request.query_params:
            qs = qs.filter(origin_dt__range=(self.request.query_params['min_data'] , self.request.query_params['max_date'])) # "%d/%m/%Y"

        elif 'min_data' in self.request.query_params:
            qs = qs.filter(origin_dt__gt=(self.request.query_params['min_data'])) # "%d/%m/%Y"

        elif 'max_date' in self.request.query_params:
            qs = qs.filter(origin_dt__lt=(self.request.query_params['max_date'])) # "%d/%m/%Y"

        return qs


class AddFlight(mixins.CreateModelMixin, mixins.UpdateModelMixin, GenericViewSet):

    queryset = Flight.objects.all()

    serializer_class = FlightSerializer

    permission_classes = [IsAuthenticated, IsAdminUser]

