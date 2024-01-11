import pygame

class Jogo:
    def __init__(self) -> None:
        self.largura_tela = 800
        self.altura_tela = 400
        self.tela = pygame.display.set_mode((self.largura_tela, self.altura_tela))
        self.fps = pygame.time.Clock()
    
    def run (self):
        pygame.init()
        
        while True:
            self.fps.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

if __name__ == '__main__':
    jogo = Jogo()
    jogo.run()