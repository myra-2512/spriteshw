import pygame


pygame.init()


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Add Sprites")


black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)


sprite1_rect = pygame.Rect(50, 50, 50, 50)  
sprite2_rect = pygame.Rect(200, 200, 50, 50)


sprite1_speed = 5


running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    keys = pygame.key.get_pressed()

    
    if keys[pygame.K_LEFT] and sprite1_rect.left > 0:
        sprite1_rect.x -= sprite1_speed
    if keys[pygame.K_RIGHT] and sprite1_rect.right < screen_width:
        sprite1_rect.x += sprite1_speed
    if keys[pygame.K_UP] and sprite1_rect.top > 0:
        sprite1_rect.y -= sprite1_speed
    if keys[pygame.K_DOWN] and sprite1_rect.bottom < screen_height:
        sprite1_rect.y += sprite1_speed

    
    screen.fill(black)  
    pygame.draw.rect(screen, red, sprite1_rect)  
    pygame.draw.rect(screen, blue, sprite2_rect)  
    
    pygame.display.flip()


pygame.quit()