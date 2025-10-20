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

