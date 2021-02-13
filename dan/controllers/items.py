import dan.models.items as danitems


class GetItemsController:
    def __init__(self, items=None):
        self._items = items or danitems.Items()

    def get(self, id):
        return self._items.get(id)
