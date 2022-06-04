# Faça um programa de python que abra e reproduza o áudio de um arquivo MP3.

import pygame
pygame.init()
pygame.mixer.music.load('C:/Users/lucas/Desktop/ex021(b).mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
