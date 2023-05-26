import pyxel, random, argparse

version = 1.1

parser = argparse.ArgumentParser(
    prog="PySnake v1.1",
    description="Snake rewritten in Python",
    add_help=False
)
parser.add_argument('-v', "--version", help="Prints the version", action='store_true')
parser.add_argument('-h', "--help", help="Prints out this help", action='store_true')
args = parser.parse_args()

if args.help:
    f = open("assets/help.txt", 'r')
    contents = f.read()
    print(f"\n{contents}\n")
    f.close()
    quit()
elif args.version:
    print(f"\nPySnake Version: v{version}\n")
    quit()

class App():
    def __init__(self):
        pyxel.init(60, 60, title="PySnake", fps=20)
        self.menu = True
        self.restart = False
        self.funnymsg = 1000
        self.tail = []
        self.score = 0
        self.sdir = "stop"
        self.death = False
        self.x = 0
        self.y = 0
        self.apx = random.randrange(0, 57)
        self.apy = random.randrange(0, 48)
        self.dreason = ""
        self.normal = False
        self.unlimited = False
        if self.apx == self.x and self.apy == self.y:
            self.apx = random.randrange(0, 57)
            self.apy = random.randrange(0, 48)

        pyxel.load("assets/music.pyxres", image=False)
        #pyxel.image(0).load(0, 0, "snake_background.png")
        #pyxel.play(0, [0, 1],loop=True)
        #pyxel.play(1, [1, 2],loop=True)
        #pyxel.play(2, [2, 3],loop=True)
        #pyxel.play(3, [3, 4],loop=True)
        pyxel.playm(0, loop=True)
        pyxel.run(self.update, self.draw)
    def update(self):

        # Controls that should not be disabled at death:
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        elif pyxel.btnp(pyxel.KEY_R) and not self.menu:
            self.restart = True
        
        if self.menu:
            if pyxel.btnp(pyxel.KEY_N):
                self.normal = True
                self.menu = False
            elif pyxel.btnp(pyxel.KEY_U):
                self.unlimited = True
                self.menu = False

        # Restart script
        if self.restart:
            pyxel.stop()
            pyxel.playm(0, loop=True)
            self.x = 0
            self.y = 0
            self.death = False
            self.tail = []
            self.restart = False
            self.score = 0
            self.sdir = "stop"
            self.apx = random.randrange(0, 57)
            self.apy = random.randrange(0, 48)
            if self.apx == self.x and self.apy == self.y:
                self.apx = random.randrange(0, 57)
                self.apy = random.randrange(0, 48)
        if not self.death and not self.menu:
            #######################
            ## Colition Checking ##
            #######################
            
            if (self.x < self.apx + 2 and self.x + 2 > self.apx and
            self.y < self.apy + 2 and self.y + 2 > self.apy):
                self.score += 1
                self.apx = random.randrange(0, 57)
                self.apy = random.randrange(0, 48)
                while self.apx == self.x and self.apy == self.y:
                    self.apx = random.randrange(0, 57)
                    self.apy = random.randrange(0, 48)
            
            # Check if snake collides with itself
            if len(self.tail) > 1:
                for i in range(1, len(self.tail)):
                    if self.x == self.tail[i][0] and self.y == self.tail[i][1]:
                        if not self.death:
                            self.funnymsg = random.randrange(0, 10)
                            pyxel.stop()
                            #pyxel.playm(1, loop=True)
                            pyxel.play(0, 15)
                            if self.funnymsg == 5:
                                self.dreason = "Snails."
                            else:
                                self.dreason = "You ate your own tail!"
                        self.death = True
                        break


            ################
            ## Main Snake ##
            ################

            if pyxel.btn(pyxel.KEY_RIGHT):
                if not self.sdir == "left":
                    self.sdir = "right"
            elif pyxel.btn(pyxel.KEY_LEFT):
                if not self.sdir == "right":
                    self.sdir = "left"
            elif pyxel.btn(pyxel.KEY_DOWN):
                if not self.sdir == "up":
                    self.sdir = "down"
            elif pyxel.btn(pyxel.KEY_UP):
                if not self.sdir == "down":
                    self.sdir = "up"
            if self.normal:
                if self.sdir == "right":
                    self.x = (self.x + 1)
                elif self.sdir == "left":
                    self.x = (self.x - 1)
                elif self.sdir == "down":
                    self.y = (self.y + 1)
                elif self.sdir == "up":
                    self.y = (self.y - 1)
                elif self.sdir == "stop":
                    pass
            elif self.unlimited:
                if self.sdir == "right":
                    self.x = (self.x + 1) % pyxel.width
                elif self.sdir == "left":
                    self.x = (self.x - 1) % pyxel.width
                elif self.sdir == "down":
                    self.y = (self.y + 1) % 50
                elif self.sdir == "up":
                    self.y = (self.y - 1) % 50
                elif self.sdir == "stop":
                    pass

            # Tail
            self.tail.insert(0, (self.x, self.y))
            if len(self.tail) > self.score:
                self.tail.pop()

            ####################
            ## Death Checking ##
            ####################
            if self.normal:
                if self.x > 60 or self.x < 0:
                    if not self.death:
                        self.funnymsg = random.randrange(0, 10)
                        pyxel.stop()
                        #pyxel.playm(1, loop=True)
                        pyxel.play(0, 15)
                        if self.funnymsg == 5:
                            self.dreason = "Snails."
                        else:
                            self.dreason = "You hit a wall"
                    self.death = True
                elif self.y > 49 or self.y < 0:
                    if not self.death:
                        self.funnymsg = random.randrange(0, 10)
                        pyxel.stop()
                        #pyxel.playm(1, loop=True)
                        pyxel.play(0, 15)
                        if self.funnymsg == 5:
                            self.dreason = "Snails."
                        else:
                            self.dreason = "You hit a wall"
                    self.death = True

        

    def draw(self):
        if not self.death and not self.menu:
            pyxel.cls(0)
            #pyxel.blt(0, 0, 0, 0, 0, 60, 60)
            pyxel.rect(self.apx, self.apy, 2, 2, 8)
            for i, (tx, ty) in enumerate(self.tail):
                pyxel.rect(tx, ty, 2, 2, 11)
            pyxel.rect(self.x, self.y, 2, 2, 11)
            pyxel.rect(0, 50, 60, 20, 1)
            pyxel.text(5, 53, f"Score: {str(self.score)}", 0)
        elif self.death and not self.menu:
            pyxel.cls(8)
            pyxel.text(17, 5, "[Q]uit", 5)
            if self.dreason == "You ate your own tail!":
                pyxel.text(7, 10, "You ate your", 1)
                pyxel.text(12, 18, "own tail!", 1)
            else:
                pyxel.text(2, 20, f"{self.dreason}", 1)
            pyxel.text(2, 30, "Your score was", 1)
            pyxel.text((30 - ((2 * len(str(self.score))) - 1)), 40, f"{str(self.score)}", 3)
            pyxel.text(10, 50, "[R]estart", 5)
        
        if self.menu:
            pyxel.cls(1)
            pyxel.text(3, 1, "SPAMIXOFFICIAL", 5)
            pyxel.text(3, 0, "SPAMIXOFFICIAL", 9)
            pyxel.text(16, 10, "PySnake", 5)
            pyxel.text(16, 9, "PySnake", 9)
            pyxel.text(22, 21, "v1.0", 5)
            pyxel.text(22, 20, "v1.0", 10)
            
            pyxel.text(34, 50, "[U]", 9)
            pyxel.text(14, 50, "[N]", 9)
            # Icons and coices
            # Squares
            pyxel.rectb(15, 35, 10, 10, 9)
            pyxel.rectb(35, 35, 10, 10, 9)

            # Normal Icon
            pyxel.rect(17, 37, 2, 2, 9)
            pyxel.rect(21, 37, 2, 2, 9)
            pyxel.rect(17, 41, 1, 1, 9)
            pyxel.rect(22, 41, 1, 1, 9)
            pyxel.rect(17, 42, 6, 1, 9)

            # Unlimited icon
            pyxel.rect(36, 39, 1, 2, 9)
            pyxel.rect(37, 38, 2, 1, 9)
            pyxel.rect(37, 41, 2, 1, 9)
            pyxel.rect(39, 39, 2, 2, 9)
            pyxel.rect(41, 38, 2, 1, 9)
            pyxel.rect(41, 41, 2, 1, 9)
            pyxel.rect(43, 39, 1, 2, 9)

App()