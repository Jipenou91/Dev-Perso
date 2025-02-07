import pygame, random


pygame.init()

# fenetre
screen = pygame.display.set_mode((1900, 1000))
title = pygame.display.set_caption("Agar io")
icon = pygame.image.load('agar_io_icon.jpg')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
font = pygame.font.Font(None, 24)

# variables
running = True
dt = 0
rep = 0
score = 0
weight = 0

# fonctions
def init_food():
    nb_food = 0
    pos_food = [(i, i+1) for i in range(100)]
    while nb_food<100:
        pos_x = random.randint(50,1850)
        pos_y = random.randint(50,950)
        pos_food[nb_food] = (pos_x,pos_y)
        #print("pos_food[",nb_food,"] = ",pos_food[nb_food])
        nb_food+=1
    return pos_food

def place_food(pos_food):
    for k in range(100):
        pygame.draw.circle(screen, "green", pos_food[k], 5)

def eat_food(player_pos, player_radius, pos_food):
    for i, food_pos in enumerate(pos_food):
        if detection_food(player_pos, player_radius, food_pos):
            return i
    return -1

def detection_food(player_pos, player_radius, food_pos):
    dx = player_pos.x - food_pos[0]
    dy = player_pos.y - food_pos[1]
    distance = (dx * dx + dy * dy) ** 0.5
    return distance < player_radius + 5

def replace_food(indice, pos_food):
    pos_x = random.randint(50,1850)
    pos_y = random.randint(50,950)
    pos_food[indice] = (pos_x,pos_y)

def affiche_score(score):
    label_score = font.render("SCORE : ",1,(255,255,255))
    label_valeur_score = font.render(str(score),1,(255,255,255))
    screen.blit(label_score, (1700,100))
    screen.blit(label_valeur_score, (1780,100))
      

# position du joueur
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() -100)
taille = 40

# Limites de la zone de jeu
left_limit = 0
right_limit = 1900
top_limit = 0
bottom_limit = 1000

pos_food = init_food()

# boucle du jeu
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    
    #place la nourriture
    place_food(pos_food)

    #joueur principal
    pygame.draw.circle(screen, "red", player_pos, taille+weight)
    
    #detection si nourriture mangé
    indice = eat_food(player_pos,taille+weight, pos_food)
    
    #si nourriture mangé score++ et replace nourriture
    if indice!=-1:
        score+=1
        weight+=1
        replace_food(indice, pos_food)
        
    #affiche le score
    affiche_score(score)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_z]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_q]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt


    if player_pos.x < left_limit:
        player_pos.x = left_limit 
    if player_pos.x > right_limit:
        player_pos.x = right_limit
    if player_pos.y < top_limit:
        player_pos.y = top_limit
    if player_pos.y > bottom_limit:
        player_pos.y = bottom_limit


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()

