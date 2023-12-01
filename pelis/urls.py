from django.urls import path
from pelis.views import Pelis, PeliDetail

urlpatterns = [
    path('', Pelis.as_view()),
    path('<str:pk>', PeliDetail.as_view())
]