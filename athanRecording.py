import config
import pygame.mixer
from abc import ABC, abstractmethod

pygame.mixer.init()


class AthanRecording(ABC):
    path: str

    def play_athan(self) -> None:
        pygame.mixer.music.load(self.path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue



