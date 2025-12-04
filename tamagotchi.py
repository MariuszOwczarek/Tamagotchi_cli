from settings import Settings, DEFAULT_SETTINGS


class Tamagotchi:
    def __init__(self, settings: Settings = DEFAULT_SETTINGS):
        self.settings = settings
        self.name = self.settings.name
        self.age = self.settings.age
        self.max_age = self.settings.max_age
        self.max_energy = self.settings.max_energy
        self.min_energy = self.settings.min_energy
        self.__energy = self.settings.start_energy
        self.min_hunger = self.settings.min_hunger
        self.max_hunger = self.settings.max_hunger
        self.__hunger = self.settings.start_hunger
        self.max_happiness = self.settings.max_happiness
        self.min_happiness = self.settings.min_happiness
        self.__happiness = self.settings.start_happiness
        self._ticks_elapsed = 0
        self._is_alive = True

    @property
    def hunger(self):
        return self.__hunger

    @hunger.setter
    def hunger(self, value):
        self.__hunger = value

    @property
    def happiness(self):
        return self.__happiness

    @happiness.setter
    def happiness(self, value):
        self.__happiness = value

    @property
    def energy(self):
        return self.__energy

    @energy.setter
    def energy(self, value):
        self.__energy = value

    def feed(self, feed_value):
        self.hunger = self.hunger - feed_value
        self.happiness += 1
        self.__clamp_values()
        print(f'Feed: -{feed_value} starvation')
        return (self.hunger, self.happiness)

    def play(self, playtime_value):
        self.happiness = self.happiness + playtime_value
        self.energy = self.energy - playtime_value
        self.hunger = self.hunger + playtime_value // 2
        self.__clamp_values()
        print(f'Play: -{playtime_value} boredom')
        return (self.happiness, self.energy, self.hunger)

    def sleep(self, sleep_value):
        self.energy = self.energy + sleep_value
        self.happiness += 1
        self.hunger = self.hunger + sleep_value // 2
        self.__clamp_values()
        print(f'Sleep: -{sleep_value} exhaustion')
        return (self.energy, self.happiness)

    def __clamp_values(self):
        self.hunger = min(max(self.hunger, self.min_hunger), self.max_hunger)
        self.energy = min(max(self.energy, self.min_energy), self.max_energy)
        self.happiness = min(max(self.happiness, self.min_happiness),
                             self.max_happiness)

    def __maybe_age_up(self):
        if self._ticks_elapsed >= self.settings.age_up_ticks:
            self.age += 1
            self._ticks_elapsed -= self.settings.age_up_ticks
            print(f'Age: {self.age}')
        return self.age

    def __check_life_conditions(self):
        if self.hunger >= self.max_hunger:
            print('Died of Starvation')
            self._is_alive = False
            return
        if self.energy <= self.min_energy:
            print('Died of Exhaustion')
            self._is_alive = False
        if self.happiness <= self.min_happiness:
            print('Died of Boredom')
            self._is_alive = False
        if self.age >= self.max_age:
            print('Died of Old Age')
            self._is_alive = False
        if not self._is_alive:
            print(self.status())
            return
        print(self.status())
        return self._is_alive

    def __apply_tick_decay(self, n=1):
        self.hunger += 2*n
        self.energy -= 2*n
        if self.hunger > 80:
            self.happiness -= 3*n
        self.__clamp_values()
        return (self.hunger, self.energy, self.happiness)

    def tick(self, n=1):
        self._ticks_elapsed += n
        self.__apply_tick_decay(n)
        self.__maybe_age_up()
        self.__check_life_conditions()

    def status(self):
        info = {"Name": self.name,
                "Age": self.age,
                "Energy": self.energy,
                "Hunger": self.hunger,
                "Happiness": self.happiness}
        return info
