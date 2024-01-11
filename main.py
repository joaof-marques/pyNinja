import pygame
import os

class Game:
    def __init__(self) -> None:
        self.screen_width = 1440
        self.screen_height = 900
        self.ground_level = 800
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.fps = pygame.time.Clock()
    
    def set_background(self) -> None:
        background_surface = pygame.image.load(os.path.join("sprites", "background.png")).convert_alpha()
        ground_surface = pygame.image.load(os.path.join("sprites", "ground.png")).convert_alpha()
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
            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()