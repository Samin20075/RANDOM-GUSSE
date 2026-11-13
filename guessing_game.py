import random
from datetime import datetime

FILE_NAME = "game_data.csv"
MAX_ATTEMPTS = 7


def save_result(player, secret, attempts, won):
    """Ek game ka result file mein save karta hai."""
    # Pehle check karo file pehle se hai ya nahi
    try:
        with open(FILE_NAME, "r") as f:
            file_exists = True
    except FileNotFoundError:
        file_exists = False

    # "a" mode = append, purana data delete nahi hota
    with open(FILE_NAME, "a") as f:
        if not file_exists:
            f.write("date,player,secret,attempts,result\n")  # header
        result = "Win" if won else "Lose"
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        f.write(f"{now},{player},{secret},{attempts},{result}\n")


def play_game(player):
    """Ek poora game khelta hai."""
    secret = random.randint(1, 100)
    attempts = 0
    won = False

    print(f"\nMaine 1 se 100 ke beech ek number socha hai. {MAX_ATTEMPTS} chances hain!")

    while attempts < MAX_ATTEMPTS:
        try:
            guess = int(input(f"Attempt {attempts + 1}: "))
        except ValueError:
            print("Bhai number daal, text nahi!")
            continue  # attempt count nahi badhega

        attempts += 1

        if guess == secret:
            print(f"Sahi pakda! {attempts} attempts mein jeet gaya!")
            won = True
            break
        elif guess < secret:
            print("Thoda bada number soch.")
        else:
            print("Thoda chhota number soch.")

    if not won:
        print(f"Game over! Number tha {secret}.")

    save_result(player, secret, attempts, won)


def show_stats():
    """File padh ke total games aur wins dikhata hai."""
    try:
        with open(FILE_NAME, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Abhi tak koi game nahi khela.")
        return

    games = lines[1:]  # pehli line header hai, skip
    total = len(games)
    wins = 0
    for line in games:
        if line.strip().endswith("Win"):
            wins += 1

    print(f"\nTotal games: {total}")
    print(f"Wins: {wins}")
    print(f"Losses: {total - wins}")
    if total > 0:
        print(f"Win rate: {wins / total * 100:.1f}%")


def main():
    player = input("Apna naam bata: ").strip().replace(",", "")

    while True:
        print("\n--- MENU ---")
        print("1. Game khel")
        print("2. Stats dekh")
        print("3. Exit")
        choice = input("Choice: ")

        if choice == "1":
            play_game(player)
        elif choice == "2":
            show_stats()
        elif choice == "3":
            print("Bye bhai!")
            break
        else:
            print("1, 2 ya 3 daal.")


main()