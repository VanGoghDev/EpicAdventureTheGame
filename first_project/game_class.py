# coding=utf-8
import character


# coding=utf-8


class Game:
    h = character.Hero('', '')
    t = character.Trader
    goods = {}

    def __init__(self):
        self.level = 1

    def level_up(self, number):
        self.level *= number

    @staticmethod
    def intro():
        print 'Welcome to epic quest adventure!'
        print 'PreAlpha - version 0.1'
        print 'Are you ready to start?'

    @staticmethod
    def start_quit(answer):
        global h
        result = 1
        if answer == "START":
            print 'Nice! This means that you are going to start the best adventure'
            print 'In your whole life!'
            print 'What about your name?'
            print '[HINT] Type your name right here!'
            name = raw_input()
            print 'Hello, %s! Nice to see you!' % name
            print
            print 'And what about your age?'
            print '[WARNING] Yeah, your age is your age and you have full opportunity to choose one...'
            print 'Let`s think a little bit...'
            print 'If you are going to be too young, I think that you won`t have enough power to fight against monsters'
            print 'And if you are too old, it won`t be nice too'
            print '(press "enter" to continue...)'
            raw_input()
            print 'C`mon, choose your age!'
            print 'Adults are from 18 years, the strongest age is 25-34 ' \
                  'and you are going to be a grandparent starting at the age of 50'
            cycle = 1
            while cycle == 1:
                age = raw_input()
                if age == '' or age not in "11223344556677889900":
                    print 'Try again'
                    continue
                elif 24 >= int(age) >= 5 or 60 > int(age) >= 35:
                    print 'Hmm, kids should be more careful'
                    print 'But you are not to young, maybe you will achieve something at early age'
                    print 'Your difficulty is [normal]'
                    h = character.Hero(name, age)  # Hero creates here!!!!!!!!!
                    h.level_up(0)
                    cycle = 0
                elif 34 >= int(age) >= 25:
                    print 'Yeah! That is what we need!'
                    print 'Nice age! Full of power and will'
                    print 'Your difficulty is [easy]'
                    h = character.Hero(name, age)  # Hero creates here!!!!!!!!!
                    h.level_up(1)
                    cycle = 0
                elif int(age) >= 60 or int(age) <= 5:
                    print 'You are crazy person!'
                    print 'It`s gonna be hard to finish this quest at this age'
                    print 'Your difficulty is [hardcore]'
                    h = character.Hero(name, age)  # Hero creates here!!!!!!!!!
                    h.level_up(-0.75)
                    cycle = 0
                else:
                    print 'It`s gonna be challenging'
                    print 'but don`t give up!'
                    print 'Your difficulty is [hard]'
                    h = character.Hero(name, age)  # Hero creates here!!!!!!!!!
                    h.level_up(-0.5)
                    cycle = 0
            result = 1
        elif answer == "QUIT":
            print 'See you soon!'
            result = 0
        return result

    # статические методы можно будет поменять на активные
    # например если нужно передать уровню какое-либо значение необходимое
    # например если игрок что-нибудь такое сделал в предыдущем уровне, что здесь это повлияет на геймплей

    def after_registration(self):
        print 'Now you can choose a level:'
        print "If you want to play a new game type [New Game]: "
        print "If you want to choose a level type a number of level: "
        cycling = 1
        while cycling == 1:
            new_game = raw_input().upper()
            if new_game == '2':
                self.level += 1
                cycling = 0
            elif new_game == '3':
                self.level += 2
                cycling = 0
            elif new_game == 'New Game' or new_game == '1':
                self.level = 1
                cycling = 0
            elif new_game not in 'NEW GAME123':
                print 'There is no level called %s' % new_game
                continue

    @staticmethod
    def level_one():
        global goods
        print 'Welcome to the very first epic adventure of your life!'
        print
        print 'You are an adventurer who is looking for new experience'
        print 'Such as fights, tasty food, new places, castles and maybe for some princess? Ugh'
        print '(press "enter" to continue...)'
        raw_input()
        print 'You are living in the land far away and many years you were dreaming'
        print 'about new lands and of course adventures!'
        print 'But this planet is full of dangerous creatures'
        print 'That`s why you were waiting for the right moment'
        print '(press "enter" to continue...)'
        raw_input()
        print 'This moment is finally here!'
        print '%s, you are entering a new interesting world' % h.name
        print 'at the age of %s you will need a good equipment...' % h.age
        raw_input()
        print 'you can find some equipment at markets or buy from seller'
        raw_input()
        print 'Charlie and Eddie offers a nice weapons and some other interesting stuff...'
        raw_input()
        print 'But be careful! You can choose only one of them'
        print 'You will need some money'
        print 'You can take this for the first time:'
        print '200$ added'
        h.money = 200
        print 'Press left (A) for Charlie or right (D) for Eddie'
        cycle = 1
        while cycle == 1:
            action = raw_input().upper()
            if action not in "AD":
                print 'unknown command, type again'
                cycle = 1
                continue
            elif action == 'A':
                print 'Your choice is Charlie!'
                goods = {'sword': 300, 'excellent robe': 100, 'map': 50}
                cycle = 0
            elif action == 'D':
                print 'Your choice is Eddie!'
                goods = {'bow with arrows': 175, 'fresh fruits': 25, 'guide to the galaxy': 200, 'key from the secret '
                                                                                                 'dungeon': 200}
                cycle = 0
        t = character.Trader()
        t.backpack_upgrade(**goods)
        print
        trading(t, h)

    @staticmethod
    def level_two():
        print 'Second level starts right here!'

    @staticmethod
    def level_three():
        print 'Congratulations! You reached third level!'
        print h.level

    def choose_level(self):
        if self.level == 1:
            h.level_up(1)
            Game.level_one()
        elif self.level == 2:
            h.level_up(2)
            Game.level_two()
        elif self.level == 3:
            h.level_up(3)
            Game.level_three()


def trading(trader, hero):
    cycling = 1
    while cycling == 1:
        print 'Do you want to [SELL] or to [BUY]?'
        print '[QUIT] when you are ready to continue your journey'
        choice = raw_input().upper()
        if choice not in 'SELLBUY':
            print 'Unknown command, try again'
            continue
        elif choice == 'BUY':
            buy(trader, hero)
            continue
        elif choice == 'SELL':
            sell(trader, hero)
            continue
        elif choice == 'QUIT':
            cycling = 0


def buy(trader, hero):
    print 'Trader has %s$' % trader.money
    print 'These are some items that trader sales:'
    print trader.backpack
    cycling = 1
    while cycling == 1:
        print 'Choose what you want to buy!'
        print 'If you don`t need anything print "NOTHING"'
        choice = raw_input().upper()
        if choice == 'NOTHING':
            trader.item_switch_trader_gives_to_hero(0, 0, hero.money, hero)
            cycling = 0
        else:
            traded_item = trader.item_switch_trader_gives_to_hero(1, choice.lower(), hero.money, hero)
            hero.money -= traded_item
            trader.money += traded_item
            print 'traders backpack: %s' % trader.backpack
            print 'heroes backpack: %s' % hero.backpack
            print 'your current money: %s' % hero.money


def sell(trader, hero):
    print
    print 'Trader has %s$' % trader.money
    print 'Your items in your backpack:'
    print hero.backpack
    cycling = 1
    while cycling == 1:
        print 'Choose what to sell'
        print 'If you are ready press [QUIT]'
        choice = raw_input().upper()
        if choice == 'QUIT':
            trader.item_switch_hero_gives_to_trader(0, 0, hero.money, hero)
            cycling = 0
        else:
            sold_out_item = trader.item_switch_hero_gives_to_trader(1, choice.lower(), hero.money, hero)
            hero.money += sold_out_item
            trader.money -= sold_out_item
            print 'traders backpack: %s' % trader.backpack
            print 'heroes backpack: %s' % hero.backpack
            print 'your current money: %s' % hero.money
