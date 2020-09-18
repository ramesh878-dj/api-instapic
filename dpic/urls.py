from dpic.views import *
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
# router.register('instapic', InstapicViewSet, basename='instapic')

urlpatterns = [
    path('', home, name="home"),
    path('getpic/', addsome),
]