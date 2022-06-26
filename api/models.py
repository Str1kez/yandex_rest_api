from django.db import models
from django.db.models import Avg
from mptt.models import MPTTModel, TreeForeignKey


class ShopUnit(MPTTModel):
    id = models.UUIDField(unique=True, null=False, primary_key=True)
    name = models.CharField(max_length=120, null=False)
    type = models.CharField(max_length=20, null=False)
    date = models.DateTimeField(null=False)
    price = models.PositiveIntegerField(null=True)
    parentId = TreeForeignKey('self', on_delete=models.CASCADE, null=True, related_name='children')

    @property
    def is_category(self) -> bool:
        return self.type == 'CATEGORY'

    def update_price(self):
        if not self.is_category:
            return
        average_price = self.get_children().aggregate(Avg('price'))
        self.price = int(average_price['price__avg'])
        self.save()

    class MPTTMeta:
        order_insertion_by = ['id']
        parent_attr = 'parentId'
