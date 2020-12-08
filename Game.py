import pygame, sys, random
 #Spacship Class
class Spaceship(pygame.sprite.Sprite):
    def __init__(self, path, x_pos, y_pos, speed):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center = (x_pos, y_pos))

    def update(self):
        self.rect.center = pygame.mouse.get_pos()
        self.screen_constrain()

    def screen_constrain(self):
        if self.rect.right >= 1280:
            self.rect.right = 1280
        if self.rect.left <=  0:
            self.rect.left = 0
    

#Meteor Class
class Meteor(pygame.sprite.Sprite):
    def __init__(self, path, x_pos, y_pos, x_speed, y_speed):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center = (x_pos, y_pos))
        self.x_speed = x_speed
        self.y_speed = y_speed

    def update(self):
        self.rect.centerx += self.x_speed
        self.rect.centery += self.y_speed
        
        #Despawn Meteors
        if self.rect.centery >= 800:
            self.kill()

    def screen_constrain(self):
        if self.rect.right >= 1280:
            self.rect.right = 1280
        if self.rect.left <=  0:
            self.rect.left = 0

    



pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

spaceship = Spaceship("spaceship.png", 640, 500, 10)
spaceship_group = pygame.sprite.GroupSingle()
spaceship_group.add(spaceship)

#meteor1 = Meteor("Meteor1.png", 400, -100, 1, 3)
meteor_group = pygame.sprite.Group()
#meteor_group.add(meteor1)

#Meteor Timer
meteor_event = pygame.USEREVENT
pygame.time.set_timer(meteor_event, 200)


#While Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == meteor_event:
            meteor_path = random.choice(("Meteor1.png", "Meteor2.png", "Meteor3.png"))
            random_x_pos = random.randrange(0, 1280)
            random_y_pos = random.randrange(-500, -50)
            random_x_speed = random.randrange(-1, 1)
            random_y_speed = random.randrange( 4, 10)
            meteor = Meteor(meteor_path, random_x_pos, random_y_pos, random_x_speed, random_y_speed)
            meteor_group.add(meteor)

    screen.fill((42, 45, 51))
    spaceship_group.draw(screen)
    meteor_group.draw(screen)
    spaceship_group.update()
    meteor_group.update()
    pygame.display.update()
    clock.tick(120)