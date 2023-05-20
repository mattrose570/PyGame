# Class to store all settings in the game
class Settings:
    
    # Initialize game settings 
    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        # Ship settings
        self.ship_speed = 1.5