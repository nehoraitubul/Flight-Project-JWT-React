from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Flight(models.Model):

    flight_num = models.CharField(max_length=256, db_column="flight_num", null=False, blank=False)
    origin_country = models.CharField(max_length=50, db_column="origin_country", null=False, blank=False)
    origin_city = models.CharField(max_length=50, db_column="origin_city", null=False, blank=False)
    origin_code = models.CharField(max_length=50, db_column="origin_code", null=False, blank=False)
    destination_country = models.CharField(max_length=50, db_column="destination_country", null=False, blank=False)
    destination_city = models.CharField(max_length=50, db_column="destination_city", null=False, blank=False)
    destination_code = models.CharField(max_length=50, db_column="destination_code", null=False, blank=False)
    origin_dt = models.BigIntegerField(db_column="origin_dt", null=False, blank=False)
    destination_dt = models.BigIntegerField(db_column="destination_dt", null=False, blank=False)
    total_seats = models.SmallIntegerField(db_column="total_seats", null=False, blank=False)
    seats_left = models.SmallIntegerField(db_column="seats_left", null=False, blank=False)
    is_cancelled = models.BooleanField(db_column="is_cancelled", null=False, blank=False)
    price = models.SmallIntegerField(db_column="price", null=False, blank=False)


    class Meta:
        db_table = 'flights'


class Order(models.Model):

    flight_id = models.ForeignKey('Flight', on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    number_of_seats = models.SmallIntegerField(db_column="number_of_seats", null=False, blank=False)
    order_date = models.DateTimeField(db_column="order_date", null=False, blank=False)
    total_price =  models.SmallIntegerField(db_column="total_price", null=False, blank=False)

    class Meta:
        db_table = 'orders'
