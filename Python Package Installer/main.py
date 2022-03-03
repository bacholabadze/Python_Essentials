# import pygame and let it serve us;
import pygame

# the program will run as long as the run variable is True;
run = True

# determine the window's size;
width = 400
height = 100

# initialize the pygame environment;
pygame.init()

# prepare the application window and set its size;
screen = pygame.display.set_mode((width, height))

# make an object representing the default font of size 48 points;
font = pygame.font.SysFont(None, 48)

# make an object representing a given text – the text will be anti-aliased (True) and white (255,255,255)
text = font.render("Welcome to pygame", True, (255, 255, 255))

# insert the text into the (currently invisible) screen buffer;
screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2))

# flip the screen buffers to make the text visible;
pygame.display.flip()

# the pygame main loop starts here;
while run:
    # get a list of all pending pygame events;
    for event in pygame.event.get():

        # check whether the user has closed the window or clicked somewhere inside it or pressed any key;
        if event.type == pygame.QUIT \
                or event.type == pygame.MOUSEBUTTONUP \
                or event.type == pygame.KEYUP:

            # if yes, stop executing the code.
            run = False


