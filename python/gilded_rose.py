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
            if item.name != AGED_BRIE and item.name != BACKSTAGE_PASS:
                if item.quality > MIN_QUALITY:
                    if item.name != SULFURAS:
                        item.lower_quality()
            else:
                if item.quality < MAX_QUALITY:
                    item.raise_quality()
                    if item.name == BACKSTAGE_PASS:
                        if item.sell_in < DOUBLE_VALUE_DAYS:
                            if item.quality < MAX_QUALITY:
                                item.raise_quality()
                        if item.sell_in < TRIPLE_VALUE_DAYS:
                            if item.quality < MAX_QUALITY:
                                item.raise_quality()
            if item.name != SULFURAS:
                item.advance_day()
            if item.is_expired():
                if item.name != AGED_BRIE:
                    if item.name != BACKSTAGE_PASS:
                        if item.quality > MIN_QUALITY:
                            if item.name != SULFURAS:
                                item.lower_quality()
                    else:
                        item.drop_quality()
                else:
                    if item.quality < MAX_QUALITY:
                        item.raise_quality()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def advance_day(self):
        self.sell_in -= 1

    def is_expired(self):
        return self.sell_in < 0

    def raise_quality(self):
        if self.quality < MAX_QUALITY:
            self.quality += 1

    def lower_quality(self):
        if self.quality > MIN_QUALITY:
            self.quality -= 1

    def drop_quality(self):
        self.quality = MIN_QUALITY

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
