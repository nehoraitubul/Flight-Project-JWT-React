from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, viewsets

from flight_app.models import Order
from flight_app.serializers.order import OrderSerializer


class Orders(viewsets.ModelViewSet):

    queryset = Order.objects.all()

    permission_classes = [IsAuthenticated]

    serializer_class = OrderSerializer

    def get_queryset(self):
        qs = self.queryset
        user = self.request.user

        if not user.is_staff:
            qs = qs.filter(user_id = user.id)

        return qs

