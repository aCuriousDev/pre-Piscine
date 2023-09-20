import tkinter as tk
import tkinter.messagebox
import random


class RPGGame:
    def __init__(self, root):
        self.root = root
        root.title("Auto Clicker RPG")

        # Initialize game attributes and UI elements
        self.score_var = tk.StringVar()
        self.health_var = tk.StringVar()
        self.life_potion_var = tk.StringVar()
        self.shield_potion_var = tk.StringVar()

        self.setup_ui()

        # Initialize game attributes
        self.score = 0
        self.health = 100
        self.shield_potion = 1
        self.life_potion = 1
        self.shield_active = False

        self.update_labels()

        # Start the animation and money increment
        self.root.after(250, self.update_animation)
        self.root.after(5000, self.increment_money)

    def setup_ui(self):
        # ASCII Art Animation
        self.animation_frames = [
            '''
            O
            /|\\
            / \\
        ---*--*----*---
    ''',
            '''
            O
              |  
             |\\
        ----*--*----*--
    ''',
            '''
            O
            /|\\
             /| 
        -----*--*----*-
    ''',
            '''
            O
              |  
             /\\ 
        ------*--*----*
    ''',
            '''
            O
            /|\\
             |\\
        *----*--*------
    ''',
            '''
            O
              |  
             /| 
        -*----*--*-----
    ''',
            '''
            O
            /|\\
             /\\ 
        --*----*--*----
    ''',
            '''
            O
              |  
             |\\
        ---*----*--*---
    ''',
        ]

        self.current_frame = 0
        self.animation_label = tk.Label(
            self.root, text=self.animation_frames[self.current_frame], font=("Courier", 10))
        self.animation_label.pack(pady=10)

        self.score_label = tk.Label(self.root, textvariable=self.score_var)
        self.score_label.pack(pady=10)

        self.health_label = tk.Label(self.root, textvariable=self.health_var)
        self.health_label.pack(pady=10)

        # Inventory
        self.inventory_label = tk.Label(self.root, text="Inventory")
        self.inventory_label.pack(pady=10)

        self.life_potion_label = tk.Label(
            self.root, textvariable=self.life_potion_var)
        self.life_potion_label.pack(pady=5)

        self.shield_potion_label = tk.Label(
            self.root, textvariable=self.shield_potion_var)
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

    def update_animation(self):
        self.current_frame = (self.current_frame +
                              1) % len(self.animation_frames)
        self.animation_label.config(
            text=self.animation_frames[self.current_frame])
        self.root.after(500, self.update_animation)

    def increment_money(self):
        self.score += random.randint(5, 10)
        self.update_labels()
        self.root.after(6000, self.increment_money)

    def update_labels(self):
        self.score_var.set("Money: " + str(self.score))
        self.health_var.set("Health: " + str(self.health))
        self.life_potion_var.set("Life Potions: " + str(self.life_potion))
        self.shield_potion_var.set(
            "Shield Potions: " + str(self.shield_potion))

    def game_over(self):
        if self.health <= 0:
            self.fight_button.config(state="disabled")
            self.shop_button.config(state="disabled")
            self.retry_button.config(state="normal")
            tk.Label(self.root, text="Game Over!", font=(
                "Arial", 24), fg="red").pack(pady=20)

    def retry_game(self):
        # Destroy existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        # Reset game attributes
        self.score = 0
        self.health = 100
        self.shield_potion = 0
        self.life_potion = 0
        self.shield_active = False

        # Set up the game interface again
        self.setup_ui()
        self.update_labels()

    def fight(self):
        if not self.shield_active:
            self.health -= random.randint(5, 20)
            if self.health < 0:
                self.health = 0
            self.game_over()
        else:
            self.shield_active = False

        reward = random.randint(10, 100)
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
