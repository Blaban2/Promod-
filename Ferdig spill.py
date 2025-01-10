import pygame
import time 
import random 

pygame.init()

screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Pong Spill")

background = pygame.image.load("/Users/benjaminalfheim/Vcs Programering/promod vg3/Spillprosjekt pygame/Pong skalbruke.png")
background = pygame.transform.scale(background, (1000, 600))

#Klasse for spillere
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, z):
        super().__init__()
        self.player_height = z
        self.image = pygame.Surface((10, self.player_height))
        self.image.fill("#FF0000")
        self.rect = self.image.get_rect(topleft=(x, y))

    def input(self, opp, ned):
        keys = pygame.key.get_pressed()
        if keys[opp]:
            if self.rect.y <= 0:
                pass
            else:
                self.rect.y -= 10
        if keys[ned]:
            if self.rect.y >= 500:
                pass
            else:
                self.rect.y += 10

    def reduser_størrelse(self):
        self.player_height = max(10, self.player_height - 15)

        self.image = pygame.Surface((10, self.player_height))
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.image.fill("#FF0000")

    def draw(self, screen):
        screen.blit(self.image, self.rect)


#Klasse for Ballen
class Balls(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, color, speed_x, speed_y):
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        self.rect = self.image.get_rect(center=(x, y))
        
        self.speed_x = speed_x
        self.speed_y = speed_y

    def bevegelse(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.top <= 0 or self.rect.bottom >= 600:
            self.speed_y *= -1.05
            self.speed_x *= 1.05

        if self.rect.left <= 0:
            poeng.plusspoeng(2)
            self.speed_x == 0
            self.speed_y == 0
            self.reset_position(screen, 2000)
        
        if self.rect.right >= 1000:
            poeng.plusspoeng(1)
            self.speed_x == 0
            self.speed_y == 0
            self.reset_position(screen, 2000)

        if self.rect.colliderect(player1.rect):
            self.speed_x *= -1
            if current_mode == 2: 
                player1.reduser_størrelse()
            
            if current_mode == 3: 
                self.speed_x *= 1.2
                


        if self.rect.colliderect(player2.rect):
            self.speed_x *= -1
            if current_mode == 2: 
                player2.reduser_størrelse()
            
            if current_mode == 3: 
                self.speed_x *= 1.2
            
        
        if current_mode == 4:
            if self.rect.colliderect(player3.rect):
                self.speed_x *= -1
            if self.rect.colliderect(player4.rect):
                self.speed_x *= -1
    
    def reset_position(self, screen, wait_time):

        self.rect.center = (500, 300)
        self.speed_x = 0
        self.speed_y = 0

        screen.blit(background, (0, 0))
        screen.blit(self.image, self.rect)
        poeng.draw(screen)
        player1.draw(screen)
        player2.draw(screen)

        pygame.display.flip()

        pygame.time.wait(wait_time)

        self.speed_x = 5 * random.choice([-1, 1])
        self.speed_y = 5 * random.choice([-1, 1])


    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Score:
    def __init__(self):
        self.player1_score = 0
        self.player2_score = 0
        self.font = pygame.font.Font(None, 74)

    def plusspoeng(self, player):
        if player == 1:
            global current_mode
            self.player1_score += 1
            player1.rect.y = 250
            player2.rect.y = 250
            player1.player_height = 100
            player2.player_height = 100

            player1.player_height = 100
            player1.image = pygame.Surface((10, player1.player_height))
            player1.image.fill("#FF0000")
            player1.rect = player1.image.get_rect(topleft=(player1.rect.x, player1.rect.y))


            player2.player_height = 100
            player2.image = pygame.Surface((10, player2.player_height))
            player2.image.fill("#FF0000")
            player2.rect = player2.image.get_rect(topleft=(player2.rect.x, player2.rect.y))

            if vmode == 1:
                current_mode = random.randint(2,4)

        elif player == 2:
            self.player2_score += 1
            player1.rect.y = 250
            player2.rect.y = 250
            
            player1.player_height = 100
            player1.image = pygame.Surface((10, player1.player_height))
            player1.image.fill("#FF0000")
            player1.rect = player1.image.get_rect(topleft=(player1.rect.x, player1.rect.y))


            player2.player_height = 100
            player2.image = pygame.Surface((10, player2.player_height))
            player2.image.fill("#FF0000")
            player2.rect = player2.image.get_rect(topleft=(player2.rect.x, player2.rect.y))

            if vmode == 1:
                current_mode = random.randint(2,4)


    def draw(self, screen):
        player1_text = self.font.render(str(self.player1_score), True, "#ffffff")
        screen.blit(player1_text, (400, 20))

        player2_text = self.font.render(str(self.player2_score), True, "#ffffff")
        screen.blit(player2_text, (600, 20))


def meny(screen):
    background = pygame.image.load("/Users/benjaminalfheim/Vcs Programering/promod vg3/Spillprosjekt pygame/Meny Bilde 2.jpg")
    background = pygame.transform.scale(background, (1000, 600))
    
    screen.blit(background, (0, 0))

    font = pygame.font.Font(None, 74)
    title_text = font.render("Pong Spill", True, "#ffffff")
    start_text = font.render("Start Spill (Enter)", True, "#ffffff")
    quit_text = font.render("Avslutt (ESC)", True, "#ffffff")
    
    screen.blit(title_text, (screen.get_width() // 2 - title_text.get_width() // 2, 150))
    screen.blit(start_text, (screen.get_width() // 2 - start_text.get_width() // 2, 300))
    screen.blit(quit_text, (screen.get_width() // 2 - quit_text.get_width() // 2, 400))
    
    pygame.display.flip()


def win(screen, x):
    background = pygame.image.load("/Users/benjaminalfheim/Vcs Programering/promod vg3/Spillprosjekt pygame/Meny Bilde 2.jpg")
    background = pygame.transform.scale(background, (1000, 600))
    
    screen.blit(background, (0, 0))

    if gamemode == 4: 
        player3.player_height -= player3.player_height
        player4.player_height -= player4.player_height

    if poeng.player1_score == x:
        font = pygame.font.Font(None, 74)
        title_text = font.render("Game over", True, "#ffffff")
        start_text = font.render("Spiller 1 vant!", True, "#ffffff")
    if poeng.player2_score == x:
        font = pygame.font.Font(None, 74)
        title_text = font.render("Game over", True, "#ffffff")
        start_text = font.render("Spiller 2 vant!", True, "#ffffff")
    
    screen.blit(title_text, (screen.get_width() // 2 - title_text.get_width() // 2, 150))
    screen.blit(start_text, (screen.get_width() // 2 - start_text.get_width() // 2, 300))

    poeng.player1_score = 0
    poeng.player2_score = 0

    pygame.display.flip()
    pygame.time.wait(3000)


def velg_mode(screen):
    background = pygame.image.load("/Users/benjaminalfheim/Vcs Programering/promod vg3/Spillprosjekt pygame/Meny Bilde 2.jpg")
    background = pygame.transform.scale(background, (1000, 600))
    
    screen.blit(background, (0, 0))

    font = pygame.font.Font(None, 74)
    title_text = font.render("Velg gamemode!", True, "#ffffff")
    start_text = font.render("Vanlig pong: (1)", True, "#ffffff")
    quit_text = font.render("Variert pong: (2)", True, "#ffffff")
    
    screen.blit(title_text, (screen.get_width() // 2 - title_text.get_width() // 2, 150))
    screen.blit(start_text, (screen.get_width() // 2 - start_text.get_width() // 2, 300))
    screen.blit(quit_text, (screen.get_width() // 2 - quit_text.get_width() // 2, 400))
    
    pygame.display.flip()


def gamemode(x,):
    if x == 1: 
        background = pygame.image.load("/Users/benjaminalfheim/Vcs Programering/promod vg3/Spillprosjekt pygame/Pong skalbruke.png")
        background = pygame.transform.scale(background, (1000, 600))
        screen.blit(background, (0, 0))

        player1.input(pygame.K_w, pygame.K_s)
        player1.draw(screen)

        player2.input(pygame.K_UP, pygame.K_DOWN)
        player2.draw(screen)

        ball.bevegelse()
        ball.draw(screen)

        poeng.draw(screen)

        pygame.display.flip()

    if x == 2: 
        background = pygame.image.load("/Users/benjaminalfheim/Vcs Programering/promod vg3/Spillprosjekt pygame/Pong skalbruke.png")
        background = pygame.transform.scale(background, (1000, 600))
        screen.blit(background, (0, 0))

        player1.input(pygame.K_w, pygame.K_s)
        player1.draw(screen)

        player2.input(pygame.K_UP, pygame.K_DOWN)
        player2.draw(screen)

        ball.bevegelse()
        ball.draw(screen)

        poeng.draw(screen)

        pygame.display.flip()

    if x == 3:
        background = pygame.image.load("/Users/benjaminalfheim/Vcs Programering/promod vg3/Spillprosjekt pygame/Pong skalbruke.png")
        background = pygame.transform.scale(background, (1000, 600))
        screen.blit(background, (0, 0))

        player1.input(pygame.K_w, pygame.K_s)
        player1.draw(screen)

        player2.input(pygame.K_UP, pygame.K_DOWN)
        player2.draw(screen)

        ball.bevegelse()
        ball.draw(screen)

        poeng.draw(screen)

        pygame.display.flip()

    if x == 4:
        background = pygame.image.load("/Users/benjaminalfheim/Vcs Programering/promod vg3/Spillprosjekt pygame/Pong skalbruke.png")
        background = pygame.transform.scale(background, (1000, 600))
        screen.blit(background, (0, 0))

        player1.input(pygame.K_w, pygame.K_s)
        player1.draw(screen)

        player3.draw(screen)
        player4.draw(screen)

        player2.input(pygame.K_UP, pygame.K_DOWN)
        player2.draw(screen)

        ball.bevegelse()
        ball.draw(screen)

        poeng.draw(screen)

        pygame.display.flip()


game_state = "meny"

current_mode = None

player1 = Player(50, 250, 100)
player2 = Player(950, 250, 100)

player3 = Player(random.randint(250, 500), random.randint(50, 550), random.randint(50, 150))
player4 = Player(random.randint(500, 750), random.randint(50, 550), random.randint(50, 150))

ball = Balls(500, 300, 15, "#ffffff", 5, 5)

poeng = Score()

Game_time = 5

vmode = 0

game_running = True
clock = pygame.time.Clock()

while game_running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game_running = False

        if game_state == "meny":
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    game_state = "velg_mode"
                elif e.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

        elif game_state == "velg_mode":
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_1:
                    vmode = 0
                    current_mode = 1
                    game_state = "play"
                elif e.key == pygame.K_2:
                    vmode = 1
                    current_mode = random.randint(2,4)
                    game_state = "play"

    if game_state == "meny":
        meny(screen)

    elif game_state == "velg_mode":
        velg_mode(screen)

    elif game_state == "play":
        if current_mode == 1:
            gamemode(1)

        if current_mode == 2:
            gamemode(2)
        
        if current_mode == 3:
            gamemode(3)

        if current_mode == 4:
            gamemode(4)

    clock.tick(60)

    if poeng.player1_score == Game_time or poeng.player2_score == Game_time:
        win(screen, Game_time)
        game_state = "meny"

        

pygame.quit()