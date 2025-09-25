import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Snake starting position and size
block_size = 20
snake_start_x = screen_width // 2
snake_start_y = screen_height // 2 # center of the screen
snake_length = 1
snake_body = [[snake_start_x, snake_start_y]]  # list that store snake segments as [x, y] coordinates

# initial snake direction
snake_direction = "right"

# Game speed (frames per second)
game_speed = 10

# Food position
def generate_food():
    while True:
        food_x = random.randrange(0, screen_width - block_size, block_size) # generates positions that are multiples of block_size (so food aligns with grid)
        food_y = random.randrange(0, screen_height - block_size, block_size)
        # Make sure food doesn't spawn on snake
        if [food_x, food_y] not in snake_body:
            return food_x, food_y

food_x, food_y = generate_food()

# Score
score = 0

# Game Over Flag
game_over = False

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Game loop
running = True
clock = pygame.time.Clock() # object helps control the game speed

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake_direction != "right":
                snake_direction = "left"
            if event.key == pygame.K_RIGHT and snake_direction != "left":
                snake_direction = "right"
            if event.key == pygame.K_UP and snake_direction != "down":
                snake_direction = "up"
            if event.key == pygame.K_DOWN and snake_direction != "up":
                snake_direction = "down"
            # Prevents 180-degree turns (can't go right if moving left, etc.)

    # Only move if game is not over
    if not game_over:
        # Get current head position (first element in snake_body)
        head_x, head_y = snake_body[0]
        
        # Calculate new head position based on direction
        if snake_direction == "right":
            new_head = [head_x + block_size, head_y]
        elif snake_direction == "left":
            new_head = [head_x - block_size, head_y]
        elif snake_direction == "up":
            new_head = [head_x, head_y - block_size]
        elif snake_direction == "down":
            new_head = [head_x, head_y + block_size]

        # Insert new head at the beginning of snake body
        snake_body.insert(0, new_head)
        
        # Food consumption
        if snake_body[0][0] == food_x and snake_body[0][1] == food_y:
            # Generate new food
            food_x, food_y = generate_food()
            score += 1
            print("Score: " + str(score))
        else:
            # Remove tail if no food was eaten
            snake_body.pop()

        # Snake collision with walls
        if (snake_body[0][0] < 0 or snake_body[0][0] >= screen_width or 
            snake_body[0][1] < 0 or snake_body[0][1] >= screen_height):
            game_over = True

        # Snake collision with itself (skip first segment which is the head)
        if snake_body[0] in snake_body[1:]:
            game_over = True

    # Update the screen
    screen.fill(black)
    
    # Draw food
    pygame.draw.rect(screen, red, (food_x, food_y, block_size, block_size))

    # Draw snake
    for segment in snake_body:
        pygame.draw.rect(screen, green, (segment[0], segment[1], block_size, block_size))

    # Display score
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: " + str(score), True, white)
    screen.blit(score_text, (5, 5))
    
    # Display game over message
    if game_over:
        game_over_font = pygame.font.Font(None, 72)
        game_over_text = game_over_font.render("GAME OVER", True, white)
        screen.blit(game_over_text, (screen_width//2 - 150, screen_height//2 - 36))

    # Update the screen
    pygame.display.update()

    # Control the game speed - Make all the drawn elements visible on screen
    clock.tick(game_speed)

# Quit Pygame
pygame.quit()