import pygame
from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import HAMMER, HAMMER_TYPE

class Hammer(PowerUp):

    X_POS_HAMMER = 500
    Y_POS_HAMMER = 310

    def __init__(self):
        self.image = HAMMER
        self.type = HAMMER_TYPE
        super().__init__(self.image, self.type)




        