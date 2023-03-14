from rest_framework.routers import DefaultRouter
from flight_app.views.order import Orders



router = DefaultRouter()
router.register('', Orders)


urlpatterns = [

]

urlpatterns.extend(router.urls)