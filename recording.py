#!/usr/bin/python3
import os

import pygame.mixer

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"


class Recording:
    path: str

    @classmethod
    def play_recording(cls) -> None:
        pygame.mixer.init()
        pygame.mixer.music.load(cls.path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
