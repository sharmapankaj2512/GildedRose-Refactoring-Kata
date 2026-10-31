# -*- coding: utf-8 -*-

AGED_BRIE = "Aged Brie"
BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS = "Sulfuras, Hand of Ragnaros"
MAX_QUALITY = 50
MIN_QUALITY = 0
DOUBLE_VALUE_DAYS = 11
TRIPLE_VALUE_DAYS = 6


class GildedRose:

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            ageing_for(item).age(item)


class Legendary:
    """Sulfuras never has to be sold and never loses quality."""

    def age(self, item):
        return


class Maturing:
    """Aged Brie increases in quality the older it gets."""

    def age(self, item):
        item.raise_quality()
        item.advance_day()
        if item.is_expired():
            item.raise_quality()


class Appreciating:
    """A backstage pass gains value as the concert nears, then becomes worthless."""

    def age(self, item):
        item.raise_quality()
        if item.sell_in < DOUBLE_VALUE_DAYS:
            item.raise_quality()
        if item.sell_in < TRIPLE_VALUE_DAYS:
            item.raise_quality()
        item.advance_day()
        if item.is_expired():
            item.drop_quality()


class Perishable:
    """Ordinary stock degrades, twice as fast once its sell-by date passes."""

    def age(self, item):
        item.lower_quality()
        item.advance_day()
        if item.is_expired():
            item.lower_quality()


AGEING = {
    SULFURAS: Legendary(),
    AGED_BRIE: Maturing(),
    BACKSTAGE_PASS: Appreciating(),
}


def ageing_for(item):
    return AGEING.get(item.name, Perishable())


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
