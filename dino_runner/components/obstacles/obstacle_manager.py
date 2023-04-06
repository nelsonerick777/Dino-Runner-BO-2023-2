from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird_evil import Bird
import random


class ObstacleManager:


    def __init__(self):
        self.obstacles = []


    def update(self, game_speed,player):
        select_mob = random.randint(0,1)
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus())if select_mob == 0 else self.obstacles.append(Bird())
        for obstacle in self.obstacles:
            if player.rect2.colliderect(obstacle.rect) or obstacle.rect.x < -obstacle.rect.width:
                self.obstacles.pop(0)
                #if player.image2.rect.colliderect(self.rect):
            obstacle.update(game_speed,player)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

#self.obstacles.append(random.choice(self.types))
        # for obstacle in self.obstacles:
        #     if obstacle.rect.x < -obstacle.rect.width:
        #         self.obstacles.pop()
        #     obstacle.update(game_speed,player)


