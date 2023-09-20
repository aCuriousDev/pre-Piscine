import tkinter as tk
from tkinter import messagebox
import random


class RPGGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Auto-Clicker RPG")

        self.money = 0
        self.health = 100
        self.life_potions = 0
        self.shield_potions = 0
        self.shield_active = False

        self.setup_ui()
        self.money_generation()

    def setup_ui(self):
        self.score_label = tk.Label(self.root, text=f"Money: {self.money}")
        self.score_label.pack(pady=10)

        self.health_label = tk.Label(self.root, text=f"Health: {self.health}")
        self.health_label.pack(pady=10)

        self.inventory_label = tk.Label(
            self.root, text=f"Life Potions: {self.life_potions} | Shield Potions: {self.shield_potions}")
        self.inventory_label.pack(pady=10)

        self.shop_button = tk.Button(
            self.root, text="Shop", command=self.open_shop)
        self.shop_button.pack(pady=10)

        self.fight_button = tk.Button(
            self.root, text="Fight", command=self.fight)
        self.fight_button.pack(pady=10)

        self.use_life_potion_button = tk.Button(
            self.root, text="Use Life Potion", command=self.use_life_potion)
        self.use_life_potion_button.pack(pady=10)

        self.use_shield_potion_button = tk.Button(
            self.root, text="Use Shield Potion", command=self.use_shield_potion)
        self.use_shield_potion_button.pack(pady=10)

    def money_generation(self):
        self.money += 10
        self.score_label.config(text=f"Money: {self.money}")
        self.root.after(5000, self.money_generation)

    def open_shop(self):
        shop_window = tk.Toplevel(self.root)
        shop_window.title("Shop")

        life_potion_button = tk.Button(
            shop_window, text="Buy Life Potion (50 Money)", command=lambda: self.buy_item("life_potion"))
        life_potion_button.pack(pady=10)

        shield_potion_button = tk.Button(
            shop_window, text="Buy Shield Potion (100 Money)", command=lambda: self.buy_item("shield_potion"))
        shield_potion_button.pack(pady=10)

    def buy_item(self, item):
        if item == "life_potion" and self.money >= 50:
            self.money -= 50
            self.life_potions += 1
        elif item == "shield_potion" and self.money >= 100:
            self.money -= 100
            self.shield_potions += 1
        self.update_labels()

    def fight(self):
        if self.shield_active:
            self.shield_active = False
            reward = random.choice(["money", "life_potion", "shield_potion"])
            if reward == "money":
                self.money += 50
                messagebox.showinfo("Fight Result", "You won 50 money!")
            elif reward == "life_potion":
                self.life_potions += 1
                messagebox.showinfo("Fight Result", "You won a life potion!")
            else:
                self.shield_potions += 1
                messagebox.showinfo("Fight Result", "You won a shield potion!")
        else:
            damage = random.randint(10, 50)
            self.health -= damage
            reward = random.choice(["money", "life_potion", "shield_potion"])
            if reward == "money":
                self.money += 50
                messagebox.showinfo(
                    "Fight Result", f"You took {damage} damage and won 50 money!")
            elif reward == "life_potion":
                self.life_potions += 1
                messagebox.showinfo(
                    "Fight Result", f"You took {damage} damage and won a life potion!")
            else:
                self.shield_potions += 1
                messagebox.showinfo(
                    "Fight Result", f"You took {damage} damage and won a shield potion!")
        self.update_labels()
        self.check_game_over()

    def check_game_over(self):
        if self.health <= 0:
            messagebox.showinfo("Game Over", "You have been defeated!")
            self.root.destroy()

    def use_life_potion(self):
        if self.life_potions > 0:
            self.life_potions -= 1
            self.health += 30
            if self.health > 100:
                self.health = 100
            self.update_labels()

    def use_shield_potion(self):
        if self.shield_potions > 0:
            self.shield_potions -= 1
            self.shield_active = True
            self.update_labels()

    def update_labels(self):
        self.score_label.config(text=f"Money: {self.money}")
        self.health_label.config(text=f"Health: {self.health}")
        self.inventory_label.config(
            text=f"Life Potions: {self.life_potions} | Shield Potions: {self.shield_potions}")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    game = RPGGame()
    game.run()
