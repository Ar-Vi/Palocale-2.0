import pygame
import os
import login
pygame.font.init()

WIDTH, HEIGHT = 405, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Palocale")

WHITE = (255, 255, 255)
FPS = 60
FONT = pygame.font.Font(None, 32)

load_images = []
for file_num in range(len(os.listdir("assets"))):
    load_images.append(pygame.image.load(os.path.join("assets", str(file_num + 1) + ".png")))

welcome_p, welc_button, interests_p, ints_button, A1, B1, C1, A2, B2, C2, A3, B3, C3, verify_p, done_p, friends_p, \
hangouts_p, explore_p, chat_p, you_p = load_images

def page(focus):
    cursor_x, cursor_y = pygame.mouse.get_pos()
    if 670 < cursor_y < 705:
        if pygame.mouse.get_pressed(3)[0]:
            if 32 < cursor_x < 60:
                focus = friends_p
            elif 107 < cursor_x < 140:
                focus = hangouts_p
            elif 173 < cursor_x < 231:
                focus = explore_p
            elif 265 < cursor_x < 304:
                focus = chat_p
            elif 350 < cursor_x < 372:
                focus = you_p

    else:
        pass

    return focus

def main(user_input):
    focus = explore_p

    clock = pygame.time.Clock()
    run = True
    while run:
        dt = clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        focus = page(focus)

        WIN.fill(WHITE)
        WIN.blit(focus, (0, 0))

        if focus == you_p:
            text_surface = FONT.render(user_input[0] + "• " + user_input[1], True, (0, 0, 0))
            WIN.blit(text_surface, (52, 433))

        pygame.display.update()

    pygame.font.quit()
    pygame.quit()

if __name__ == "__main__":
    main(login.user_input)