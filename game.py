from obj import Obj, Bee, Text
import random

class Game:
    def __init__(self):
        # cria 2 bgs para que fique uma transicao mais suave entre eles (bg infinito)
        self.bg = Obj('assets/bg.png',0,0)
        self.bg2 = Obj('assets/bg.png', 0, -640)
        # spawna aranha em local aleatorio
        self.spider = Obj('assets/spider1.png', random.randrange(0,300), -50)
        self.flower = Obj('assets/florwer1.png', random.randrange(0,300), -50)
        self.bee = Bee('assets/bee1.png', 150, 600) # declara obj do tipo Bee que herda Obj

        self.score = Text(160, str(self.bee.pts))
        self.lifes = Text(60, str(self.bee.life))

        self.change_scene = False

    def draw(self,window):
        # desenha na tela os Obj
        self.bg.drawing(window)
        self.bg2.drawing(window)
        self.bee.drawing(window)
        self.spider.drawing(window)
        self.flower.drawing(window)
        self.score.draw(window, 150,50)
        self.lifes.draw(window, 50, 50)

    def update(self):
        # movimentacao dos Obj
        self.move_bg()
        self.spider.anim('spider',8,5)
        self.flower.anim('florwer',8,3)
        self.bee.anim('bee',2,5)
        self.move_spiders()
        self.move_flower()
        self.bee.colision(self.spider.group, 'Spider')
        self.bee.colision(self.flower.group, 'Flower')
        self.gameover()
        self.score.update_text(str(self.bee.pts))
        self.lifes.update_text(str(self.bee.life))

    def move_bg(self):
        # adiciona +4 no sprite do bg para ele se mover na tela (desce)
        self.bg.sprite.rect[1] += 4
        self.bg2.sprite.rect[1] += 4

        # qndo ficar no tamanho da altura do bg, reinicia
        if self.bg.sprite.rect[1] >= 640:
            self.bg.sprite.rect[1] = 0

        if self.bg2.sprite.rect[1] >= 0:
            self.bg2.sprite.rect[1] = -640

    def move_spiders(self):
        self.spider.sprite.rect[1] += 10 # move a aranha para baixo
        if self.spider.sprite.rect[1] >= 700: # se saiu da tela na parte de baixo
            self.spider.sprite.kill() # elimina a aranha da tela
            # spawna outra aranha em local aleatorio
            self.spider = Obj('assets/spider1.png', random.randrange(0,300), -50)

    def move_flower(self):
        self.flower.sprite.rect[1] += 8 # move a flor para baixo
        if self.flower.sprite.rect[1] >= 640: # se saiu da tela na parte de baixo
            self.flower.sprite.kill() # elimina a flor da tela
            # spawna outra flor em local aleatorio
            self.flower = Obj('assets/florwer1.png', random.randrange(0,300), -100)

    def gameover(self):
        if self.bee.life <= 0:
            self.change_scene = True