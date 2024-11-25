from django.urls import path
from . views import TitanicView

urlpatterns = [path("appT/", TitanicView.as_view(), name='titanic_view'),
               ]