from rest_framework import serializers

from api.models import ShopUnit


class ShopUnitSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = ShopUnit
        fields = ['id', 'name', 'type', 'parentId', 'date', 'price', 'children']

    def get_children(self, obj):
        children = obj.get_children()
        children_data = ShopUnitSerializer(many=True, instance=children).data
        if not children_data:
            return children_data if obj.is_category else None
        return children_data

    def validate(self, attrs):
        # TODO: Написать здесь валидацию для данных (описано в Notion)
        pass
