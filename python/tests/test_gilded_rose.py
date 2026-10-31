# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)


class ItemTest(unittest.TestCase):
    def test_quality_stops_at_its_maximum(self):
        item = Item("Aged Brie", 5, 50)
        item.raise_quality()
        self.assertEqual(50, item.quality)

    def test_quality_stops_at_zero(self):
        item = Item("Elixir of the Mongoose", 5, 0)
        item.lower_quality()
        self.assertEqual(0, item.quality)


if __name__ == '__main__':
    unittest.main()
