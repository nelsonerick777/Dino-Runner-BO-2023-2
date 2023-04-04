import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS



class Cactus(Obstacle):

    TYPE_CACTUS = [SMALL_CACTUS, LARGE_CACTUS]
    TYPE_POS_CACTUS = [325, 295]

    def __init__(self):
        self.type = random.randint(0, 2)
        self.count = random.randint(0,1)
        self.type_cactus = self.TYPE_CACTUS[self.count]
        image = self.type_cactus[self.type]
        super().__init__(image)
        self.rect.y = self.TYPE_POS_CACTUS[self.count]