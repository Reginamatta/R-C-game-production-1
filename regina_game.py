import pygame as pg
import player

WINSIZE = (640, 480)
WINCENTER = [320, 240]
GROUND = 420
NUMSTARS = 150

def main():
    pg.init()
    screen = pg.display.set_mode(WINSIZE)
    pg.display.set_caption("Regina Game")
    white = 255, 240, 240
    black = 20, 20, 20
    screen.fill(black)
    clock = pg.time.Clock()
    cloud = pg.image.load('Images/cute-cloud-simple-illustration-for-kids-drawing-png.png')
    cloud = pg.transform.scale(cloud,(100,100))
    duck = player.Player((50,50))
    duck2= player.Player((100,50))

    running = True
    while running:
        # game logic
        for event in pg.event.get():
            # Keybinds
            if event.type == pg.KEYDOWN:
                # Jump
                if event.key == pg.K_SPACE:
                    print("duck")
                    duck.jump()
                if  event.key == pg.K_w:
                    print("duck")
                    duck2.jump()
            # Check for QUIT event
            if event.type == pg.QUIT:
                running = False
        duck.move(GROUND)
        duck2.move(GROUND)

        # Draw screen
        screen.fill(white)
        draw_clouds(screen, cloud, WINCENTER)
        draw_floor(screen)
        duck.draw(screen)
        duck2.draw(screen)
        pg.display.update()
        clock.tick(60)
        
    pg.quit()

### Drawing
def draw_clouds(screen: pg.Surface, cloud, cloud_position):
    screen.blit(cloud, cloud_position)


def draw_floor ( screen: pg.Surface):
    color = (0,0,0)
    rect = pg.Rect(0,GROUND,WINSIZE[0], WINSIZE[1]- GROUND)
    pg.draw.rect(screen,color,rect)


if __name__ == '__main__':
    main()
