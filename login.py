import pygame
import os
import const
from text import InputBox

WIDTH, HEIGHT = 405, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Palocale")

WHITE = (255, 255, 255)
FPS = 60

load_images = []
for num in range(1, 8):
    load_images.append(pygame.image.load(os.path.join("assets", str(num) + ".png")))

welcome_p, welcome_button, interests_p, ints_button, ints_select, verify_p, done_p = \
    load_images


def page(currentPage, listOfAss):
    cursor_x, cursor_y = pygame.mouse.get_pos()
    

    if pygame.mouse.get_pressed(3)[0]:
        if currentPage == welcome_p and 163 < cursor_x < 241 and 490 < cursor_y < 569:
            listOfAss = [[interests_p, (0,0)]]

        elif 107 < cursor_x < 140:
          pass
            
    else:
        pass

    return listOfAss


"""
 ------ COORDINATES ------ 
Name field: 73, 360 to 331, 394
Age field: 161, 412 to 244, 448
Welc button: 163, 490 to 241, 569

Ints button: 163, 556 to 241, 635

Veri button: 163, 508 to 241, 587

Done button: 163, 491 to 241, 569
"""

def main():
    assToDisplay = [[welcome_p, (0,0)]]
    input_box1 = InputBox(73, 360, 1000, 34)
    input_box2 = InputBox(161, 412, 83, 36)
    input_boxes = [input_box1, input_box2]
    clock = pygame.time.Clock()
    run = True

    while run:
        dt = clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            for box in input_boxes:
                box.handle_event(event)
        
        assToDisplay = page(assToDisplay[0][0], assToDisplay)
        WIN.fill(WHITE)
        for ass in assToDisplay:
            WIN.blit(ass[0], ass[1])
        
        for box in input_boxes:
            box.update()
        
        for box in input_boxes:
            box.draw(WIN)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()


