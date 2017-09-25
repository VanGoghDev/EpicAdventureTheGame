import random


class Character:  # character class where we can keep all stats and items
    def __init__(self):
        self.level = 1
        self.hp = 100

    def level_up(self, n):
        self.level = n
        self.hp += 100 * n


class Hero(Character):
    def __init__(self, name, age):
        """

        :rtype: object
        """
        Character.__init__(self)
        self.backpack = []
        self.name = name
        self.age = age
        self.money = 0

    def hero_backpack(self, item):
        self.backpack.append(item)


class Trader(Character):
    traded_item = 0
    for_sale = ''
    sold_out_item = ''

    def __init__(self):
        Character.__init__(self)
        self.backpack = {}
        self.money = self.level * random.randint(100, 300)

    def backpack_upgrade(self, **items):
        for item in items:
            self.backpack[item] = items.get(item)
        return self.backpack

    def item_switch_trader_gives_to_hero(self, cycling, item, money, h):
        global traded_item
        if cycling == 1:
            while cycling == 1:
                if money >= self.backpack.get(item):
                    if item.upper() == 'NOTHING':
                        traded_item = 0
                        cycling = 0
                    else:
                        print 'Nice deal! Good luck in your journeys!'
                        items = self.backpack.keys()
                        for n in items:
                            if n == item.lower():
                                Hero.hero_backpack(h, n)
                        traded_item = self.backpack.pop(item.lower())
                        cycling = 0
                else:
                    print 'You don`t have enough money. Come here again when you will have enough money'
                    print 'Maybe something else?'
                    item = raw_input()
                    traded_item = 0
                    continue
        else:
            traded_item = 0
        return traded_item

    def item_switch_hero_gives_to_trader(self, cycling, item, money, h):
        global sold_out_item
        if cycling == 1:
            while cycling == 1:
                if self.money >= h.backpack.get(item):
                    if item.upper() == 'NOTHING':
                        sold_out_item = 0
                        cycling = 0
                    else:
                        print


class Enemy(Character):
    def __init__(self):
        Character.__init__(self)
