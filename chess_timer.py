import pygame
import time

pygame.init()
pygame.display.init()
pygame.mixer.init()
pygame.font.init()

WIDTH = 720
HEIGHT = 360
TIMER = 5
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.mixer.music.load("lose.wav")
font = pygame.font.SysFont('Calibri', 30)
clock = pygame.time.Clock()


def blit_to(text, coords):
    """Blits text, centered, to coords, provided as a tuple."""
    to_display = font.render(text, False, WHITE)
    (text_w, text_h) = font.size(text)
    screen.blit(to_display, (coords[0] - (text_w / 2), coords[1] - (text_h / 2)))


def gameloop():
    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            return
        if ev.type == pygame.KEYDOWN:
            break
        blit_to("Press Space to start.", (WIDTH / 2, HEIGHT / 2))
        pygame.display.flip()

    turn = 1
    while True:

        start_time = time.clock()
        while turn == 1:
            ev = pygame.event.poll()
            time_left = round(TIMER - (time.clock() - start_time), 1)
            if ev.type == pygame.QUIT:
                return
            if time_left <= 0:
                return 2
            if ev.type == pygame.KEYDOWN:
                turn = 2
            blit_to("PLAYER ONE'S TURN", (WIDTH / 4, HEIGHT / 4))
            blit_to("TIME: {}".format(time_left), (WIDTH / 4, HEIGHT / 3))
            blit_to("PLAYER TWO", (3/4 * WIDTH, HEIGHT / 4))
            blit_to("Press Space to end turn.", (WIDTH / 2, HEIGHT / 2))
            pygame.display.flip()
            screen.fill(BLACK)

        start_time = time.clock()
        while turn == 2:
            ev = pygame.event.poll()
            time_left = round(TIMER - (time.clock() - start_time), 1)
            if ev.type == pygame.QUIT:
                return
            if time_left <= 0:
                return 1
            if ev.type == pygame.KEYDOWN:
                turn = 1
            blit_to("PLAYER ONE", (WIDTH / 4, HEIGHT / 4))
            blit_to("PLAYER TWO'S TURN", (3/4 * WIDTH, HEIGHT / 4))
            blit_to("TIME: {}".format(time_left), (3/4 * WIDTH, HEIGHT / 3))
            blit_to("Press Space to end turn.", (WIDTH / 2, HEIGHT / 2))
            pygame.display.flip()
            screen.fill(BLACK)


result = gameloop()
if result is None:
    pygame.quit()
else:
    pygame.mixer.music.play()
    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break
        blit_to("PLAYER {} WINS".format("TWO" if result == 2 else "ONE"), (WIDTH / 2, HEIGHT / 2))
        pygame.display.flip()
        screen.fill(BLACK)
