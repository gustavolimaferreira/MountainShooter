import pygame

print('Setup Start')
pygame.init()
window = pygame.display.set_mode(size=(600, 480))
print('Setup End')

print('Loop Start')
while True:
    #Check for all events
    for event in pygame.event.get():
        #If the event is quit, close the game
        if event.type == pygame.QUIT:
            print('Quitting...')
            pygame.quit()# Close Window
            quit() #end pygame
