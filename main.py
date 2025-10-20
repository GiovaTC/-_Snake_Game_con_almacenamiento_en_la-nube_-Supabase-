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

