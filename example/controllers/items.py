import example.models.items as items


class GetItemsController:
    def __init__(self, items=None):
        self._items = items or items.Items()

    def get(self, id):
        return self._items.get(id)
