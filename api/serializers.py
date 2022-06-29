from typing import OrderedDict, List

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from api.models import ShopUnit


class ShopUnitSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = ShopUnit
        fields = ['id', 'name', 'type', 'parentId', 'date', 'price', 'children']

    def get_children(self, obj):
        print(obj)
        children = obj.get_children()
        children_data = ShopUnitSerializer(many=True, instance=children).data
        if not children_data:
            return children_data if obj.is_category else None
        return children_data

    def validate(self, attrs: OrderedDict) -> OrderedDict:
        # TODO: Написать здесь валидацию для данных (описано в Notion)
        print(self.initial_data)
        self.__validate_parent([x.get('parentId') for x in self.initial_data if x['parentId'] is not None])
        self.__validate_category([x.get('price') for x in self.initial_data if x['type'] == 'CATEGORY'])
        self.__validate_offer([x.get('price') for x in self.initial_data if x['type'] == 'OFFER'])
        self.__validate_id()
        return attrs

    def __validate_parent(self, parentId_list: List[str]):
        for parentId in parentId_list:
            for el in self.initial_data:
                if el['id'] == parentId:
                    if el['type'] == 'CATEGORY':
                        return
                    raise ValidationError
            try:
                parent_instance = ShopUnit.objects.get(id=parentId)
            except ShopUnit.DoesNotExist:
                raise ValidationError
            if not parent_instance.is_category:
                raise ValidationError

    @staticmethod
    def __validate_category(price_list: List[int | None]):
        if not all([price is None for price in price_list]):
            raise ValidationError

    @staticmethod
    def __validate_offer(price_list: List[int | None]):
        """Валидация на неотрицательную цену пройдет по модели"""
        if any([price is None for price in price_list]):
            raise ValidationError

    def __validate_id(self):
        id_set = {x['id'] for x in self.initial_data}
        if len(id_set) != len(self.initial_data):
            raise ValidationError
