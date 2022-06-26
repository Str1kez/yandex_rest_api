from rest_framework import serializers

from api.models import ShopUnit


class ShopUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopUnit
        fields = ['id', 'name', 'type', 'parentId', 'date', 'price', 'children']


ShopUnitSerializer._declared_fields['children'] = ShopUnitSerializer(many=True, source='get_children', required=False)
