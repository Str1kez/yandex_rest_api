from rest_framework.exceptions import NotFound
from rest_framework.generics import RetrieveAPIView
from api.models import ShopUnit
from api.serializers import ShopUnitSerializer


class ShopUnitAPIView(RetrieveAPIView):
    serializer_class = ShopUnitSerializer
    queryset = ShopUnit.objects.all()
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        shop_unit_id = kwargs.get('id')
        if shop_unit_id is None:
            raise NotFound
        return self.retrieve(request, *args, **kwargs)
