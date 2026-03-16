from items.item import Item
from data.items import ITEM_DATABASE


def create_item(item_id):

    data = ITEM_DATABASE[item_id]

    return Item(
        data["name"],
        data["type"],
        data["stats"]
    )
