import pyxel, random

class App():
    def __init__(self):
        pyxel.init(60, 60)
        self.score = 0
        self.sdir = "stop"
        self.death = False
        self.x = 0
        self.y = 0
        self.apx = random.randrange(0, 60)
        self.apy = random.randrange(0, 50)
        if self.apx == self.x and self.apy == self.y:
            self.apx = random.randrange(0, 60)
            self.apy = random.randrange(0, 60)
        pyxel.run(self.update, self.draw)
    def update(self):

        ####################
        ## Death Checking ##
        ####################
        if self.x > 60 or self.x < 0:
            self.death = True
        elif self.y > 50 or self.y < 0:
            self.death = True

        if self.death == True:
            print("You're dead UwU XD")
            quit()

        #######################
        ## Colition Checking ##
        #######################
        
        if self.apx == self.x and self.apy == self.y:
            self.score = +1
            self.apx = random.randrange(0, 60)
            self.apy = random.randrange(0, 50)
            if self.apx == self.x and self.apy == self.y:
                self.apx = random.randrange(0, 60)
                self.apy = random.randrange(0, 60)
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
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        
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

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.apx, self.apy, 2, 2, 8)
        pyxel.rect(self.x, self.y, 2, 2, 11)
        pyxel.rect(0, 50, 60, 20, 1)
        pyxel.text(5, 53, f"Score: {str(self.score)}", 0)

App()