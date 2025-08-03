import pygame
from obj import Obj

class Menu:
    def __init__(self, image):
        self.bg = Obj(image,0,0) # instancia o bg do inicio do jogo
        self.change_scene = False

    def draw(self, window):
        self.bg.group.draw(window) # desenha na tela o bg informado

    def event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN: # ao pressionar Enter entra no jogo
                self.change_scene = True

class GameOver(Menu):
    def __init__(self, image):
        super().__init__(image)


