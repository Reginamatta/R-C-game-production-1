import pygame as pg

WINSIZE = (640, 480)
WINCENTER = [320, 240]
NUMSTARS = 150

def main():
    pg.init()
    screen = pg.display.set_mode(WINSIZE)
    pg.display.set_caption("ReginaGame")
    white = 255, 240, 240
    black = 20, 20, 20
    screen.fill(black)
    clock = pg.time.Clock()
    duck = pg.image.load('Images/smolDuck.png')


    running = True
    while running:
        screen.fill(white)
        screen.blit(duck, (50, 50))
        pg.display.update()
        clock.tick(50)
        for event in pg.event.get():
            # Check for QUIT event
            if event.type == pg.QUIT:
                running = False
    pg.quit()


if __name__ == '__main__':
    main()
