"""
    Author:   Byron Dowling, Leslie Cook, Izzy Olaemimimo
    Class:    5443 2D Python Gaming

    Asset Credits:

        Knight Sprites:
            - Author: [Free Game Assets]
            - https://free-game-assets.itch.io/free-2d-knight-sprite-sheets

        Background Art:
            - Author: ["klyaksun"]
            - https://www.vecteezy.com/vector-art/15370321-ancient-roman-arena-for-gladiators-fight
            - https://www.vecteezy.com/vector-art/13852032-ancient-roman-arena-for-gladiators-fight-at-night

"""

import pygame
import pprint
import copy
import os
from PlayerSelection import PlayerSelector
from PIL import Image, ImageDraw
import utilities


###################################################################################################
"""
 ██████╗  █████╗  ██████╗██╗  ██╗ ██████╗ ██████╗  ██████╗ ██╗   ██╗███╗   ██╗██████╗ 
 ██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝ ██╔══██╗██╔═══██╗██║   ██║████╗  ██║██╔══██╗
 ██████╔╝███████║██║     █████╔╝ ██║  ███╗██████╔╝██║   ██║██║   ██║██╔██╗ ██║██║  ██║
 ██╔══██╗██╔══██║██║     ██╔═██╗ ██║   ██║██╔══██╗██║   ██║██║   ██║██║╚██╗██║██║  ██║
 ██████╔╝██║  ██║╚██████╗██║  ██╗╚██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║██████╔╝
 ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═════╝ 
                                                                                      
 ██╗███╗   ███╗ █████╗  ██████╗ ███████╗██████╗ ██╗   ██╗                             
 ██║████╗ ████║██╔══██╗██╔════╝ ██╔════╝██╔══██╗╚██╗ ██╔╝                             
 ██║██╔████╔██║███████║██║  ███╗█████╗  ██████╔╝ ╚████╔╝                              
 ██║██║╚██╔╝██║██╔══██║██║   ██║██╔══╝  ██╔══██╗  ╚██╔╝                               
 ██║██║ ╚═╝ ██║██║  ██║╚██████╔╝███████╗██║  ██║   ██║                                
 ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝                                                                                                          
"""
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location, size):

        pygame.sprite.Sprite.__init__(self)
        self.width, self.height = self.getImgWidthHeight(image_file)
        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.scale(self.image, size)

        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

    def getImgWidthHeight(self, path):
        """Uses pil to image size in pixels.
        Params:
            path (string) : path to the image
        """
        if os.path.isfile(path):
            im = Image.open(path)
            return im.size
        return None

###################################################################################################
"""
  ██████╗  █████╗ ███╗   ███╗███████╗        
 ██╔════╝ ██╔══██╗████╗ ████║██╔════╝        
 ██║  ███╗███████║██╔████╔██║█████╗          
 ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝          
 ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗        
  ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝        
                                             
 ███████╗██████╗ ██████╗ ██╗████████╗███████╗
 ██╔════╝██╔══██╗██╔══██╗██║╚══██╔══╝██╔════╝
 ███████╗██████╔╝██████╔╝██║   ██║   █████╗  
 ╚════██║██╔═══╝ ██╔══██╗██║   ██║   ██╔══╝  
 ███████║██║     ██║  ██║██║   ██║   ███████╗
 ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝   ╚═╝   ╚══════╝

"""
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, imgLink, location, smsc_dimensions, inverted=False):
        self.playerMain = pygame.sprite.Sprite()
        self.location = location
        self.playerMain.image = self.__makeImage(imgLink, smsc_dimensions, inverted)
        self.playerMain.rect = self.playerMain.image.get_rect(center = location)
        self.playerMain.mask = pygame.mask.from_surface(self.playerMain.image)
        
    def draw(self):
        screen.blit(self.playerMain.image, self.playerMain.rect.topleft)
        
    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y
        
    def changeImage(self, imgLink, smsc_dimensions, inverted=False):
        self.playerMain.image = self.__makeImage(imgLink, smsc_dimensions, inverted)
        
    def __makeImage(self, imgLink, smsc_dimensions, inverted=False):
        if not inverted:
            image = pygame.image.load(imgLink)
            image = pygame.transform.smoothscale(image, smsc_dimensions)

        ## Inverted case where the Sprite is facing left
        else:
            image = pygame.image.load(imgLink)
            image = pygame.transform.smoothscale(image, smsc_dimensions)
            image_Copy = image.copy()
            image = pygame.transform.flip(image_Copy, True, False)
            
        return image

###################################################################################################
"""
 ██████╗ ██╗      █████╗ ██╗   ██╗███████╗██████╗ 
 ██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗
 ██████╔╝██║     ███████║ ╚████╔╝ █████╗  ██████╔╝
 ██╔═══╝ ██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗
 ██║     ███████╗██║  ██║   ██║   ███████╗██║  ██║
 ╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝                        
"""
class Player:
    def __init__(self, SP, P):
        self.StartingPosition = SP
        self.spriteObject = P
        self.player_X = SP[0]
        self.player_Y = SP[1]
        self.Crouching = False
        self.Standing = True
        self.Jumping = False
        self.Descending = False
        self.Projectile = False
        self.Moving = False
        self.Hurt = False
        self.Dead = False
        self.Attacking = False
        self.Weapon = False
        self.Jump_Height = 0
        self.idle_frameCount = P["Action"]["Idle"]["frameCount"]
        self.jump_frameCount = P["Action"]["Jump"]["frameCount"]
        self.death_frameCount = P["Action"]["Die"]["frameCount"]
        self.move_frameCount = P["Action"]["Move"]["frameCount"]
        self.hurt_frameCount = P["Action"]["Hurt"]["frameCount"]
        self.attack_frameCount = P["Action"]["Attack"]["frameCount"]
        self.weapon_frameCount = P["Action"]["Weapon"]["frameCount"]
        self.blood_frameCount = P["Action"]["Blood"]["frameCount"]
        self.bloodSplat_frameCount = P["Action"]["bloodSplatter"]["frameCount"]
        self.idle_frame = 0
        self.jump_frame = 0
        self.death_frame = 0
        self.move_frame = 0
        self.hurt_frame = 0
        self.attack_frame = 0
        self.weapon_frame = 0
        self.blood_frame = 0
        self.name = P["Screen Name"]

    ## When the player has been killed
    def playerDeathAnimation(self,AOFDSS,Inverted=False):
        if self.Dead == True:
            P_link = f'{self.spriteObject["Action"]["Die"]["imagePath"]}/{self.death_frame}.png'
            Player = GameSprite(P_link, 
                                (self.player_X, self.player_Y), AOFDSS, Inverted)
            P_blood = f'{self.spriteObject["Action"]["Blood"]["imagePath"]}/{self.blood_frame}.png'
            Player_blood = GameSprite(P_blood, 
                                (self.player_X, self.player_Y), AOFDSS, Inverted)
            Player_blood.draw()
            Player.draw()
           
            if self.death_frame < self.death_frameCount - 1:
                self.death_frame += 1

            ## Had to add this so that if you get killed mid-air, gravity still occurs
            ## otherwise the Sprite lays dead floating in mid-air
            if self.Jump_Height > 0:
                self.Jump_Height -= 10
                self.player_Y += 10
    
    ## Handling whether the Player is Standing or the Player is Moving
    def movePlayer(self,AOFDSS,Inverted=False,AOFVS=15,AOFJH=150,AOFPS=10):
        if self.Dead == False:
            if self.Attacking == True:
                P_link = f'{self.spriteObject["Action"]["Attack"]["imagePath"]}/{self.attack_frame}.png'
                Player = GameSprite(P_link, 
                                (self.player_X, self.player_Y), AOFDSS, Inverted)
                if self.attack_frame < self.attack_frameCount - 1:
                    self.attack_frame += 1
                else:
                    self.attack_frame = 0
                    self.Attacking = False

            if self.Hurt == True:
                P_link = f'{self.spriteObject["Action"]["Hurt"]["imagePath"]}/{self.hurt_frame}.png'
                Player = GameSprite(P_link, 
                                (self.player_X, self.player_Y), AOFDSS, Inverted)

                if self.hurt_frame < self.hurt_frameCount - 1:
                    self.hurt_frame += 1
                    
                else:
                    self.hurt_frame = 0
                    self.Hurt = False

            ## We want Standing/Idle to be lowest in order of importance, therefore it only
            ## animates idle standing if the sprite isn't attacking or taking damage
            if self.Standing == True and self.Attacking == False and self.Hurt == False:
                if self.Moving == False:
                    P_link = f'{self.spriteObject["Action"]["Idle"]["imagePath"]}/{self.idle_frame}.png'
                    Player = GameSprite(P_link, 
                                        (self.player_X, self.player_Y), AOFDSS, Inverted)
                else:
                    P_link = f'{self.spriteObject["Action"]["Move"]["imagePath"]}/{self.move_frame}.png'
                    Player = GameSprite(P_link, 
                                        (self.player_X, self.player_Y), AOFDSS, Inverted)
                    if self.move_frame < self.move_frameCount - 1:
                        self.move_frame += 1
                    else:
                        self.move_frame = 0
                self.Moving = False

            if self.Jumping == True:
                P_link = f'{self.spriteObject["Action"]["Jump"]["imagePath"]}/{self.jump_frame}.png'
                Player = GameSprite(P_link, 
                                (self.player_X, self.player_Y), AOFDSS, Inverted)
                if self.Descending == False:
                    if self.jump_frame < self.jump_frameCount -1:
                        self.jump_frame += 1
                    self.player_Y -= AOFVS
                    self.Jump_Height += AOFVS

                    if self.Jump_Height == AOFJH:
                        self.Descending = True
                else:
                    if self.jump_frame > 0:
                        self.jump_frame -= 1
                    self.player_Y += AOFPS
                    self.Jump_Height -= AOFPS

                    if self.Jump_Height == 0:
                        self.Descending = False
                        self.Jumping = False
                        self.Standing = True
                        self.jump_frame = 0
        Player.draw()
        return Player

###################################################################################################
""" 
  ██████╗  █████╗ ███╗   ███╗███████╗                                                 
 ██╔════╝ ██╔══██╗████╗ ████║██╔════╝                                                 
 ██║  ███╗███████║██╔████╔██║█████╗                                                   
 ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝                                                   
 ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗                                                 
  ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝                                                 
                                                                                      
  ██████╗ ██████╗ ███╗   ██╗████████╗██████╗  ██████╗ ██╗     ██╗     ███████╗██████╗ 
 ██╔════╝██╔═══██╗████╗  ██║╚══██╔══╝██╔══██╗██╔═══██╗██║     ██║     ██╔════╝██╔══██╗
 ██║     ██║   ██║██╔██╗ ██║   ██║   ██████╔╝██║   ██║██║     ██║     █████╗  ██████╔╝
 ██║     ██║   ██║██║╚██╗██║   ██║   ██╔══██╗██║   ██║██║     ██║     ██╔══╝  ██╔══██╗
 ╚██████╗╚██████╔╝██║ ╚████║   ██║   ██║  ██║╚██████╔╝███████╗███████╗███████╗██║  ██║
  ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
                                                                                      
"""
class GameController:
    def __init__(self, width, height):
        self.Running = True
        self.screenWidth = width
        self.screenHeight = height
        self.PLAYER_SPEED = 10
        self.VERTICAL_SPEED = 15
        self.FPS = 60
        self.JUMP_HEIGHT = 250
        self.PROJECTILE_VELOCITY = 50
        self.right_health = 10
        self.left_health = 10
        self.Default_Smoothscale_Dimensions = (250,250)
        self.Crouching_Smoothscale_Dimensions = (215,175)
        self.Projectile_Smoothscale_Dimensions = (150,50)
        self.Players = []
        self.clock = pygame.time.Clock()
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)
        self.GREEN = (0,255,0)
        self.YELLOW = (255,255,0)
        self.RED = (255,0,0)
        self.TAN = (255,255,204)
        self.P1 = ""
        self.P2 = ""

    def getScreenSize(self):
        dimensions = (self.screenWidth, self.screenHeight)
        return dimensions
    
    def loadPlayers(self):
        C4 = PlayerSelector()
        sprites = C4.chooseSprites()
        self.P1 = Player((400, 500), sprites[0])
        self.P2 = Player((1370, 500), sprites[1])

    def resetGame(self):
        self.right_health = 10
        self.left_health = 10
        self.loadPlayers()


###################################################################################################
"""
  ██████╗ ██████╗ ██╗     ██╗     ██╗███████╗██╗ ██████╗ ███╗   ██╗
 ██╔════╝██╔═══██╗██║     ██║     ██║██╔════╝██║██╔═══██╗████╗  ██║
 ██║     ██║   ██║██║     ██║     ██║███████╗██║██║   ██║██╔██╗ ██║
 ██║     ██║   ██║██║     ██║     ██║╚════██║██║██║   ██║██║╚██╗██║
 ╚██████╗╚██████╔╝███████╗███████╗██║███████║██║╚██████╔╝██║ ╚████║
  ╚═════╝ ╚═════╝ ╚══════╝╚══════╝╚═╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                                                                   
  ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗     
 ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██║████╗  ██║██╔════╝     
 ██║     ███████║█████╗  ██║     █████╔╝ ██║██╔██╗ ██║██║  ███╗    
 ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██║██║╚██╗██║██║   ██║    
 ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗██║██║ ╚████║╚██████╔╝    
  ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝     
                                                                    
"""

## Keeps sprites from going too far off screen
def checkForHorizontalCollisions(currentX):
    if currentX <= 50:
        return True
    elif currentX >= (screenWidth - 225):
        return True
    else:
        return False

## Mask Collision Detection between Sprites and Projectiles
def checkForProjectileCollision(sprite, projectile):
    result = pygame.sprite.collide_mask(sprite.playerMain, projectile.playerMain)
    if result != None:
        return True
    else:
        return False

###################################################################################################
"""
  ██████╗  █████╗ ███╗   ███╗███████╗                                
 ██╔════╝ ██╔══██╗████╗ ████║██╔════╝                                
 ██║  ███╗███████║██╔████╔██║█████╗                                  
 ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝                                  
 ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗                                
  ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝                                
                                                                     
 ██╗   ██╗ █████╗ ██████╗ ██╗ █████╗ ██████╗ ██╗     ███████╗███████╗
 ██║   ██║██╔══██╗██╔══██╗██║██╔══██╗██╔══██╗██║     ██╔════╝██╔════╝
 ██║   ██║███████║██████╔╝██║███████║██████╔╝██║     █████╗  ███████╗
 ╚██╗ ██╔╝██╔══██║██╔══██╗██║██╔══██║██╔══██╗██║     ██╔══╝  ╚════██║
  ╚████╔╝ ██║  ██║██║  ██║██║██║  ██║██████╔╝███████╗███████╗███████║
   ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝╚══════╝                                                                   
 """

## Initialize Pygame Stuff
pygame.init()
pygame.font.init()
pygame.mixer.init()
pygame.mixer.set_num_channels(7)
utilities.background_music()
running = True

## Rough Dimensions of Byron's Monitor
screenWidth = 1750
screenHeight = 800

## New Game Controller Object
AOFW = GameController(screenWidth, screenHeight)

## Set the size of the window using the above dimensions
size = (screenWidth, screenHeight)
screen = pygame.display.set_mode(size)

## Setting the background image and orienting starting from (0,0) origin i.e top left corner
BackGround = Background("Arena_Night.jpg", [0, 0], (screenWidth, screenHeight))

AOFW.loadPlayers()

## Set the title of the window
banner = f'Get Ready for Deadliest Warrior! {AOFW.P1.name} vs {AOFW.P2.name}'
pygame.display.set_caption(banner)

## Control variables for when sprites cross over each other
P1_Inverted = False
P2_Inverted = True

tick = 0

## Reset Button stuff
button_font = pygame.font.SysFont('Algerian', 50)
button_text = button_font.render("RESET", True, AOFW.TAN)
button_rect = button_text.get_rect()
button_rect.center = (screenWidth // 2, screenHeight - 200)

###################################################################################################
"""
  ██████╗  █████╗ ███╗   ███╗███████╗    ██╗      ██████╗  ██████╗ ██████╗ 
 ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██║     ██╔═══██╗██╔═══██╗██╔══██╗
 ██║  ███╗███████║██╔████╔██║█████╗      ██║     ██║   ██║██║   ██║██████╔╝
 ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║     ██║   ██║██║   ██║██╔═══╝ 
 ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ███████╗╚██████╔╝╚██████╔╝██║     
  ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝    ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝                                                                             
"""
## Run the game loop
while running:
    AOFW.clock.tick(AOFW.FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                # Reset the game
                AOFW.resetGame()
                utilities.background_music() 
    if AOFW.right_health <= 0 or AOFW.left_health <= 0:
            # Draw the reset button and wait for the player to click it
            pygame.draw.rect(screen, (255, 0, 0), button_rect)
            screen.blit(button_text, button_rect)
            pygame.display.update()
    ## Get the pressed keys
    keys = pygame.key.get_pressed()

    ## Player 1 key controls
    if keys[pygame.K_a]:
        AOFW.P1.Moving = True
        pygame.mixer.Channel(6).set_volume(0.05)
        pygame.mixer.Channel(6).play(pygame.mixer.Sound('fight_sounds/metal-plate.wav'))
        P1_Collision = checkForHorizontalCollisions(AOFW.P1.player_X - AOFW.PLAYER_SPEED)
        if P1_Collision == False and AOFW.P1.Dead == False:
            AOFW.P1.player_X -= AOFW.PLAYER_SPEED
    if keys[pygame.K_d]:
        AOFW.P1.Moving = True
        pygame.mixer.Channel(6).set_volume(0.05)
        pygame.mixer.Channel(6).play(pygame.mixer.Sound('fight_sounds/metal-plate.wav'))
        P1_Collision = checkForHorizontalCollisions(AOFW.P1.player_X + AOFW.PLAYER_SPEED)
        if P1_Collision == False and AOFW.P1.Dead == False:
            AOFW.P1.player_X += AOFW.PLAYER_SPEED
    if keys[pygame.K_w]:
        if AOFW.P1.Standing == True and AOFW.P1.Dead == False:
            pygame.mixer.Channel(6).set_volume(0.04)
            pygame.mixer.Channel(6).play(pygame.mixer.Sound('fight_sounds/sword-hit-in-battle.wav'))
            AOFW.P1.Jumping = True
            AOFW.P1.Standing = False
    if keys[pygame.K_LSHIFT]:
        if AOFW.P1.Projectile == False and AOFW.P1.Dead == False:
            AOFW.P1.Projectile = True
            pygame.mixer.Channel(1).set_volume(0.07)
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('fight_sounds/fighting-mans-voice.wav'))
            AOFW.P1.Attacking = True
            P1_Spear_X = AOFW.P1.player_X
            P1_Spear_Y = AOFW.P1.player_Y
            P1_Spear = GameSprite('Projectiles/spear_LTR.png',
                                  (P1_Spear_X, P1_Spear_Y), AOFW.Projectile_Smoothscale_Dimensions, False)
            P1_Spear.draw()
    if keys[pygame.K_s]:
            AOFW.P1.Crouching = True

    ## Player 2 key controls
    if keys[pygame.K_LEFT]:
        AOFW.P2.Moving = True
        pygame.mixer.Channel(6).set_volume(0.05)
        pygame.mixer.Channel(6).play(pygame.mixer.Sound('fight_sounds/metal-plate.wav'))
        P2_Collision = checkForHorizontalCollisions(AOFW.P2.player_X - AOFW.PLAYER_SPEED)
        if P2_Collision == False and AOFW.P2.Dead == False:
            AOFW.P2.player_X -= AOFW.PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        AOFW.P2.Moving = True
        pygame.mixer.Channel(6).set_volume(0.05)
        pygame.mixer.Channel(6).play(pygame.mixer.Sound('fight_sounds/metal-plate.wav'))
        P2_Collision = checkForHorizontalCollisions(AOFW.P2.player_X + AOFW.PLAYER_SPEED)
        if P2_Collision == False and AOFW.P2.Dead == False:
            AOFW.P2.player_X += AOFW.PLAYER_SPEED
    if keys[pygame.K_UP]:
        if AOFW.P2.Standing == True and AOFW.P2.Dead == False:
            AOFW.P2.Jumping = True
            pygame.mixer.Channel(0).set_volume(0.01)
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('fight_sounds/sword-hit-in-battle.wav'))
            AOFW.P2.Standing = False
    if keys[pygame.K_RSHIFT]:
        if AOFW.P2.Projectile == False and AOFW.P2.Dead == False:
            pygame.mixer.Channel(1).set_volume(0.07)
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('fight_sounds/fighting-mans-voice.wav'))
            AOFW.P2.Projectile = True
            AOFW.P2.Attacking = True
            P2_Spear_X = AOFW.P2.player_X
            P2_Spear_Y = AOFW.P2.player_Y
            P2_Spear = GameSprite('Projectiles/spear_RTL.png',
                                  (P2_Spear_X, P2_Spear_Y), AOFW.Projectile_Smoothscale_Dimensions, False)
            P2_Spear.draw()
    if keys[pygame.K_DOWN]:
        AOFW.P2.Crouching = True

    """
        Handles where if the sprites walk past each other, they will flip their directions
    """
    if AOFW.P1.player_X > (AOFW.P2.player_X + 25):
        P1_Inverted = True
        P2_Inverted = False
    else:
        P1_Inverted = False
        P2_Inverted = True
        

    ## "I want you to paint it, paint it, paint it black"
    screen.fill(AOFW.BLACK)

    ## Layering background image of map imagery
    screen.blit(BackGround.image, BackGround.rect)

    ## Game Banner
    font = pygame.font.SysFont('Algerian',50)
    text = font.render("Are You Not Entertained?", 1, AOFW.TAN)

    screen.blit(text, (screenWidth/3,70))

    """
        Health Bar Stuff

            - Left Health = Player1
            - Right Health = Player2
            - Color coded health:
                - Green = Good
                - Yellow = Mid
                - Red = Low
    """
    Health_font = pygame.font.SysFont('Algerian', 30)

    ## Right Health Bar conditionals
    if AOFW.right_health > 7:
        right_health_text = Health_font.render(
                "Player 2 Health: " + str(AOFW.right_health), 1, AOFW.GREEN)
    elif AOFW.right_health <= 7 and AOFW.right_health > 3:
        right_health_text = Health_font.render(
                "Player 2 Health: " + str(AOFW.right_health), 1, AOFW.YELLOW)
    else:
        right_health_text = Health_font.render(
                "Player 2 Health: " + str(AOFW.right_health), 1, AOFW.RED)
        
    ## Left Health Bar conditionlas
    if AOFW.left_health > 7:
        left_health_text = Health_font.render(
                "Player 1 Health: " + str(AOFW.left_health), 1, AOFW.GREEN)
    elif AOFW.left_health <= 7 and AOFW.left_health > 3:
        left_health_text = Health_font.render(
                "Player 1 Health: " + str(AOFW.left_health), 1, AOFW.YELLOW)
    else:
        left_health_text = Health_font.render(
                "Player 1 Health: " + str(AOFW.left_health), 1, AOFW.RED)
    
    screen.blit(right_health_text, (screenWidth - right_health_text.get_width() - 120, 10))
    screen.blit(left_health_text, (120, 10))
    
    
    ## So the idle frames aren't cracked out
    if tick % 3 == 0:
        if AOFW.P1.idle_frame < AOFW.P1.idle_frameCount - 1:
            AOFW.P1.idle_frame += 1
        else:
            AOFW.P1.idle_frame = 0
        if AOFW.P2.idle_frame < AOFW.P2.idle_frameCount - 1:
            AOFW.P2.idle_frame += 1
        else:
            AOFW.P2.idle_frame = 0

    """
        Either the player is dead and animate the death slides or they
        are still alive in which case start animating the player sprite based
        on the conditions captured from key input.
    """
    if AOFW.P1.Dead == True:
        AOFW.P1.playerDeathAnimation(AOFW.Default_Smoothscale_Dimensions,P1_Inverted)
        Winner_font = pygame.font.SysFont('Algerian', 100)
        draw_text = Winner_font.render("Player 2 Wins", 1, AOFW.TAN)
        screen.blit(draw_text, (screenWidth/2 - draw_text.get_width() /
                2, screenHeight/2 - draw_text.get_height()/2))
    
    elif AOFW.P1.Crouching == True:
        Player1 = AOFW.P1.movePlayer(AOFW.Crouching_Smoothscale_Dimensions,P1_Inverted)
        AOFW.P1.Crouching = False
    else:
        Player1 = AOFW.P1.movePlayer(AOFW.Default_Smoothscale_Dimensions,P1_Inverted)

    if AOFW.P2.Dead == True:
        AOFW.P2.playerDeathAnimation(AOFW.Default_Smoothscale_Dimensions,P2_Inverted)
        Winner_font = pygame.font.SysFont('Algerian', 100)
        draw_text = Winner_font.render("Player 1 Wins", 1, AOFW.TAN)
        screen.blit(draw_text, (screenWidth/2 - draw_text.get_width() /
                2, screenHeight/2 - draw_text.get_height()/2))
        
    elif AOFW.P2.Crouching == True:
        Player2 = AOFW.P2.movePlayer(AOFW.Crouching_Smoothscale_Dimensions,P2_Inverted)
        AOFW.P2.Crouching = False
    else:
        Player2 = AOFW.P2.movePlayer(AOFW.Default_Smoothscale_Dimensions,P2_Inverted)


    ## Animation of Player 1's projectiles
    if AOFW.P1.Projectile == True:
        if P2_Inverted == True:
            P1_Spear_X += AOFW.PROJECTILE_VELOCITY
        else:
            P1_Spear_X -= AOFW.PROJECTILE_VELOCITY
        P1_Collision = checkForHorizontalCollisions(P1_Spear_X)
        P1_Hit = checkForProjectileCollision(Player2, P1_Spear)
        P1_Spear = GameSprite(fr'{AOFW.P1.spriteObject["Action"]["Weapon"]["imagePath"]}/{AOFW.P1.weapon_frame}.png',
                        (P1_Spear_X, P1_Spear_Y), AOFW.Projectile_Smoothscale_Dimensions, not P1_Inverted)
        if P1_Hit == True:
            pygame.mixer.Channel(3).set_volume(0.05)
            pygame.mixer.Channel(3).play(pygame.mixer.Sound('fight_sounds/knife-slice-cut.mp3'))
            AOFW.P2.Hurt = True
            if AOFW.right_health > 0:
                AOFW.right_health -= 3
            AOFW.P1.Projectile = False

            if AOFW.right_health <= 0:
                ## So that the health doesn't show as negative
                if AOFW.right_health < 0:
                    AOFW.right_health = 0
                AOFW.P2.Dead = True
                pygame.mixer.Channel(4).set_volume(0.1)
                pygame.mixer.Channel(4).play(pygame.mixer.Sound('fight_sounds/sword-slide-fight.wav'))
                pygame.mixer.music.pause()
                pygame.mixer.Channel(5).set_volume(0.05)
                pygame.mixer.Channel(5).play(pygame.mixer.Sound('fight_sounds/medieval-fanfare.mp3'))
        if P1_Collision == False:
            P1_Spear.draw()
            if AOFW.P1.weapon_frame < AOFW.P1.weapon_frameCount - 2:
                AOFW.P1.weapon_frame += 1
            else:
                AOFW.P1.weapon_frame = 0
        else:
            AOFW.P1.Projectile = False

    ## Animation of Player 2's projectiles
    if AOFW.P2.Projectile == True:
        if P2_Inverted == True:
            P2_Spear_X -= AOFW.PROJECTILE_VELOCITY
        else:
            P2_Spear_X += AOFW.PROJECTILE_VELOCITY
        P2_Collision = checkForHorizontalCollisions(P2_Spear_X)
        P2_Hit = checkForProjectileCollision(Player1, P2_Spear)
        P2_Spear = GameSprite(fr'{AOFW.P2.spriteObject["Action"]["Weapon"]["imagePath"]}/{AOFW.P2.weapon_frame}.png',
                        (P2_Spear_X, P2_Spear_Y), AOFW.Projectile_Smoothscale_Dimensions, not P2_Inverted)
        if P2_Hit == True:
            pygame.mixer.Channel(3).set_volume(0.1)
            pygame.mixer.Channel(3).play(pygame.mixer.Sound('fight_sounds/knife-slice-cut.mp3'))
            AOFW.P1.Hurt = True
            
            if AOFW.left_health > 0:
                AOFW.left_health -= 3
            AOFW.P2.Projectile = False

            if AOFW.left_health <= 0:
                ## So that the health doesn't show as negative
                if AOFW.left_health < 0:
                    AOFW.left_health = 0
                AOFW.P1.Dead = True
                pygame.mixer.Channel(4).set_volume(0.05)
                pygame.mixer.Channel(4).play(pygame.mixer.Sound('fight_sounds/sword-slide-fight.wav'))
                pygame.mixer.music.pause()
                pygame.mixer.Channel(5).set_volume(0.03)
                pygame.mixer.Channel(5).play(pygame.mixer.Sound('fight_sounds/medieval-fanfare.mp3'))
        if P2_Collision == False:
            P2_Spear.draw()
            if AOFW.P2.weapon_frame < AOFW.P2.weapon_frameCount - 2:
                AOFW.P2.weapon_frame += 1
            else:
                AOFW.P2.weapon_frame = 0
        else:
            AOFW.P2.Projectile = False

    tick += 1

    pygame.display.flip()
###################################################################################################