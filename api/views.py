from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin
from rest_framework.response import Response

from api.models import ShopUnit
from api.serializers import ShopUnitSerializer


class ShopUnitAPIView(RetrieveModelMixin,
                      CreateModelMixin,
                      GenericAPIView):
    serializer_class = ShopUnitSerializer
    queryset = ShopUnit.objects.all()
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        shop_unit_id = kwargs.get('id')
        if shop_unit_id is None:
            raise NotFound
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        items = request.data.get('items')
        date = request.data.get('updateDate')
        if items is None or date is None:
            raise ValidationError
        for item in items:
            item['date'] = date
        # TODO: написать тут дальнейшую логику запроса /imports
        return Response(data=items, status=201)

