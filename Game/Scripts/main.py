import pygame

print(f'Initializing...')
pygame.init()

window = pygame.display.set_mode((1280, 720), vsync=True)

pygame.display.set_caption("???? Adventures")
clock = pygame.time.Clock()
print(f'Initialization complete.')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #close window
            print(f'Exiting...')
            quit() #end pygame

