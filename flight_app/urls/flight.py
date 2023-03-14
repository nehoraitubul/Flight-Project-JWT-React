from rest_framework.routers import DefaultRouter

from flight_app.views.flight import GetFlights, AddFlight

router = DefaultRouter()
router.register('all', GetFlights)
router.register('add_flight', AddFlight)

urlpatterns = [

]

urlpatterns.extend(router.urls)
