class Enemy:
    life = 3

    def __init__(self, x):
        print("RAWWWRRR!!! " + str(x))

    def attack(self):
        print("ouch!")
        self.life -= 1

    def checkLife(self):
        if self.life <= 0:
            print("I am dead!")
        else:
            print(str(self.life) + " life left")

enemy1 = Enemy(2)
enemy2 = Enemy(4)

enemy1.attack()
enemy1.checkLife()
enemy2.checkLife()