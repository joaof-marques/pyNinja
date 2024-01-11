import pygame
import os

class Game:
    def __init__(self) -> None:
        self.screen_width = 1440
        self.screen_height = 900
        self.ground_level = 800
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.fps = pygame.time.Clock()
        
        self.hero_animation_frame = 0
        
    
    def set_background(self) -> None:
        background_surface = pygame.image.load(os.path.join("sprites","enviroment", "background.png")).convert_alpha()
        ground_surface = pygame.image.load(os.path.join("sprites","enviroment", "ground.png")).convert_alpha()
        self.screen.blit(background_surface, (0,0))
        self.screen.blit(ground_surface, (0,self.ground_level-20))
    
    def get_frame_from_spritesheet (self, spritesheet, frame_size, frame_pos) -> pygame.Surface:        
        x_start = frame_size*frame_pos
        x_final = x_start + frame_size
        
        image = pygame.Surface((frame_size, frame_size), pygame.SRCALPHA)     
        image.blit(spritesheet.convert_alpha(), (0,0), (x_start, 0, x_final, frame_size))
        
        return image
    
    
    def draw_hero(self) -> None: 
        hero_surface = pygame.image.load(os.path.join("sprites", 'hero', "hero_idle.png")).convert_alpha()
        hero_frame_surface = self.get_frame_from_spritesheet(hero_surface, 128, self.hero_animation_frame//5).convert_alpha()
        hero_rect = hero_frame_surface.get_rect(midbottom = (700, self.ground_level))
        self.screen.blit(hero_frame_surface, hero_rect)
        
        
    
    def run (self):
        pygame.init()
        
        while True:
            self.fps.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                    
            self.set_background()
            if self.hero_animation_frame >= 30:
                self.hero_animation_frame = 0
            self.draw_hero()
            self.hero_animation_frame += 1
            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()