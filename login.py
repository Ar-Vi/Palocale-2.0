import pygame
import os
import const
from text import InputBox

WIDTH, HEIGHT = 405, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Palocale")

WHITE = (255, 255, 255)
ORANGE = (248, 173, 24)
FPS = 50

load_images = []
for num in range(1, 16):
    load_images.append(pygame.image.load(os.path.join("assets", str(num) + ".png")))

welcome_p, welcome_button, interests_p, ints_button, A1, B1, C1, A2, B2, C2, A3, B3, C3, verify_p, done_p = \
    load_images


def page(currentPage, listOfAss, input_boxes):
    cursor_x, cursor_y = pygame.mouse.get_pos()
    
    if currentPage == welcome_p and len(input_boxes[0].text) > 1 and len(input_boxes[1].text) > 1:
        listOfAss.append([welcome_button, (0,0)])
    elif currentPage == interests_p and len(listOfAss) > 4:
        listOfAss.append([ints_button, (0,0)])

    if pygame.mouse.get_pressed(3)[0]: # 
        if currentPage == welcome_p and 163 < cursor_x < 241 and 490 < cursor_y < 569:
            listOfAss = [[interests_p, (0,0)]]
            input_boxes = []

        elif currentPage == interests_p and 30 < cursor_x < 137 and 172 < cursor_y < 278:
            listOfAss.append([A1, (0,0)])
        elif currentPage == interests_p and 148 < cursor_x < 256 and 172 < cursor_y < 278:
            listOfAss.append([B1, (0,0)])
        elif currentPage == interests_p and len(listOfAss) > 1 and 163 < cursor_x < 241 and 490 < cursor_y < 569:
            listOfAss = [[verify_p, (0,0)]]

            
    else:
        pass

    return listOfAss, input_boxes


"""
 ------ COORDINATES ------ 
Name field: 73, 358 to 331, 394
Age field: 161, 412 to 244, 448
Welc button: 163, 490 to 241, 569

Ints button: 163, 556 to 241, 635

Veri button: 163, 508 to 241, 587

Done button: 163, 491 to 241, 569
"""

def main():
    assToDisplay = [[welcome_p, (0,0)]]
    input_box1 = InputBox(73, 358, 258, 38)
    input_box2 = InputBox(161, 412, 83, 38)
    input_boxes = [input_box1, input_box2]#
    clock = pygame.time.Clock()
    run = True

    while run:
        dt = clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            for box in input_boxes:
                box.handle_event(event)
        
        assToDisplay, input_boxes = page(assToDisplay[0][0], assToDisplay, input_boxes)

        WIN.fill(WHITE)
        for ass in assToDisplay:
            WIN.blit(ass[0], ass[1])
        
       
        for box in input_boxes:
            box.draw(WIN)
        
        #pygame.draw.rect(WIN, ORANGE, (73, 360, 258, 34), 2)
        
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()


