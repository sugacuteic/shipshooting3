import pygame, os, pyautogui, random
pygame.font.init()
pygame.mixer.init()
print(pyautogui.size())
WIDTH, HEIGHT = pyautogui.size()
sw, sh = WIDTH // 12, HEIGHT // 12
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ship shooting")
bg = pygame.image.load("bg.png")
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
yship = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("images\ship2.png"),(sw, sh)),-90)
rship = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("images\ship1.png"),(sw, sh)),90)
BORDER = pygame.Rect(WIDTH / 2 - 50, 0, 20, HEIGHT)
speed = 20

def red_movement(keypressed,red):
    if keypressed [pygame.K_LEFT] and red.x > BORDER.x + BORDER.width:
        red.x -= speed
    if keypressed [pygame.K_RIGHT] and red.x + sh < WIDTH :
        red.x += speed  
    if keypressed [pygame.K_DOWN] and red.y + sw < HEIGHT:
        red.y += speed
    if keypressed [pygame.K_UP] and red.y > 0 :
        red.y -= speed   

def yel_movement(keypressed,yel):
    if keypressed [pygame.K_a] and yel.x > 0:
        yel.x -= speed
    if keypressed [pygame.K_d] and yel.x + sh < BORDER.x :
        yel.x += speed  
    if keypressed [pygame.K_s] and yel.y + sw < HEIGHT:
        yel.y += speed
    if keypressed [pygame.K_w] and yel.y > 0 :
        yel.y -= speed   
        
def handle_bullets(rbullet, ybullet, RED, YELLOW):
    for b in rbullet:
        b.x -= 10
        if b.x < 0:
            rbullet.remove(b)
        if b.colliderect(YELLOW):
            rbullet.remove(b)
        for y in ybullet:
            if y.colliderect(b):
                ybullet.remove(y)
                rbullet.removeb(b)
    for y in ybullet:
        y.x += 10
        if y.x > WIDTH:
            ybullet.remove(y)
        if y.colliderect(RED):
            ybullet.remove(y)
        



def draw_screen(RED, YELLOW, rbullet, ybullet):
    screen.blit(bg, (0,0))
    screen.blit(yship, (YELLOW.x, YELLOW.y ))
    screen.blit(rship, (RED.x, RED.y))
    pygame.draw.rect(screen, "black", BORDER)
    for i in rbullet:
        pygame.draw.rect(screen, "red", i)
    # pygame.draw.rect(screen, "red", RED)
    # pygame.draw.rect(screen, "yellow", YELLOW)
    pygame.display.update()
    
def main():
    RED = pygame.Rect(WIDTH - 200, HEIGHT / 2, sh, sw)
    YELLOW = pygame.Rect(50, HEIGHT / 2, sh, sw)
    rbullet = []
    ybullet = []
    run = True
    while run:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                run = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RSHIFT:
                    b = pygame.Rect(RED.x, RED.y + RED.height / 2, 20, 10)
                    rbullet.append(b)
        if random.randint(1,50) < 3:
            b = pygame.Rect(YELLOW.x + YELLOW.width, YELLOW.y + YELLOW.height / 2, 20, 10)
            ybullet.append(b)
            
        draw_screen(RED, YELLOW, rbullet, ybullet)  
        print(len(rbullet))
        keypressed = pygame.key.get_pressed()  
        red_movement(keypressed, RED)
        yel_movement(keypressed, YELLOW)
        handle_bullets(rbullet, ybullet, RED, YELLOW)
main()