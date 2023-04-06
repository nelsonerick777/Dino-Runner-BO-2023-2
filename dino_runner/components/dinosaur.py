import pygame
from dino_runner.utils.constants import (RUNNING,RUNNING_SHIELD,RUNNING_HAMMER,JUMPING,JUMPING_SHIELD,JUMPING_HAMMER,
                                         DUCKING,DUCKING_SHIELD,DUCKING_HAMMER, DEFAULT_TYPE,SHIELD_TYPE,HAMMER_TYPE,
                                         HAMMER,SCREEN_WIDTH)

class Dinosaur:
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5
    X_POS_HAMMER = 80
    Y_POS_HAMMER = 310
    
    def __init__(self):
        self.run_image = {DEFAULT_TYPE: RUNNING,SHIELD_TYPE:RUNNING_SHIELD,HAMMER_TYPE:RUNNING_HAMMER}
        self.duck_image = {DEFAULT_TYPE: DUCKING,SHIELD_TYPE:DUCKING_SHIELD,HAMMER_TYPE:DUCKING_HAMMER}
        self.jump_image = {DEFAULT_TYPE: JUMPING,SHIELD_TYPE:JUMPING_SHIELD,HAMMER_TYPE:JUMPING_HAMMER}
        self.type = DEFAULT_TYPE
        self.image = self.run_image[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0
        self.dino_run = True
        self.dino_duck = False
        self.dino_jump = False
        self.jump_vel = self.JUMP_VEL
        self.dino_dead = False
        self.shield = False
        self.hammer = False
        self.time_up_power_up = 0
        self.hammer_count = 0
        self.image2 = HAMMER
        self.rect2 = self.image2.get_rect()
        self.rect2.x = 0
        self.rect2.y = 0
        self.activate = False

    def update(self, user_input,game_speed):
        if self.dino_jump:
            self.jump()
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        
        if user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = True
            self.dino_jump = False
        
        elif user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = False
            self.dino_jump = True

        elif not self.dino_jump:
            self.dino_run = True
            self.dino_duck = False
            self.dino_jump = False
        
        if self.hammer == True:
            if user_input[pygame.K_SPACE]:
               self.activate = True
               self.rect2.x = self.dino_rect.x
               self.rect2.y = self.dino_rect.y
            if self.activate:
                self.ability(game_speed)
                time_to_show = round((self.time_up_power_up - pygame.time.get_ticks()) / 1000, 2)
                if time_to_show <0:
                    self.reset()


        if self.step_index >= 10:
            self.step_index = 0

        if self.shield:
            time_to_show = round((self.time_up_power_up - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show <0:
                self.reset()


    def draw(self, screen):
        screen.blit(self.image, self.dino_rect)
        if self.activate:
           screen.blit(self.image2,self.rect2)


    def run(self):
        self.image = self.run_image[self.type][self.step_index //5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1


    def duck(self):
        self.image = self.duck_image[self.type][self.step_index //5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1


    def jump(self):
        self.image = self.jump_image[self.type]
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < -self.JUMP_VEL:
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def set_power_up(self,power_up):
        if power_up.type == SHIELD_TYPE:
            self.type = SHIELD_TYPE
            self.shield = True
            self.time_up_power_up = power_up.time_up
        if power_up.type == HAMMER_TYPE:
            self.type = HAMMER_TYPE
            self.hammer = True
            self.time_up_power_up = power_up.time_up
    
    def ability(self,game_speed):
        self.rect2.x += game_speed
        #if self.rect2.x > self.rect2.weight:





    def reset(self):
        self.type = DEFAULT_TYPE
        self.shield = False
        self.hammer = False
        self.time_up_power_up = 0
        self.hammer_count = 0
        self.activate = False
        self.rect2.x = 0
        self.rect2.y = 0






    