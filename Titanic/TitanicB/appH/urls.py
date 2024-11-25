from django.urls import path
from .views import HousePriView

urlpatterns = [path("appH/", HousePriView.as_view(), name='housepr_view'),
               ]