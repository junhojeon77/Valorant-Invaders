import pygame
import random
import time

pygame.font.init()
pygame.mixer.init()
WIDTH, HEIGHT = 1000, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Valorant Invaders")

BG = pygame.transform.scale(pygame.image.load("valorant.jpg"), (WIDTH, HEIGHT))
star_img = pygame.transform.scale(pygame.image.load("Jett.png"), (120, 120))
player_img = pygame.transform.scale(pygame.image.load("yoru.jpg"), (90, 90))
music = pygame.mixer.music.load('valorantmusic.mp3')
font = pygame.font.SysFont("comicsans", 50)

def draw(player, elapsed_time, stars):
    WIN.blit(BG, (0,0))
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, (255, 255, 255))
    WIN.blit(time_text, (10, 10))
    WIN.blit(player_img, player.topleft)
    
    for star in stars:
        WIN.blit(star_img, star.topleft)
    
    pygame.display.update()
    

    
STAR_WIDTH = 120
STAR_HEIGHT = 120
STAR_VEL = 15

PLAYER_WIDTH = 90
PLAYER_HEIGHT = 90
Player_vel = 20

FONT = pygame.font.SysFont('comicsans', 30)


def main():
    
    run = True
    
    player = pygame.Rect(WIDTH // 2, HEIGHT - 100, PLAYER_WIDTH, PLAYER_HEIGHT)
    
    clock = pygame.time.Clock()
    
    start_time = time.time()
    elapsed_time = 0
    
    star_add_counter = 1500
    star_count = 0
    
    stars = []
    
    
    while run:
        while run & hit == False:
            pygame.mixer.music.load(music)
        hit = False
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time
        
        if star_count >= star_add_counter:
            for i in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)
                
            star_add_counter = max(200, star_add_counter - 50)
            star_count = 0
                
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    return True
                elif event.key == pygame.K_n:
                    return False
                break
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player[0] - Player_vel >= 0:
            player[0] -= Player_vel
        if keys[pygame.K_RIGHT]and player[0] + Player_vel <= WIDTH:
            player[0] += Player_vel
        
        
        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y >= player[1] and star.colliderect(player):
                stars.remove(star)
                hit = True
                break
            
        if hit:
            retry = ask_retry()
            if retry:
                main()
            else:
                run = False
                        
            
        draw(player, elapsed_time, stars)
        
    pygame.quit()
    
def ask_retry():
    lost_text = FONT.render("You Lost! Try again? Y/N", 1, "White")
    WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, 
                         HEIGHT/2 - lost_text.get_height()/2))
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    return True
                elif event.key == pygame.K_n:
                    return False
    
    

if __name__ == "__main__":
    main()

