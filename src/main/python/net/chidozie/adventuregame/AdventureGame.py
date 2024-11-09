import os
import pygame
from pygame import SurfaceType

from src.main.python.updater.UdateClient import UpdateClient


class AdventureGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))

        icon_path = 'additional/assets/images/Scorpion.png'
        pygame.display.set_caption('Adventure Game')
        if not os.path.exists(icon_path): url = 'https://1drv.ms/i/s!Ah_0Zcex0RSTh_5iXBPDWYy7j7NEkw?e=ClwspF'
        self.download_icon(url, icon_path)
        icon = pygame.image.load(icon_path)
        pygame.display.set_icon(icon)

        self.clock = pygame.time.Clock()
        self.running = True
        while self.running:
            self.handle_events()
            self.render()

    def download_icon(self, url, path):
        response = requests.get(url)

    with open(os.path, 'wb') as file:
        file.write(response.content)
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False



    def render(self):
        self.screen.fill((0, 0, 0))  # Black background
        pygame.display.flip()  # Update display


def main():
    AdventureGame()
    UpdateClient.update()
    pygame.quit()


if __name__ == "__main__":
    main()
