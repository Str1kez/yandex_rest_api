from typing import List

from api.models import ShopUnit


def update_parent_price(instance_list: List[ShopUnit]):
    for instance in instance_list:
        while instance:
            instance.update_price()
            instance = instance.parentId
