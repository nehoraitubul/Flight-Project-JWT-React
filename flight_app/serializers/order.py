from datetime import date

from rest_framework import serializers

from flight_app.models import Order


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = "__all__"
        # fields = ["id", "flight_id" , "number_of_seats" , "total_price"]


    def create(self, validated_data):
        # order = Order.objects.create(
        #     flight_id = validated_data['flight_id'],
        #     user_id = self.context['request'].user,
        #     number_of_seats = validated_data['number_of_seats'],
        #     order_date = date.today().strftime("%Y-%m-%d"),
        #     total_price = validated_data['total_price']
        # )
        #
        # return order

        return Order.objects.create(**validated_data)
