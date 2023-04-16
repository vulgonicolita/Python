import pygame
pygame.init() '''inicio do pygame que é um módulo muito usado para jogos'''
'''o pygame pode carregar imagens e tudo. aqui estamos vendo o uso do das músicas'''
pygame.mixer.music.load(ex021.mp3)
pygame.mixer.music.play()
pygame.event.wait()