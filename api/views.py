from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin, DestroyModelMixin
from rest_framework.response import Response

from api.misc.updaters import update_parent_price
from api.models import ShopUnit
from api.serializers import ShopUnitSerializer


class BaseAPIView(GenericAPIView):
    serializer_class = ShopUnitSerializer
    queryset = ShopUnit.objects.all()
    lookup_field = 'id'


class ShopUnitAPIGetView(RetrieveModelMixin, BaseAPIView):
    def get(self, request, *args, **kwargs):
        shop_unit_id = kwargs.get('id')
        if shop_unit_id is None:
            raise NotFound
        return self.retrieve(request, *args, **kwargs)


class ShopUnitAPIPostView(BaseAPIView):
    def post(self, request, *args, **kwargs):
        items = request.data.get('items')
        date = request.data.get('updateDate')
        if items is None or date is None:
            raise ValidationError
        for item in items:
            item['date'] = date
        print(items)
        serialized_data = self.serializer_class(data=items, many=True)
        if serialized_data.is_valid(raise_exception=False):
            serialized_data.save()
            update_parent_price([vd['parentId'] for vd in serialized_data.validated_data])
        return Response(serialized_data.data, status=200)


class ShopUnitAPIDeleteView(DestroyModelMixin, BaseAPIView):
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        update_parent_price([instance.parentId])
        return Response(status=200)
