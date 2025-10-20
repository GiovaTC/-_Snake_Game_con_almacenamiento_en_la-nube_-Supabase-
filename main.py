# Juego principal .
import pygame, sys, random, requests
from supabase_config import SUPABASE_URL, SUPABASE_KEY, SUPABASE_TABLE

pygame.init()
WIDTH, HEIGHT = 600, 400
CELL = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐍 Snake con Supabase")
clock = pygame.time.Clock()
font = pygame.font.SysFont("consolas", 25)

def subir_puntaje(nombre, puntaje):
    try:
        data = {"player": nombre, "score": puntaje}
        headers = {
            "apikey": SUPABASE_KEY,
            "Authorization": f"Bearer {SUPABASE_KEY}",
            "Content-Type": "application/json"
        }
        r = requests.post(f"{SUPABASE_URL}/rest/v1/{SUPABASE_TABLE}", json=data, headers=headers)
        if r.status_code in (200, 201):
            print("✅ Puntaje registrado en la nube!")
        else:
            print(f"⚠️ Error al registrar puntaje: {r.text}")
    except Exception as e:
        print(f"❌ No se pudo conectar a Supabase: {e}")

def dibujar_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, (0, 255, 0), (*segment, CELL, CELL))

def dibujar_food(food):
    pygame.draw.rect(screen, (255, 0, 0), (*food, CELL, CELL))

def main():
    snake = [(100, 100), (80, 100), (60, 100)]
    direction = (CELL, 0)
    food = (random.randrange(0, WIDTH, CELL), random.randrange(0, HEIGHT, CELL))
    score = 0
    player = input("👤 Nombre del jugador: ")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, CELL):
                    direction = (0, -CELL)
                if event.key == pygame.K_DOWN and direction != (0, -CELL):
                    direction = (0, CELL)
                if event.key == pygame.K_LEFT and direction != (CELL, 0):
                    direction = (-CELL, 0)
                if event.key == pygame.K_RIGHT and direction != (-CELL, 0):
                    direction = (CELL, 0)
        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        snake.insert(0, new_head)

        if new_head == food:
            score += 10
            food = (random.randrange(0, WIDTH, CELL), random.randrange(0, HEIGHT, CELL))
        else:
            snake.pop()

        if (
            new_head[0] < 0 or new_head[0] >= WIDTH or
            new_head[1] < 0 or new_head[1] >= HEIGHT or
            new_head in snake[1:]
        ):
            print(f"💀 Juego terminado. Puntaje final: {score}")
            subir_puntaje(player, score)
            pygame.quit()
            sys.exit()
        
        screen.fill((0, 0, 0))
        dibujar_snake(snake)
        dibujar_food(food)
        texto = font.render(f"puntaje: {score}", True, (255, 255, 255))
        screen.blit(texto, (10, 10))
        pygame.display.flip()
        clock.tick(10)

if __name__ == "__main__":
    main()
        

