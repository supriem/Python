import pygame
from .constants import BLACK, ROWS, RED, SQUARE_SIZE  # We are in same package so use .
class Board:
	def __init__(self):
		self.board  = []
		self.selected_piece = None
		self.red_left = self.while_left = 12
		self.red_kings = self.white_kings = 0

	def draw_squares(self, win):
		win.fill(BLACK)
		for row in range(ROWS):
			for col in range(row % 2, ROWS, 2):
				pygame.draw.rect(win, RED, (row* SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE) )

