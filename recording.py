import pygame.mixer

pygame.mixer.init()


class Recording:
    path: str

    def play_recording(self) -> None:
        pygame.mixer.music.load(self.path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue



