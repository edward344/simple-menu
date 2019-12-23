import pygame

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

BUTTON_WIDTH = 190
BUTTON_HEIGHT = 49

WHITE = (255,255,255)
YELLOW = (255,204,0)
BLACK = (0,0,0)
RED = (255,0,0)

class Menu:
    def __init__(self,items):
        self.state = 0
        self.items = items
        self.font = pygame.font.Font("kenvector_future_thin.ttf",30)
        self.sprite_sheet = pygame.image.load("button.png").convert()
        self.buttons = self.create_button()
        self.sound = pygame.mixer.Sound("switch2.ogg")
        
    def create_button(self):
        # this dictionary will contain all colors buttons
        button_dict = {}
        button_dict["blue_button"] = self.get_image(0,0,190,49)
        button_dict["yellow_button"] = self.get_image(190,0,190,49)
        
        return button_dict
        
    def get_image(self,x,y,width,height):
        """ This method will cut an image and return it """
        # Create a new blank image
        image = pygame.Surface([width,height]).convert()
        # Copy the sprite from the large sheet onto the smaller
        image.blit(self.sprite_sheet,(0,0),(x,y,width,height))
        # Assuming black works as the transparent color
        image.set_colorkey(BLACK)
        # Return the image
        return image
        
    def display_frame(self,screen):
        # draw a background rectangle
        rect = self.get_bg_rect()
        pygame.draw.rect(screen,WHITE,rect)
        pygame.draw.rect(screen,BLACK,rect,2)
        
        for index, item in enumerate(self.items):
            if self.state == index:
                button = self.buttons["yellow_button"]
            else:
                button = self.buttons["blue_button"]
                
            label = self.font.render(item,True,BLACK)    
            
            button_pos = self.get_button_pos(index)
            text_pos = self.get_text_pos(label,button_pos)
            
            screen.blit(button,button_pos)
            screen.blit(label,text_pos)
            
            
    def get_bg_rect(self):
        btn_width = BUTTON_WIDTH + 100 # add 100 px padding
        btn_height = BUTTON_HEIGHT * len(self.items) + 100 # add 100 px padding
        
        x = SCREEN_WIDTH // 2 - btn_width // 2
        y = SCREEN_HEIGHT // 2 - btn_height // 2
        width = btn_width 
        height = btn_height
        
        rect = pygame.Rect(x,y,width,height)
        
        return rect
        
            
    def get_button_pos(self,index):
        # calculate the position of the button
        posX = (SCREEN_WIDTH//2) - (BUTTON_WIDTH//2)
        # t_h: total height of button block
        t_h = len(self.items) * BUTTON_HEIGHT
        posY = (SCREEN_HEIGHT//2) - (t_h//2) + (index * (BUTTON_HEIGHT + 5))
        
        return posX,posY
        
        
    def get_text_pos(self,label,button_pos):
        # calculate position of the text on the button
        width = label.get_width()
        height = label.get_height()
        
        x,y = button_pos
        
        posX = x + (BUTTON_WIDTH//2) - (width//2)
        posY = y + (BUTTON_HEIGHT//2) - (height//2)
        
        return posX,posY
        
        
    def event_handler(self,event):
        if event.type == pygame.KEYDOWN:
            # play sound effect
            self.sound.play()
            if event.key == pygame.K_UP:
                if self.state > 0:
                    self.state -= 1
            elif event.key == pygame.K_DOWN:
                if self.state < len(self.items) -1:
                    self.state += 1
        

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("Kenny Menu")
    done = False
    clock = pygame.time.Clock()
    
    menu = Menu(("start","options","credit","exit"))
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            menu.event_handler(event)
                
        screen.fill(YELLOW)
        menu.display_frame(screen)
        pygame.display.flip()
        clock.tick(30)
        
    pygame.quit()

if __name__ == '__main__':
    main()