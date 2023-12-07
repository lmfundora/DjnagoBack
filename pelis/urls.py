from django.urls import path
from pelis.views import Pelis, PeliDetail, Label, LabelDetail

urlpatterns = [
    path('', Pelis.as_view()),
    path('<str:pk>', PeliDetail.as_view()),
    path('labels/', Label.as_view()),
    path('labels/<str:pk>', LabelDetail.as_view()),
]