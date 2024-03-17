import pygame

class Text_box:
    def __init__(self, x, y, width, height, font_size=24):
        self.rect = pygame.Rect(x, y, width, height)
        self.font = pygame.font.Font("assets/fonts/arcade.ttf", font_size)
        self.lines = []
        self.current_line = 0

    def set_text(self, text_lines):
        self.text_lines = text_lines

    def next_line(self):
        self.current_line += 1
        if self.current_line >= len(self.text_lines):
            self.current_line = len(self.text_lines) - 1

    def draw(self, screen, x, y):
        self.rect.x = x
        self.rect.y = y
        pygame.draw.rect(screen, "white", self.rect)
        pygame.draw.rect(screen, "black", self.rect, 3)
        for i, line in enumerate(self.text_lines[self.current_line]):
            text = self.font.render(line, True, "black")
            text_rect = text.get_rect(left=self.rect.left + 15, top=self.rect.y + i * (self.font.get_linesize()) + 10)
            screen.blit(text, text_rect)
