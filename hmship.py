import pygame, os, pyautogui
pygame.font.init()
pygame.mixer.init()
print(pyautogui.size())
WIDTH, HEIGHT = pyautogui.size()
sw, sh = WIDTH // 16, HEIGHT // 16
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ship shooting")
bg = pygame.image.load("bg.png")
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
yship = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("images\ship2.png"),(sw, sh)),0)
rship = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("images\ship1.png"),(sw, sh)),180)
BORDER = pygame.Rect(0, HEIGHT / 2 - 5, WIDTH, 10)

def draw_screen():
    screen.blit(bg, (0,0))
    screen.blit(yship, (WIDTH /2, HEIGHT - 200))
    screen.blit(rship, (WIDTH / 2, 100))
    pygame.draw.rect(screen, "black", BORDER)
    pygame.display.update()

    
def main():
    RED = pygame.Rect(WIDTH / 2, 100, sw, sh)
    YELLOW = pygame.Rect(WIDTH / 2, 100, sw, sh)
    run = True
    while run:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                run = False
        draw_screen()    

main()