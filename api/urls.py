from django.urls import path

from api.views import ShopUnitAPIView

app_name = 'api'

urlpatterns = [
    path('imports/', ShopUnitAPIView.as_view()),
    path('nodes/<uuid:id>/', ShopUnitAPIView.as_view()),
]
