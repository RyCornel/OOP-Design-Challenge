import pygame, sys, random
 

#Spacship Class
class Spaceship(pygame.sprite.Sprite):
    def __init__(self, path, x_pos, y_pos):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center = (x_pos, y_pos))
        self.shield_surface = pygame.image.load("shield.png")
        self.health = 5
        
    def update(self):
        self.rect.center = pygame.mouse.get_pos()
        self.screen_constrain()
        self.display_health()

    def screen_constrain(self):
        if self.rect.right >= 1280:
            self.rect.right = 1280
        if self.rect.left <=  0:
            self.rect.left = 0

    def display_health(self):
        for index,shield in enumerate(range(self.health)):
            screen.blit(self.shield_surface, (index * 40,10))

    def get_damage(self, damage_amount):
        self.health -= damage_amount

 
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

    
#Laser Class
class Laser(pygame.sprite.Sprite):
    def __init__(self, path, pos, speed):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center = pos)
        self.speed = speed

    def update(self):
        self.rect.centery -= self.speed
        
        #Despawn Lasers
        if self.rect.centery <= -100:
            self.kill()


#Health Class
class Health(pygame.sprite.Sprite):
    def __init__(self, path):
        super().__init__()
        self.shield_surface = pygame.image.load(path)
        self.health = 5

    def display_health(self):
        for index, shield in enumerate(range(self.health)):
            screen.blit(self.shield_surface, (10 + index * 40, 10))
    
    def get_damage(self, damage_amount):
        self.health -= damage_amount

    def update(self):
        self.display_health()


#Main Method for Game
def main_game():
    #Place Objects on Screen
    spaceship_group.draw(screen)
    meteor_group.draw(screen)
    laser_group.draw(screen)

    #Update Screen Objects
    spaceship_group.update()
    meteor_group.update()
    laser_group.update()
    

    #Check for Collisions
    if pygame.sprite.spritecollide(spaceship_group.sprite, meteor_group, True):
        spaceship_group.sprite.get_damage(1)
    
    #Check if Laser Hits Meteor 
    for laser in laser_group:
        pygame.sprite.spritecollide(laser, meteor_group, True)

    return 1

#Game Over Method
def end_game():
    text_surface = game_font.render("Game Over", True, (255, 255, 255))
    text_rect = text_surface.get_rect(center = (640, 320))
    screen.blit(text_surface, text_rect)

    score_surface = game_font.render(f"Your High Score Is: {score}", True, (255, 255, 255))
    score_rect = score_surface.get_rect(center = (640, 360))
    screen.blit(score_surface, score_rect)

#PyGame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
game_font = pygame.font.Font(None, 40)
score = 0

#Spaceship Group
spaceship = Spaceship("spaceship.png", 640, 500)
spaceship_group = pygame.sprite.GroupSingle()
spaceship_group.add(spaceship)

#Meteor Group
#meteor1 = Meteor("Meteor1.png", 400, -100, 1, 3)
meteor_group = pygame.sprite.Group()
#meteor_group.add(meteor1)

#Health Group
health_shield = Health("shield.png")
health_group = pygame.sprite.Group()
health_group.add(health_shield)


#Meteor Timer
meteor_event = pygame.USEREVENT
pygame.time.set_timer(meteor_event, 200)


#Laser Group
laser_group = pygame.sprite.Group()



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

        #Laser If Statement
        if event.type == pygame.MOUSEBUTTONDOWN:
            new_laser = Laser("Laser.png", event.pos, 20)
            laser_group.add(new_laser)

        #Reset If Satement
        if event.type == pygame.MOUSEBUTTONDOWN and spaceship_group.sprite.health <= 0:
            spaceship_group.sprite.health = 5
            meteor_group.empty()
            score = 0

        #if event.type == pygame.K_SPACE:
            #new_laser = Laser("Laser.png", event.pos, 20)
            #laser_group.add(new_laser)

    screen.fill((42, 45, 51))
    if spaceship_group.sprite.health > 0:
        score += main_game()
    else:
        end_game()
    
    pygame.display.update()
    clock.tick(120)