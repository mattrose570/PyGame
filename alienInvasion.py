import sys

import pygame

from settings import Settings

# Class to manage game & assets
class AlienInvasion:
    
    #Initialize game and make resources 
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")



    # Main loop for the game
    def runGame(self):
        while True:
            # watching for keyboard/mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)
            # Make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == "__main__":
    # Creates a game instance, and run the game
    ai = AlienInvasion()
    ai.runGame()