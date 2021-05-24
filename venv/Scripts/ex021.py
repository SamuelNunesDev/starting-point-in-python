import pygame

pygame.init()
pygame.mixer.music.load('flamingos.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(1)
clock = pygame.time.Clock()
clock.tick(10)
while pygame.mixer.music.get_busy():
        pygame.event.poll()
        clock.tick(10)
