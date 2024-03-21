import pygame


class Button:
    button_width = 100
    button_height = 50
    button_x = 50
    button_y = 50
    color = (130, 130, 130, 255)

    def get_dims(self):
        return self.button_x, self.button_y, self.button_width, self.button_height

    def draw_button(self, screen):
        button_x, button_y, button_width, button_height = self.get_dims()

        pygame.draw.rect(screen, self.color, (button_x, button_y, button_width, button_height))

        # Add text to the button
        font = pygame.font.Font(None, 36)
        text = font.render("Button", True, (0, 0, 0, 255))
        text_rect = text.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))
        screen.blit(text, text_rect)
