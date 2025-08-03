import pygame

# classe para gerenciar os sprites do jogo
class Obj:
    def __init__(self, image, x, y):
        self.group = pygame.sprite.Group() # faz grupos de acordo com o tipo de sprite
        self.sprite = pygame.sprite.Sprite(self.group) # atribui o grupo aos sprites

        self.sprite.image = pygame.image.load(image) # carrega a imagem do sprite
        self.sprite.rect = self.sprite.image.get_rect() # pega as dimensoes do sprite
        self.sprite.rect[0] = x
        self.sprite.rect[1] = y

        self.frame = 1
        self.tick = 0

    def drawing(self, window):
        self.group.draw(window) # desenha os sprites na tela

    def anim(self, image, tick, frames):
        self.tick += 1 # adiciona novo tick

        if self.tick == tick: # reinicia a animacao de acordo com a qtd de ticks
            self.tick = 0
            self.frame += 1  # adiciona novo frame

        if self.frame == frames: # ao chegar no final reinicia os frames
            self.frame = 1
        # carrega img direto da pasta dos assets para mudar de uma pra outra
        self.sprite.image = pygame.image.load('assets/' + image + str(self.frame) + '.png')


class Bee(Obj): # herança da classe Obj
    def __init__(self, image, x, y):
        super().__init__(image, x, y) # necessita em casos de herança

        # sons para os eventos da abelha
        pygame.mixer.init()
        self.sound_pts = pygame.mixer.Sound('assets/sounds/score.ogg')
        self.sound_block = pygame.mixer.Sound('assets/sounds/bateu.ogg')

        # status iniciais
        self.life = 3
        self.pts = 0

    def move_bee(self, event):
        if event.type == pygame.MOUSEMOTION: # movimento da abelha é igual a movimentacoo do mouse
            self.sprite.rect[0] = pygame.mouse.get_pos()[0] - 35
            self.sprite.rect[1] = pygame.mouse.get_pos()[1] - 30

    def colision(self, group, name):
        name = name
        colision = pygame.sprite.spritecollide(self.sprite, group, True)
        if name == 'Flower' and colision:
            self.pts += 1
            self.sound_pts.play()
        elif name == 'Spider' and colision:
            self.life -= 1
            self.sound_block.play()


class Text:
    def __init__(self, size, text):
        self.font = pygame.font.SysFont('Arial bold', size)
        self.render = self.font.render(text, True, (255, 255, 255))

    def draw(self, window, x, y):
        window.blit(self.render, (x, y))

    def update_text(self,update):
        self.render = self.font.render(update, True, (255, 255, 255))