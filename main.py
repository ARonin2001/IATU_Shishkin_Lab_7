import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import itertools
import time

def generate_schedules_with_constraints(n):
    players = list(range(1, n+1))
    all_matches = list(itertools.combinations(players, 2))
    best_schedule = None
    min_rounds = float('inf')

    for schedule in itertools.permutations(all_matches):
        rounds = []
        current_round = []
        for match in schedule:
            valid_round = True
            for p in match:
                if any(p in m for m in current_round):
                    valid_round = False
                    break
            if valid_round:
                current_round.append(match)
            else:
                rounds.append(current_round)
                current_round = [match]

        rounds.append(current_round)

        num_rounds = len(rounds)
        if num_rounds < min_rounds:
            min_rounds = num_rounds
            best_schedule = rounds

    return best_schedule, min_rounds


def calculate_and_display(N, output_text):
    try:
        if N < 2:
            output_text.insert(tk.END, "Число игроков должно быть не меньше 2.\n")
            return

        start_time = time.time()
        best_schedule, min_rounds = generate_schedules_with_constraints(N)
        end_time = time.time()

        output_text.insert(tk.END, f"Оптимальное расписание ({N} игроков): {min_rounds} раундов\n")
        output_text.insert(tk.END, f"Время выполнения: {end_time - start_time} сек.\n")
        output_text.insert(tk.END, f"Расписание: {best_schedule}\n")

    except ValueError:
        output_text.insert(tk.END, "Пожалуйста, введите целое число.\n")

def main():
	root = tk.Tk()		
	root.title("Расписание шахматного турнира")

	label = ttk.Label(root, text="Введите число игроков:")
	label.pack(pady=5)
	entry = ttk.Entry(root)
	entry.pack(pady=5)

	output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=10)
	output_text.pack(pady=5)

	button = ttk.Button(root, text="Рассчитать", 
		command=lambda: calculate_and_display(int(entry.get()), output_text) )
	button.pack(pady=10)

	root.mainloop()

if __name__ == "__main__":
	main()