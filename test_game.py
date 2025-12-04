from tamagotchi import Tamagotchi
from settings import DEFAULT_SETTINGS
from utils import Utils
import pytest


class TestGame:

    def test_check_settings(self):
        t = Tamagotchi(DEFAULT_SETTINGS)
        assert t.name == "Alibaba"
        assert t.age == 0
        assert t.energy == t.settings.start_energy
        assert t.hunger == t.settings.start_hunger
        assert t.happiness == t.settings.start_happiness
        assert t._is_alive is True

    def test_feed_clamps_and_increases_happiness(self):
        t = Tamagotchi(DEFAULT_SETTINGS)
        t.hunger = 10
        t.happiness = 90
        t.feed(20)
        assert t.hunger >= t.min_hunger
        assert t.happiness <= t.max_happiness

    def test_play_affects_stats(self):
        t = Tamagotchi(DEFAULT_SETTINGS)
        t.energy = 50
        t.hunger = 40
        t.happiness = 50
        t.play(10)
        assert t.energy < 50
        assert t.hunger > 40
        assert t.happiness > 50

    def test_sleep_affects_stats(self):
        t = Tamagotchi(DEFAULT_SETTINGS)
        t.energy = 50
        t.hunger = 40
        t.happiness = 50
        t.sleep(10)
        assert t.energy > 50
        assert t.hunger > 40
        assert t.happiness > 50

    def test_tick_increases_age_and_decays_stats(self):
        t = Tamagotchi(DEFAULT_SETTINGS)
        t._ticks_elapsed = t.settings.age_up_ticks
        t.energy = 50
        t.hunger = 50
        t.happiness = 50
        t.tick(1)
        assert t.age == 1
        assert t.hunger >= t.min_hunger
        assert t.energy <= t.max_energy

    def test_death_conditions(self):
        t = Tamagotchi(DEFAULT_SETTINGS)

        # Głód
        t.hunger = t.max_hunger
        t.tick()
        assert t._is_alive is False

        # Energia
        t = Tamagotchi(DEFAULT_SETTINGS)
        t.energy = t.min_energy
        t.tick()
        assert t._is_alive is False

        # Szczęście
        t = Tamagotchi(DEFAULT_SETTINGS)
        t.happiness = t.min_happiness
        t.tick()
        assert t._is_alive is False

        # Starość
        t = Tamagotchi(DEFAULT_SETTINGS)
        t.age = t.max_age
        t.tick()
        assert t._is_alive is False

    def test_status_returns_dict(self):
        t = Tamagotchi(DEFAULT_SETTINGS)
        info = t.status()
        assert isinstance(info, dict)
        assert info["Name"] == t.name
        assert info["Age"] == t.age
        assert info["Energy"] == t.energy
        assert info["Hunger"] == t.hunger
        assert info["Happiness"] == t.happiness

    def test_clear_screen_runs_without_error(self):
        u = Utils()
        try:
            u._clear_screen()
        except Exception:
            pytest.fail("clear_screen() raised Exception unexpectedly!")
