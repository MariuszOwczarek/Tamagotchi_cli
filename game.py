from settings import Settings, DEFAULT_SETTINGS
from tamagotchi import Tamagotchi
import sys
from utils import Utils


class Game:
    def __init__(self, settings: Settings = DEFAULT_SETTINGS):
        self.settings = settings
        self.tamagotchi = Tamagotchi(settings)
        self.utils = Utils()

    def info(self):
        print("""
             ================ TAMAGOTCHI ================
                        Select one of the Options:
                        1. Feed
                        2. Play
                        3. Sleep
                        4. Status
                        Q. Exit
             ============================================
             """)

    def run(self):
        while self.tamagotchi._is_alive:
            self.utils._clear_screen()
            self.info()
            self.tamagotchi.status()
            choice = input("Choosen Action: ").strip().lower()

            match choice:
                case '1':
                    value = int(input("How much food to give? "))
                    self.tamagotchi.feed(value)
                    self.tamagotchi.tick(self.settings.feed_tick)

                case '2':
                    value = int(input("How long to play? "))
                    self.tamagotchi.play(value)
                    self.tamagotchi.tick(self.settings.play_ticks)

                case '3':
                    value = int(input("How long to Sleep? "))
                    self.tamagotchi.sleep(value)
                    self.tamagotchi.tick(self.settings.sleep_ticks)

                case '4':
                    self.tamagotchi.tick(self.settings.sleep_ticks)

                case 'q':
                    print("Quit game.")
                    sys.exit()

                case _:
                    print("Wrong Action Chosen !")

        print("Your Tamagotchi is Dead. Game Over.")
