import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 400
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pixel Jumper")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Player
player_size = 30
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - player_size - 10
player_speed = 5
player_jump = -12  # Reduced jump strength for easier control
player_gravity = 0.5  # Reduced gravity for slower falling

# Platforms
platform_width = 100  # Wider platforms
platform_height = 20
platform_count = 6
platforms = []

# Generate initial platforms
for i in range(platform_count):
    platform_x = random.randint(0, WIDTH - platform_width)
    platform_y = HEIGHT - (i + 1) * (HEIGHT // platform_count)
    platforms.append(
        pygame.Rect(platform_x, platform_y, platform_width, platform_height)
    )

# Add a starting platform
start_platform = pygame.Rect(
    WIDTH // 2 - platform_width // 2, HEIGHT - 50, platform_width, platform_height
)
platforms.append(start_platform)

# Game variables
clock = pygame.time.Clock()
running = True
player_vel_y = 0
score = 0
game_speed = 1  # Initial game speed

# Font
font = pygame.font.Font(None, 36)


# Game start message
def draw_start_message():
    start_text = font.render("Press SPACE to start", True, GREEN)
    window.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, HEIGHT // 2))


# Main game loop
game_started = False
while running:
    clock.tick(60)  # 60 FPS

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if (
            event.type == pygame.KEYDOWN
            and event.key == pygame.K_SPACE
            and not game_started
        ):
            game_started = True

    if not game_started:
        window.fill(BLACK)
        draw_start_message()
        pygame.display.update()
        continue

    # Move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    # Apply gravity
    player_vel_y += player_gravity
    player_y += player_vel_y

    # Check for platform collisions
    for platform in platforms:
        if (
            player_vel_y > 0
            and player_y + player_size > platform.top
            and player_y < platform.bottom
        ):
            if platform.left - player_size < player_x < platform.right:
                player_y = platform.top - player_size
                player_vel_y = player_jump

    # Move platforms down and create new ones
    if player_y < HEIGHT // 2:
        player_y += abs(player_vel_y)
        for platform in platforms:
            platform.y += abs(player_vel_y) * game_speed
            if platform.top > HEIGHT:
                platforms.remove(platform)
                new_platform = pygame.Rect(
                    random.randint(0, WIDTH - platform_width),
                    platform.y - HEIGHT,
                    platform_width,
                    platform_height,
                )
                platforms.append(new_platform)
                score += 1

                # Gradually increase game speed
                if score % 5 == 0:
                    game_speed += 0.1

    # Game over if player falls off screen
    if player_y > HEIGHT:
        running = False

    # Draw everything
    window.fill(BLACK)
    pygame.draw.rect(window, RED, (player_x, player_y, player_size, player_size))
    for platform in platforms:
        pygame.draw.rect(window, WHITE, platform)

    # Display score
    score_text = font.render(f"Score: {score}", True, WHITE)
    window.blit(score_text, (10, 10))

    pygame.display.update()

# Game over screen
game_over_text = font.render("Game Over", True, RED)
final_score_text = font.render(f"Final Score: {score}", True, WHITE)
restart_text = font.render("Press R to restart", True, GREEN)

window.blit(
    game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 50)
)
window.blit(
    final_score_text, (WIDTH // 2 - final_score_text.get_width() // 2, HEIGHT // 2 + 50)
)
window.blit(
    restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 100)
)
pygame.display.update()

# Wait for restart or quit
waiting = True
while waiting:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            waiting = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            # Restart the game
            exec(open(__file__).read())
            waiting = False

pygame.quit()
