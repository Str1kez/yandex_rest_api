from django.urls import path

from api.views import ShopUnitAPIGetView, ShopUnitAPIPostView, ShopUnitAPIDeleteView

app_name = 'api'

urlpatterns = [
    path('imports', ShopUnitAPIPostView.as_view()),
    path('nodes/<uuid:id>', ShopUnitAPIGetView.as_view()),
    path('delete/<uuid:id>', ShopUnitAPIDeleteView.as_view()),
]
