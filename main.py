import pygame
import os
from characters_classes import Hero, Enemy

class Game:
    def __init__(self) -> None:
        self.screen_width = 1440
        self.screen_height = 900
        self.ground_level = 750
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.fps = pygame.time.Clock()
        
        # Characters
        self.hero = Hero()
        self.group_single = pygame.sprite.GroupSingle()
        self.group_single.add(self.hero)
        
        self.mobs = []
        self.mobs_group = pygame.sprite.Group()
        
    def set_background(self) -> None:
        background_surface = pygame.image.load(os.path.join("sprites","enviroment", "background.png")).convert_alpha()
        ground_surface = pygame.image.load(os.path.join("sprites","enviroment", "ground.png")).convert_alpha()
        self.screen.blit(background_surface, (0,0))
        self.screen.blit(ground_surface, (0,self.ground_level-20))

    
    def run (self):
        pygame.init()
        
        while True:
            self.fps.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                    
            self.set_background()
            if len(self.mobs) < 1:
                self.mobs.append(Enemy("fire_mob", 6))
                self.mobs_group.add(self.mobs[-1])
            
            
            self.mobs_group.update(self.hero.x)  
            self.group_single.update() #handle animations swap
            self.mobs_group.draw(self.screen)        
            self.group_single.draw(self.screen)
            
            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()