import pytest
from assertpy import assert_that

import example.models.items as items


class TestItems:
    def test_get_returns_specified_item(self):
        item_collection = items.Items()
        item = item_collection.get("1")
        assert_that(item.get("id")).is_equal_to("1")
