import pygame
import os

class pyNinja_characters:
    def __init__(self, hp, damage) -> None:
        self.hp = hp
        self.damage = damage
        self.ground_level = 775           
        self.frame_pos = 0
        
        
class Hero(pygame.sprite.Sprite, pyNinja_characters):
    def __init__(self) -> None:
        self.hp = 1000
        self.damage = 250
        self.gravity = 0.5
        pygame.sprite.Sprite.__init__(self)
        pyNinja_characters.__init__(self, self.hp,self.damage)    
                
        #animation
        self.idle_frames = [pygame.image.load(os.path.join("sprites", "hero", "idle_frames", f"frame_idle_{cont}.png")) for cont in range(1,7)]  
        self.run_frames = [pygame.image.load(os.path.join("sprites", "hero", "run_frames", f"frame_run_{cont}.png")) for cont in range(1,9)]
        self.jump_frames = [pygame.image.load(os.path.join("sprites", "hero", "jump_frames", f"frame_jump_{cont}.png")) for cont in range(1,9)]
        self.current_animation = self.idle_frames
        self.index = 0
        
        #surface and rect for draw method
        self.image = self.idle_frames[self.index]
        self.rect = self.image.get_rect(midbottom = (700,self.ground_level))
        self.moved_left = False #used to determine horizontal direction
        
        #positioning
        self.x = 700
        self.y = self.ground_level
        self.x_accel = 0
        self.gravity = 0 

    def apply_accelerations(self):
        self.gravity += 1.8
        self.y += self.gravity
        self.rect.bottom = self.y
        if self.y >= self.ground_level:
            self.y = self.ground_level
            self.rect.bottom = self.ground_level
            
        self.x_accel *= 0.75
        self.x += self.x_accel
        if self.x_accel > -1 and self.x_accel < 1:
            self.x_accel = 0


    def player_inputs (self):
        keys = pygame.key.get_pressed()
                    
        if keys[pygame.K_SPACE] and self.rect.bottom >= self.ground_level:
            self.gravity = -30
            self.current_animation = self.jump_frames
            self.index = 0
        if keys[pygame.K_a]:
            self.x_accel -= 10
            self.moved_left = True
        if keys[pygame.K_d]:
            self.x_accel += 10
            self.moved_left = False
            
    def update (self):
        
        self.player_inputs()
        self.apply_accelerations()  

        if self.rect.bottom >= self.ground_level and self.x_accel == 0:
            self.current_animation = self.idle_frames
        elif self.rect.bottom >= self.ground_level and self.x_accel != 0:
            self.current_animation = self.run_frames
        # multiply and floor division to slow down the animation loop        
        if self.index >= (len(self.current_animation))*5:
            self.index = 0
            
        
        self.image = pygame.transform.flip(self.current_animation[self.index//5], self.moved_left, False)
        self.rect = self.image.get_rect(midbottom = (self.x, self.y))
        self.index+=1


            
            
        
    def attack (self) -> None:
        pass

class Enemy (pygame.sprite.Sprite, pyNinja_characters):
    def __init__(self, mob_type, idle_frame_count) -> None:
        self.hp = 600
        self.damage = 325
        self.mob_type = mob_type
        pygame.sprite.Sprite.__init__(self)
        pyNinja_characters.__init__(self, self.hp,self.damage)
        
        self.idle_frames = [pygame.image.load(os.path.join("sprites", "mobs", mob_type, "idle_frames", f"{cont}_idle_frame.png")) for cont in range(1,idle_frame_count+1)]
        self.run_frames = [pygame.image.load(os.path.join("sprites", "mobs", mob_type, "run_frames", f"{cont}_run_frame.png")) for cont in range(1,8)]
        self.current_animation = self.idle_frames
        self.index = 0
        
        self.x = 1200
        self.y = self.ground_level
        self.x_accel = 0
        self.gravity = 0
        
        self.image = self.current_animation[0]
        self.rect = self.image.get_rect(midbottom = (self.x, self.y))
        self.moved_left = False
     
    def apply_accelerations(self, hero_x):
        self.x_accel = (hero_x - self.x)*0.05
        self.x += self.x_accel
        
    def update (self, hero_x):
        
        self.apply_accelerations(hero_x)
        
        if self.rect.bottom >= self.ground_level and self.x_accel == 0:
            self.current_animation = self.idle_frames
        elif self.rect.bottom == self.ground_level and self.x_accel != 0:
            self.current_animation = self.run_frames
        # multiply and floor division to slow down the animation loop        
        if self.index >= (len(self.current_animation))*5:
            self.index = 0
            
        self.image = pygame.transform.flip(self.current_animation[self.index//5], self.moved_left, False)
        self.rect = self.image.get_rect(midbottom = (self.x, self.y))
        self.index+=1