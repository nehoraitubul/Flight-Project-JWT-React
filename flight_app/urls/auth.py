from django.urls import path
from rest_framework.routers import DefaultRouter


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from flight_app.views.auth import signup, me, GetUser

router = DefaultRouter()
router.register('users', GetUser)

urlpatterns = [
    path('signup/', signup),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('me/', me),
]

urlpatterns.extend(router.urls)