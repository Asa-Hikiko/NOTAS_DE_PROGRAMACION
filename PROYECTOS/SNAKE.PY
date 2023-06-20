import pygame
import random

# Inicialización de Pygame
pygame.init()

# Definición de colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Definición de la ventana del juego
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Snake Game")

# Definición de la serpiente y su movimiento
SNAKE_SIZE = 10
snake_speed = 15
snake_x = WINDOW_WIDTH // 2
snake_y = WINDOW_HEIGHT // 2
snake_x_change = 0
snake_y_change = 0
snake_list = []
snake_length = 1

# Función para dibujar la serpiente
def draw_snake(snake_list):
    for x,y in snake_list:
        pygame.draw.rect(screen, GREEN, [x, y, SNAKE_SIZE, SNAKE_SIZE])

# Definición de la comida
FOOD_SIZE = 10
food_x = round(random.randrange(0, WINDOW_WIDTH - FOOD_SIZE) / 10.0) * 10.0
food_y = round(random.randrange(0, WINDOW_HEIGHT - FOOD_SIZE) / 10.0) * 10.0

# Función para dibujar la comida
def draw_food(food_x, food_y):
    pygame.draw.rect(screen, RED, [food_x, food_y, FOOD_SIZE, FOOD_SIZE])

# Definición del juego
game_over = False
clock = pygame.time.Clock()

# Bucle principal del juego
while not game_over:
    # Eventos del juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x_change = -SNAKE_SIZE
                snake_y_change = 0
            elif event.key == pygame.K_RIGHT:
                snake_x_change = SNAKE_SIZE
                snake_y_change = 0
            elif event.key == pygame.K_UP:
                snake_y_change = -SNAKE_SIZE
                snake_x_change = 0
            elif event.key == pygame.K_DOWN:
                snake_y_change = SNAKE_SIZE
                snake_x_change = 0

    # Actualización de la posición de la serpiente
    snake_x += snake_x_change
    snake_y += snake_y_change

    # Comprobación de colisión con los bordes de la ventana
    if snake_x < 0 or snake_x >= WINDOW_WIDTH or snake_y < 0 or snake_y >= WINDOW_HEIGHT:
        game_over = True

    # Comprobación de colisión con la comida
    if snake_x == food_x and snake_y == food_y:
        food_x = round(random.randrange(0, WINDOW_WIDTH - FOOD_SIZE) / 10.0) * 10.0
        food_y = round(random.randrange(0, WINDOW_HEIGHT - FOOD_SIZE) / 10.0) * 10.0
        snake_length += 1

    # Actualización de la lista de la serpiente
    snake_head = []
    snake_head.append(snake_x)
    snake_head.append(snake_y)
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]

    # Comprobación de colisión con uno mismo
    for segment in snake_list[:-1]:
        if segment == snake_head:
            game_over = True

    # Fondo de pantalla
    screen.fill(BLACK)

    # Dibujado de la serpiente y la comida
    draw_snake(snake_list)
    draw_food(food_x, food_y)

    # Actualización de la pantalla
    pygame.display.update()

    # Control de la velocidad de la serpiente
    clock.tick(snake_speed)

# Cierre del juego
pygame.quit()
quit()