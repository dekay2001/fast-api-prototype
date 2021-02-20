import collections as collections

import pytest
from assertpy import assert_that

import example.models.items as items


class TestItems:
    def setup(self):
        self.item_collection = items.Items()

    def test_get_returns_none_if_item_does_not_exist(self):
        assert_that(self.item_collection.get("does not exist")).is_none()

    def test_get_returns_specified_item_if_item_exists(self):
        assert_that(self.item_collection.get("1")).is_not_none()

    def test_can_add_an_item(self):
        item = self._make_item(item_id="5", item_data=None)
        self.item_collection.add(item)
        assert_that(self.item_collection.get("5")).is_equal_to(item)

    def _make_item(self, item_id=None, item_data=None):
        Item = collections.namedtuple("id", "id data")
        return Item(id=item_id, data=item_data)
