from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('blogs', views.BlogViewSet)

urlpatterns = [
    path('', include(router.urls))
]
