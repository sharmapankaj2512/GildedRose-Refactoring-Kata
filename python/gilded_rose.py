# -*- coding: utf-8 -*-

AGED_BRIE = "Aged Brie"
BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS = "Sulfuras, Hand of Ragnaros"
MAX_QUALITY = 50
MIN_QUALITY = 0
DOUBLE_VALUE_DAYS = 11
TRIPLE_VALUE_DAYS = 6


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self._update_item(item)

    def _update_item(self, item):
        if self._is_legendary(item):
            return
        if item.name == AGED_BRIE:
            self._update_aged_brie(item)
        elif item.name == BACKSTAGE_PASS:
            self._update_backstage_pass(item)
        else:
            self._update_ordinary(item)

    def _update_aged_brie(self, item):
        self._raise_quality(item)
        item.sell_in -= 1
        if item.sell_in < 0:
            self._raise_quality(item)

    def _update_backstage_pass(self, item):
        self._raise_quality(item)
        if item.sell_in < DOUBLE_VALUE_DAYS:
            self._raise_quality(item)
        if item.sell_in < TRIPLE_VALUE_DAYS:
            self._raise_quality(item)
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = MIN_QUALITY

    def _update_ordinary(self, item):
        self._lower_quality(item)
        item.sell_in -= 1
        if item.sell_in < 0:
            self._lower_quality(item)

    def _is_legendary(self, item):
        return item.name == SULFURAS

    def _raise_quality(self, item):
        if item.quality < MAX_QUALITY:
            item.quality += 1

    def _lower_quality(self, item):
        if item.quality > MIN_QUALITY:
            item.quality -= 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
