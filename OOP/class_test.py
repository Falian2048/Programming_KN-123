from rich import print
import tkinter as tk
from tkinter import ttk


class Cat1:
    def __init__(self, name="[bold red][Default name][/bold red]", age=0, color="[bold red][Default color][/bold red]",
                 sound="[bold red][Default sound][/bold red]"):
        self.name = name
        self.age = age
        self.color = color
        self.sound = sound
        print(f"Animal: {self.age} years old {self.color} {self.name} is created")

    def speak(self):
        print(f"{self.age} years old {self.color}, {self.name} says {self.sound}")


class CatGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Cat Creator")

        # Input fields
        ttk.Label(self.root, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = ttk.Entry(self.root)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.root, text="Age:").grid(row=1, column=0, padx=5, pady=5)
        self.age_entry = ttk.Entry(self.root)
        self.age_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.root, text="Color:").grid(row=2, column=0, padx=5, pady=5)
        self.color_entry = ttk.Entry(self.root)
        self.color_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(self.root, text="Sound:").grid(row=3, column=0, padx=5, pady=5)
        self.sound_entry = ttk.Entry(self.root)
        self.sound_entry.grid(row=3, column=1, padx=5, pady=5)

        # Buttons
        ttk.Button(self.root, text="Create Cat", command=self.create_cat).grid(row=4, column=0, columnspan=2, pady=10)
        ttk.Button(self.root, text="Make Sound", command=self.make_sound).grid(row=5, column=0, columnspan=2, pady=5)

        self.cat = None
        self.root.mainloop()

    def create_cat(self):
        name = self.name_entry.get() or "[bold red][Default name][/bold red]"
        age = int(self.age_entry.get()) if self.age_entry.get() else 0
        color = self.color_entry.get() or "[bold red][Default color][/bold red]"
        sound = self.sound_entry.get() or "[bold red][Default sound][/bold red]"
        self.cat = Cat1(name, age, color, sound)

    def make_sound(self):
        if self.cat:
            self.cat.speak()
        else:
            print("Create a cat first!")


if __name__ == "__main__":
    CatGUI()
