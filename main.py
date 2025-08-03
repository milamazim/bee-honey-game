import pygame
from menu import Menu, GameOver
from game import Game

# classe principal do game
class Main:
    def __init__(self, sizex, sizey, title):
        # inicializa o pygsme
        pygame.init()
        # musica de fundo
        pygame.mixer.init()
        pygame.mixer.music.load('assets/sounds/bg.ogg')
        pygame.mixer.music.play(-1) # musica em loop
        # cria a janelinha do jogo com a start screen
        self.window = pygame.display.set_mode([sizex, sizey])
        pygame.display.set_caption(title)
        # cria as instancias das classes importadas
        self.start_screen = Menu('assets/start.png')
        self.game = Game()
        self.gameover = GameOver('assets/gameover.png')
        # inicia loop verdadeiro para permanecer com jogo aberto
        self.loop = True
        # controle do tick
        self.fps = pygame.time.Clock()

    # metodo que acessa os eventos
    def events(self):
        for event in pygame.event.get(): # percorre todos os eventos do jogo
            if event.type == pygame.QUIT: # evento para encerrar o jogo
                self.loop = False # finaliza loop que mantem o jogo aberto
            if not self.start_screen.change_scene: # permanece na tela do menu
                self.start_screen.event(event) # capta se esta sendo pressionado 'enter'
            elif not self.game.change_scene: # permanece na tela do jogo
                self.game.bee.move_bee(event) # capta o movimento do mouse da abelha
            else:
                self.gameover.event(event) # vai pra tela do game over

    # metodo que coloca os elementos na tela do jogo
    def draw(self):
        self.window.fill((0, 0, 0))
        if not self.start_screen.change_scene: # permanece na tela do menu
            self.start_screen.draw(self.window) # desenha a tela do menu
        elif not self.game.change_scene: # permanece na tela do jogo
            self.game.draw(self.window) # desenha a tela do jogo
            self.game.update() # atualiza os itens dinamicos do jogo
        elif not self.gameover.change_scene:
            self.gameover.draw(self.window) # tela de game over
        else:
            # reseta as variaveis para recomeçar o jogo
            self.start_screen.change_scene = False
            self.game.change_scene = False
            self.gameover.change_scene = False
            self.game.bee.life = 3
            self.game.bee.pts = 0

    # metodo que mantem o jogo rodando e atualizando a cada frame
    def updates(self):
        while self.loop: # loop que mantem o jogo ativo
            self.fps.tick(30) # 30 ticks = 1 segundo aprox.
            self.draw()
            self.events()
            pygame.display.update()

Main(360, 640, "Bee Honey").updates()
