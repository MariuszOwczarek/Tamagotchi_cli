from dataclasses import dataclass


@dataclass
class Settings:
    # instance variables
    name: str = "Alibaba"
    age: int = 0
    max_age: int = 100
    max_energy: int = 100
    min_energy: int = 0
    start_energy: int = 50
    max_happiness: int = 100
    min_happiness: int = 0
    start_happiness: int = 70
    min_hunger: int = 0
    max_hunger: int = 100
    start_hunger: int = 50
    playtime_value: int = 10
    sleep_value: int = 10

    # ticks costs
    feed_tick: int = 2
    play_ticks: int = 3
    sleep_ticks: int = 5
    status_ticks: int = 1
    age_up_ticks: int = 20


DEFAULT_SETTINGS = Settings()
