import tkinter as tk
import tkinter.messagebox
import random


class RPGGame:
    def __init__(self, root):
        self.root = root
        root.title("Auto Clicker RPG")

        # Initialize game attributes
        self.score = 0
        self.health = 100
        self.shield_potion = 0
        self.life_potion = 0
        self.shield_active = False

        # Set up the game interface
        self.retry_game()

        # ASCII Art Animation

    def setup_ui(self):
        self.animation_frames = [
            """
            O
            /|\\
            / \\
        ---*--*----*---
    """,
            """
            O
              |  
             |\\
        ----*--*----*--
    """,
            """
            O
            /|\\
             /| 
        -----*--*----*-
    """,
            """
            O
              |  
             /\\ 
        ------*--*----*
    """,
            """
            O
            /|\\
             |\\
        *----*--*------
    """,
            """
            O
              |  
             /| 
        -*----*--*-----
    """,
            """
            O
            /|\\
             /\\ 
        --*----*--*----
    """,
            """
            O
              |  
             |\\
        ---*----*--*---
    """,

        ]

        self.current_frame = 0
        self.animation_label = tk.Label(
            self.root, text=self.animation_frames[self.current_frame], font=("Courier", 10))
        self.animation_label.pack(pady=10)

        self.score_label = tk.Label(
            self.root, text="Money: " + str(self.score))
        self.score_label.pack(pady=10)

        self.health_label = tk.Label(
            self.root, text="Health: " + str(self.health))
        self.health_label.pack(pady=10)

        # Inventory
        self.inventory_label = tk.Label(self.root, text="Inventory")
        self.inventory_label.pack(pady=10)

        self.life_potion_label = tk.Label(
            self.root, text="Life Potions: " + str(self.life_potion))
        self.life_potion_label.pack(pady=5)

        self.shield_potion_label = tk.Label(
            self.root, text="Shield Potions: " + str(self.shield_potion))
        self.shield_potion_label.pack(pady=5)

        # Buttons
        self.fight_button = tk.Button(
            self.root, text="Fight", command=self.fight)
        self.fight_button.pack(pady=10)

        self.shop_button = tk.Button(self.root, text="Shop", command=self.shop)
        self.shop_button.pack(pady=10)

        self.retry_button = tk.Button(
            self.root, text="Retry", command=self.retry_game)
        self.retry_button.pack(pady=10)
        self.retry_button.config(state="disabled")

        self.root.after(500, self.update_animation)  # Start the animation
        self.root.after(10000, self.increment_money)

    def update_animation(self):
        self.current_frame = (self.current_frame +
                              1) % len(self.animation_frames)
        self.animation_label.config(
            text=self.animation_frames[self.current_frame])
        self.root.after(500, self.update_animation)

    def increment_money(self):
        self.score += random.randint(1, 5)
        self.update_labels()
        self.root.after(10000, self.increment_money)

    def update_labels(self):
        self.score_label.config(text="Money: " + str(self.score))
        self.health_label.config(text="Health: " + str(self.health))
        self.life_potion_label.config(
            text="Life Potions: " + str(self.life_potion))
        self.shield_potion_label.config(
            text="Shield Potions: " + str(self.shield_potion))

    def game_over(self):
        if self.health <= 0:
            self.fight_button.config(state="disabled")
            self.shop_button.config(state="disabled")
            self.retry_button.config(state="normal")
            game_over_label = tk.Label(
                self.root, text="Game Over!", font=("Arial", 24), fg="red")
            game_over_label.pack(pady=20)

    def retry_game(self):
        attributes_to_destroy = [
            'animation_label',
            'score_label',
            'health_label',
            'life_potion_label',
            'shield_potion_label',
            'fight_button',
            'shop_button',
            'retry_button'
        ]

        for attribute in attributes_to_destroy:
            if hasattr(self, attribute):
                getattr(self, attribute).destroy()

        self.setup_ui()

    def fight(self):
        if not self.shield_active:
            self.health -= random.randint(5, 20)
            if self.health < 0:
                self.health = 0
            self.game_over()
        else:
            self.shield_active = False

        reward = random.randint(10, 50)
        self.score += reward

        potion_chance = random.random()
        if potion_chance > 0.8:
            self.life_potion += 1
        elif potion_chance > 0.6:
            self.shield_potion += 1

        self.update_labels()

    def shop(self):
        if self.score >= 20 and self.life_potion > 0:
            use_life_potion = tk.messagebox.askyesno(
                "Shop", "Buy a life potion for 20 money?")
            if use_life_potion:
                self.score -= 20
                self.health += 30
                self.life_potion -= 1
                if self.health > 100:
                    self.health = 100

        if self.score >= 40 and self.shield_potion > 0:
            use_shield_potion = tk.messagebox.askyesno(
                "Shop", "Buy a shield potion for 40 money?")
            if use_shield_potion:
                self.score -= 40
                self.shield_active = True
                self.shield_potion -= 1

        self.update_labels()


if __name__ == "__main__":
    root = tk.Tk()
    game = RPGGame(root)
    root.mainloop()
