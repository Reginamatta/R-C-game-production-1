import pygame as pg

WINSIZE = (640, 480)
WINCENTER = [320, 240]
GROUND = 320
NUMSTARS = 150

def main():
    pg.init()
    screen = pg.display.set_mode(WINSIZE)
    pg.display.set_caption("Regina Game")
    white = 255, 240, 240
    black = 20, 20, 20
    screen.fill(black)
    clock = pg.time.Clock()
    duck = pg.image.load('Images/smolDuck.png')
    duck_position = (50,50)

    running = True
    while running:
        # game logic
        for event in pg.event.get():
            # Keybinds
            if event.type == pg.KEYDOWN:
                # Jump
                if event.key == pg.K_SPACE or event.key == pg.K_UP or event.key == pg.K_w:
                    print("duck")
                    duck_position = player_jump(duck_position)
            # Check for QUIT event
            if event.type == pg.QUIT:
                running = False
        duck_position = move_player(duck_position)

        # Draw screen
        screen.fill(white)
        draw_clouds(screen)
        screen.blit(duck, duck_position)
        pg.display.update()

        clock.tick(clock.get_fps())
        clock.get_time()
        
    pg.quit()

### Player movement
def move_player(duck_position):
    x,y = duck_position
    if y < GROUND:
        y += 5
    return (x,y)

def player_jump(duck_position):
    x,y = duck_position
    return (x,y-70)

### Drawing
def draw_clouds(screen: pg.Surface):
    blue = (0,0,255)
    rect = pg.Rect(0,-150,640,300)
    pg.draw.ellipse(screen,blue, rect)


if __name__ == '__main__':
    main()
