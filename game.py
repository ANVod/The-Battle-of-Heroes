import random


class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона.")

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        turn = 0
        while self.player.is_alive() and self.computer.is_alive():
            if turn % 2 == 0:
                self.player.attack(self.computer)
                print(f"У {self.computer.name} осталось {self.computer.health} здоровья.\n")
            else:
                self.computer.attack(self.player)
                print(f"У {self.player.name} осталось {self.player.health} здоровья.\n")
            turn += 1

        if self.player.is_alive():
            print(f"{self.player.name} побеждает!")
        else:
            print(f"{self.computer.name} побеждает!")


# Создание героев
player_name = input("Введите ваше имя героя: ")
player = Hero(player_name)
computer = Hero("Компьютер", 100, random.randint(15, 25))

# Запуск игры
game = Game(player, computer)
game.start()