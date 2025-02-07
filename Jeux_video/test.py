import pygame, sys, random, time

pygame.init()

# fenetre
DIMENSION_X = 800
DIMENSION_Y = 1000
window = pygame.display.set_mode((DIMENSION_X, DIMENSION_Y))
title = pygame.display.set_caption('Ship Game')
icon = pygame.image.load('Documents/Thomas/Jeux_video/images/vaisseau.jpg')
win_icon = pygame.display.set_icon(icon)

# Couleurs
NOIR = (0, 0, 0)
BLANC = (255, 255, 255)
ROUGE = (255, 0, 0)

# variables
SPEED_JOUEUR = 10
SPEED_ENNEMI = 2
TAILLE_JOUEUR = 50
TAILLE_ENNEMI = 30
COULEUR_JOUEUR = BLANC
COULEUR_ENNEMI = ROUGE


# Limites de la zone de jeu
LEFT_LIMIT = 0
RIGHT_LIMIT = DIMENSION_X - TAILLE_JOUEUR
TOP_LIMIT = 0
BOTTOM_LIMIT = DIMENSION_Y - TAILLE_JOUEUR

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.taille = TAILLE_JOUEUR
        self.hauteur = TAILLE_JOUEUR
        self.color = BLANC
        self.speed = SPEED_JOUEUR
        self.shoots = []
        self.dernier_tir = 0
        self.shoot_delai = 500 # milisecond

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.taille, self.hauteur))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < DIMENSION_X - self.taille:
            self.x += self.speed
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y < DIMENSION_Y - self.hauteur:
            self.y += self.speed
        if self.y <= 700:
            self.y = 700

    def shoot(self):
        keys = pygame.key.get_pressed()
        temps_actuel = pygame.time.get_ticks()
        if keys[pygame.K_SPACE] and temps_actuel - self.dernier_tir > self.shoot_delai:
            self.shoots.append(Shoot(self.x + self.hauteur // 2, self.y))
            self.dernier_tir = temps_actuel

class Shoot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = BLANC
        self.speed = 10

    def move(self, direction):
        if direction == 'top':
            self.y -= self.speed
        else:
            self.y += self.speed

    def draw(self, window):
        pygame.draw.line(window, self.color, (self.x, self.y), (self.x, self.y - 10), 5)
        
class Ennemi:
    def __init__(self,):
        self.x = random.randint(1, 800)
        self.y = random.randint(1, 200)
        self.color = COULEUR_ENNEMI
        self.speed = SPEED_ENNEMI
        self.taille = TAILLE_ENNEMI
        self.hauteur = TAILLE_ENNEMI
        self.gauche = True
        self.droite = False
        self.shoots = []
        self.dernier_tir = 0
        self.shoot_delai = 500 # milisecond

    def draw(self, window): 
        pygame.draw.rect(window, self.color, (self.x, self.y, self.taille, self.hauteur))
    
    def move(self, window):
        if self.gauche:
            self.x += self.speed
            if self.x >= RIGHT_LIMIT + 20:
                self.gauche = False
                self.droite = True
        if self.droite:
            self.x -= self.speed
            if self.x <= LEFT_LIMIT:
                self.gauche = True
                self.droite = False
    
    def shoot(self):
        temps_actuel = pygame.time.get_ticks()
        if temps_actuel - self.dernier_tir > self.shoot_delai:
            self.shoots.append(Shoot(self.x + self.hauteur // 2, self.y))
            self.dernier_tir = temps_actuel
        
# creation joueur et ennemi
joueur = Player(DIMENSION_X // 2, DIMENSION_Y - 100)
ennemi = Ennemi()

# boucle du jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # actions joueur      
    joueur.move()
    joueur.shoot()
    
    # actions ennemi
    ennemi.move(window)
    ennemi.shoot()

    # remettre en noir l'ecran a chaque fois
    window.fill(NOIR)
    
    # dessinner joueur et ennemi
    joueur.draw(window)  
    ennemi.draw(window)
    
    # le joueur tire
    for i in joueur.shoots:
        i.move('top')
        i.draw(window)
    
    # l'ennemi tire
    for k in ennemi.shoots:
        k.move('bottom')
        k.draw(window)

    # mettre tout a jour
    pygame.display.flip()
    
    # limiter la vitesse de la boucle du jeu pour pas aller trop vite
    pygame.time.Clock().tick(60)


