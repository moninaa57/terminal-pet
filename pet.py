"""
🐾 Terminal Pet
Usage:
    python3 pet.py

Commands:
    feed   -> pet eats 🍗
    play   -> pet gets excited 🎮
    error  -> pet gets sad 💔
    exit   -> quit
"""
import random
import time
import os

class TerminalPet:
    def __init__(self, name="Mochi"):
        self.name = name
        self.mood = "happy"

    def show(self):
        faces = {
            "happy": "(=^‥^=)ﾉ",
            "sad": "(=；ェ；=)",
            "hungry": "(=ΦェΦ=)",
            "excited": "(=^･ω･^)y＝",
        }
        print(f"\n{self.name}: {faces.get(self.mood, '(=^‥^=)')}\n")

    def react(self, command):
        if command in ["error", "fail"]:
            self.mood = "sad"
            print(f"{self.name} is sad because of the error... 💔")
        elif command in ["feed", "eat"]:
            self.mood = "happy"
            print(f"{self.name} enjoyed the food 🍗")
        elif command in ["play", "fun"]:
            self.mood = "excited"
            print(f"{self.name} is playing around 🎮")
        else:
            self.mood = random.choice(["happy", "hungry"])
            print(f"{self.name} is just chilling... 😺")

        self.show()

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    pet = TerminalPet()
    clear()
    print("🐾 Welcome to Terminal Pet! Type 'exit' to quit.")
    pet.show()

    while True:
        cmd = input("👉 Enter a command: ").strip().lower()
        if cmd == "exit":
            print(f"Bye bye from {pet.name}! (=^･^=)ﾉ彡☆")
            break
        pet.react(cmd)
        time.sleep(1)

if __name__ == "__main__":
    main()
