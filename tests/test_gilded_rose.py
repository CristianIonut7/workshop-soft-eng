# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0), Item("lol", 10, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_lol(self):
        items = [Item("foo", 0, 0), Item("lol", 10, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)
        self.assertEqual("lol", items[1].name)
        self.assertEqual(9, items[1].sell_in)
        self.assertEqual(4, items[1].quality)

    def test_Aged_Backpasses(self):
        items = [Item("Aged Brie", 0, 0), 
                 Item("Backstage passes to a TAFKAL80ETC concert", 45, 5),
                 Item("Backstage passes to a TAFKAL80ETC concert", 10, 5),
                 Item("Backstage passes to a TAFKAL80ETC concert", -1, 5),
                 Item("Backstage passes to a TAFKAL80ETC concert", 5, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Aged Brie", items[0].name)
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(2, items[0].quality)
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[1].name)
        self.assertEqual(44, items[1].sell_in)
        self.assertEqual(6, items[1].quality)
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[2].name)
        self.assertEqual(9, items[2].sell_in)
        self.assertEqual(7, items[2].quality)
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[3].name)
        self.assertEqual(-2, items[3].sell_in)
        self.assertEqual(0, items[3].quality)
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[4].name)
        self.assertEqual(4, items[4].sell_in)
        self.assertEqual(8, items[4].quality)
        
    def test_negSellinForRand(self):
        items = [Item("Test", -1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Test", items[0].name)
        self.assertEqual(-2, items[0].sell_in)
        self.assertEqual(8, items[0].quality)
    def test_Sulfuras(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 15, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Sulfuras, Hand of Ragnaros", items[0].name)
        self.assertEqual(15, items[0].sell_in)
        self.assertEqual(80, items[0].quality)



        
if __name__ == '__main__':
    unittest.main()
