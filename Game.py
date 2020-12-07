import pygame, sys
 
class Spaceship(pygame.sprite.Sprite):
    def __init__(self, path, x_pos, y_pos, speed):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center = (x_pos, y_pos))

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

spaceship = Spaceship("spaceship.png", 640, 500, 10)
spaceship_group = pygame.sprite.GroupSingle()
spaceship_group.add(spaceship)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((42, 45))
    spaceship_group.draw(screen)
    pygame.display.update()
    clock.tick(120)