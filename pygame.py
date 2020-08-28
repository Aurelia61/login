import pygame

pygame.init()
screen = pygame.display.set_mode([300,300])
base_font = pygame.font.Font(None, 32)

# username variables
username_text = ''
username_status = False
username_rect = pygame.Rect(50,50,140,32)     # définit où le rectangle (pour écrire) doit se situer (left, top, width, height)
username_color = pygame.Color('orchid') 

# password variables
password_text = ''
password_status = False
password_rect = pygame.Rect(50,120,140,32)
password_color = pygame.Color('green')  

# while we want to
while True :
    # get the event
    for event in pygame.event.get():
        # if the player quit pygame
        if event.type == pygame.QUIT:
            # close pygame
            pygame.quit()

        # if the player presses on button left of the mouse
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:     # si clic sur la souris
            # if the place where he pressed is in the surface of the username rectangle
            if username_rect.collidepoint(event.pos):  
                # the player could tape the username but not the password
                username_status = True
                password_status = False
            # if the place where he pressed is in the surface of the password rectangle
            elif password_rect.collidepoint(event.pos):
                # the player could tape the password but not the username
                password_status = True
                username_status = False

        # if the player could tape in username rect
        if username_status == True:
            # if he presses on the key of his keypad
            if event.type == pygame.KEYDOWN:
                # if he wants to delete the last letter
                if event.key == pygame.K_BACKSPACE:
                    # delete the last letter in the string
                    username_text = username_text[:-1]      
                else:
                    # add the letter pressed
                    username_text += event.unicode      # attention :: seulement sur une seule ligne

        # if the player could tape in password rect
        if password_status == True :
            # if he presses on the key of his keypad
            if event.type == pygame.KEYDOWN:
                # if he wants to delete the last letter
                if event.key == pygame.K_BACKSPACE:
                    # delete the last letter in the string
                    password_text = password_text[:-1]      
                else:
                    # add the letter pressed
                    password_text += event.unicode

    # fill the screen with the color in ()
    screen.fill((102,51,153))     # couleur du fond de la surface

    # print both rectangles
    pygame.draw.rect(screen, username_color, username_rect, 2)
    pygame.draw.rect(screen, password_color, password_rect, 2)

    # create a surface to write the login_text
    username_surface = base_font.render(username_text, True, (255,255,255))    
    # print the login_text in the middle of the surface
    screen.blit(username_surface, (username_rect.x+5, username_rect.y+5))      
    # modify the rectangle depend on the size of the text (max between 100px and what it will be written) + 10 px after the last letter
    username_rect.w = max(100, username_surface.get_width() + 10)    

    # create a surface to write the password_text
    password_surface = base_font.render(password_text, True, (0,0,0)) 
    # print the password_text in the middle of the surface
    screen.blit(password_surface, (password_rect.x+5, password_rect.y+5))
    # modify the rectangle depend on the size of the text
    password_rect.w = max(100, password_surface.get_width() + 10)  

    # update the window
    pygame.display.flip()