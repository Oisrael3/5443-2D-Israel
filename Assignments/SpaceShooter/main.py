import pygame
import random
import math
from pygame.locals import *
import pygame.mixer
# Font initialization
pygame.font.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# Set the screen dimensions
screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode([screen_width, screen_height])
font = pygame.font.SysFont("Arial", 24, "bold")

#used for the caption and icon
pygame.display.set_caption("Izzy and Byron space game")

#Score
score_val = 0
scoreX = 5
scoreY = 5
font = pygame.font.SysFont("Arial", 24, "bold")

#Game Over
game_over_font = pygame.font.SysFont('Arial', 64, )

def show_score(x,y):
    score = font.render("Points: " + str(score_val),
                        True, (255,255,255))
    screen.blit(score, (x , y))
    
def game_over():
    game_over_text = game_over_font.render("GAME OVER",
                                           True, (255,255,255))
    screen.blit(game_over_text, (190, 250))
#background musicp
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("Griffin SpaceBattle/space_rocks/cinematic-atmosphere-score-2-22136.wav")
pygame.mixer.music.set_volume(.1)
#pygame.mixer.music.fadein(5000)
pygame.mixer.music.play(-1)

#used to wait for the music to finish
#while pygame.mixer.music.get_busy():
    #pass
#pygame.mixer.music.stop()
#pygame.mixer.quit()

#load game images
background = pygame.image.load("Griffin SpaceBattle/space_rocks/space bg.png").convert_alpha()
healthasteroid = pygame.image.load("Griffin SpaceBattle/space_rocks/asteroid.png").convert_alpha()
logo = pygame.image.load("Griffin SpaceBattle/space_rocks/gamelogo.png").convert_alpha()
shipimage = pygame.image.load("Griffin SpaceBattle/space_rocks/rocketship.png").convert_alpha()
laser = pygame.image.load("Griffin SpaceBattle/space_rocks/beams1.png").convert_alpha()
# Change the size of the missile
laser = pygame.transform.scale(laser, (35, 35))
pygame.display.set_icon(logo)



# Define the player class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = shipimage
        self.rect = self.image.get_rect()
        self.direction = 0
        self.health = 1000
        self.score = 0
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = screen_width / 2
        self.y = screen_height / 2
        self.turn = pygame.transform.rotate(self.image, self.direction)
        self.turnRect = self.turn.get_rect()
        self.turnRect.center = (self.x, self.y)

        # Find the direction the player is facing
        self.sin = math.sin(math.radians((self.direction + 90)))
        self.cosine = math.cos(math.radians(self.direction + 90))
        self.point = (self.x + self.cosine * self.width / 2, self.y + self.sin * self.height / 2)

    def drawSprite(self, screen):
        screen.blit(self.turn, self.turnRect)


    def leftTurn(self):
        self.direction += 5
        self.turn = pygame.transform.rotate(self.image, self.direction)
        self.turnRect = self.turn.get_rect()
        self.turnRect.center = (self.x, self.y)
        self.sin = math.sin(math.radians(self.direction + 90))
        self.cosine = math.cos(math.radians(self.direction + 90))
        self.point = (self.x + self.cosine * self.width / 2, self.y - self.sin * self.height / 2)

    def rightTurn(self):
        self.direction -= 5
        self.turn = pygame.transform.rotate(self.image, self.direction)
        self.turnRect = self.turn.get_rect()
        self.turnRect.center = (self.x, self.y)
        self.sin = math.sin(math.radians(self.direction + 90))
        self.cosine = math.cos(math.radians(self.direction + 90))
        self.point = (self.x + self.cosine * self.width / 2, self.y - self.sin * self.height / 2)
        
    def down(self):
        self.direction += 5
        self.turn = pygame.transform.rotate(self.image, self.direction)
        self.turnRect = self.turn.get_rect()
        self.turnRect.center = (self.x, self.y)
        self.sin = math.sin(math.radians(self.direction + 90))
        self.cosine = math.cos(math.radians(self.direction + 90))
        self.point = (self.x + self.cosine * self.width / 2, self.y - self.sin * self.height / 2)

    def thrust(self):
        self.x += self.cosine * 6
        self.y -= self.sin * 6
        self.turn = pygame.transform.rotate(self.image, self.direction)
        self.turnRect = self.turn.get_rect()
        self.turnRect.center = (self.x, self.y)
        self.sin = math.sin(math.radians(self.direction + 90))
        self.cosine = math.cos(math.radians(self.direction + 90))
        self.point = (self.x + self.cosine * self.width / 2, self.y - self.sin * self.height / 2)


# Define the projectile class
class Missile:
    def __init__(self):
        self.image = laser
        self.gun = player.point
        self.x, self.y = self.gun

        # Follows sin and cos of player to determine missile direction
        self.s = player.sin
        self.c = player.cosine

        # Fires missile in the direction player is pointing
        self.velocity_x = self.c * 10
        self.velocity_y = self.s * 10

    def move(self):
        # Calculate the new position based on angle and speed
        self.x += self.velocity_x
        self.y -= self.velocity_y

    def draw(self, screen):
        # Draw the missile on the screen
        screen.blit(laser, (self.x, self.y))

# Define the asteroid class
class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = healthasteroid
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 1000)
        self.rect.y = random.randrange(-100, -50)

    def update(self):
        # Move the asteroid down the screen
        self.rect.y += 3
        if self.rect.y > 600:
            self.rect.x = random.randrange(0, 1)
            self.rect.y = random.randrange(-1, 1)

# Initialize Pygame
pygame.init()

# Create a group of sprites
spritesGroup = pygame.sprite.Group()

# Create the player sprite
player = Player(325, 350)

# Creates a list of missiles
missiles = []


# Create a group of asteroids
asteroid_list = pygame.sprite.Group()
for i in range(10):
    asteroids = Asteroid()
    asteroid_list.add(asteroids)
    spritesGroup.add(asteroids)

# Set the game caption
pygame.display.set_caption("Asteroid Shooter")

# Set the game clock
clock = pygame.time.Clock()

# Displays player score
def score():
    img = font.render(f"Score: {player.score}", True, BLACK)
    screen.blit(img, (1000, 10))

# Displays player health
def health():
    hlth = font.render(f"Health: {player.health}", True, BLACK)
    screen.blit(hlth, (10, 10))

def gameScreen():
    player.drawSprite(screen)
    for m in missiles:
        m.draw(screen)
    pygame.display.update()


# Main game loop
game_over = False
while not game_over:
    gameScreen()

    for m in missiles:
        m.move()
    # Move the player based on input from the keyboard
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.leftTurn()
    if keys[pygame.K_RIGHT]:
        player.rightTurn()
    if keys[pygame.K_UP]:
        player.thrust()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                missiles.append(Missile())
    # Set the game clock
    clock.tick(60)


    # Update asteroid group
    spritesGroup.update()

    # Check for collisions between the player and asteroids
    asteroid_hit_list = pygame.sprite.spritecollide(player, asteroid_list, True)
    for asteroid in asteroid_hit_list:
        asteroid.kill()
        # Player health increases each time a health asteroid is hit
        player.health += 10

        print("Asteroid hit")

    screen.fill(BLACK)

    # Draw asteroid sprites
    spritesGroup.draw(screen)

    score()
    health()
    # Update the screen
    #screen.blit(background, (700,300))
    pygame.display.flip()



# Quit Pygame
pygame.quit()
