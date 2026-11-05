from user_interface.ui import ConsoleUI
from gui.nine_morris_gui import NineMensMorrisGUI

def main():
    player_name = input("Enter your name: ").strip() or "Player"

    while True:
        print("\nSelect Interface:")
        print("1. Console UI")
        print("2. Graphical UI (Pygame)")

        try:
            choice = input("Choice (1 or 2): ").strip()
            if choice == "2":
                app = NineMensMorrisGUI()
                app.run()
                break
            elif choice == "1":
                app = ConsoleUI(player_name)
                app.run()
                break
            elif choice == "0":
                print("Exiting...")
                break
            else:
                raise ValueError("Invalid choice.")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()