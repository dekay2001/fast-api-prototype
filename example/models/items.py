class Items:
    def __init__(self, items=None):
        self._items = items or {
            "1": {"id": "1", "description": "snoop"},
            "2": {"id": "2", "description": "dogg"},
        }

    def add(self, item):
        self._items[item.id] = item
        print(self._items)

    def get(self, id):
        return self._items.get(id)
