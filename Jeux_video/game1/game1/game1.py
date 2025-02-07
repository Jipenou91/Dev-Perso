import pygame, random


pygame.init()

#fenetre
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

# colors
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)

#variables
running = True
dt = 0

#position du joueur
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() -100)

#boucle du jeu
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    
    img_vaisseau = pygame.image.load('image/vaisseau.jpg')
    screen.blit(img_vaisseau, (player_pos))

    #pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_z]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_q]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
    if keys[pygame.K_SPACE]:
        pygame.draw.rect(screen, white, )

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
