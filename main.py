import game_class as progress


def main():
    progress.Game.intro()
    gaming = 1
    while gaming == 1:
        answer = raw_input("Type [START] if you are ready and [QUIT] if you are not: ").upper()
        if answer not in "STARTQUIT":
            print "Unknown command"
            print "Try again!"
            continue
        gaming = progress.Game.start_quit(answer)
        if gaming == 0:
            break
        g = progress.Game()
        g.after_registration()
        g.choose_level()
        break


main()

"""h = Hero()
e = Enemy()
h.hero_backpack("Iron Sword")
h.level_up()
print h.backpack
print h.level"""
