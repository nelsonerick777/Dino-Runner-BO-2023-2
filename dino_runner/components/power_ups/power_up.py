import pygame
from dino_runner.utils.constants import SCREEN_WIDTH, SHIELD_TYPE, HAMMER_TYPE,SOUND_POWER

class PowerUp:

    Y_POS_POWER_UP =125
    POWER_UP_DURATION = 5000
    POWER_UP_DURATION_HAMMER = 3000

    def __init__(self,image,type):
        self.image = image
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = self.Y_POS_POWER_UP
        self.used = False
        self.start_time = 0
        self.time_up = 0
        self.act = SHIELD_TYPE
        self.sound = SOUND_POWER


    def update(self,game_speed,player):
            if self.type == SHIELD_TYPE:
                self.rect.x -= game_speed
                if self.rect.colliderect(player.dino_rect):
                    self.start_time = pygame.time.get_ticks()
                    self.time_up = self.start_time + self.POWER_UP_DURATION
                    self.used = True
            elif self.type == HAMMER_TYPE:
                 self.rect.x -= game_speed
                 if self.rect.colliderect(player.dino_rect):
                    self.start_time = pygame.time.get_ticks()
                    self.time_up = self.start_time + self.POWER_UP_DURATION_HAMMER
                    self.used = True
                      #self.rect.x += game_speed
                #     self.time_up = 0
                #     self.used = False
                


            
    

    def draw(self, screen):
        screen.blit(self.image, self.rect)