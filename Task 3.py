import tkinter as tk
import random

OPTIONS = ['Rock', 'Paper', 'Scissors']

RULES = {
    ('Rock', 'Scissors'): 'win',
    ('Paper', 'Rock'): 'win',
    ('Scissors', 'Paper'): 'win',
    ('Scissors', 'Rock'): 'lose',
    ('Rock', 'Paper'): 'lose',
    ('Paper', 'Scissors'): 'lose'
}

class RPSGame:
    def __init__(self, master):
        self.master = master
        master.title("Rock Paper Scissors")
        master.geometry("400x430")
        master.resizable(False, False)
        self.user_score = 0
        self.comp_score = 0
        self.round_num = 1

        self.label_title = tk.Label(master, text="Rock Paper Scissors", font=("Arial", 22, "bold"))
        self.label_title.pack(pady=20)

        self.label_instructions = tk.Label(master, text="Choose your move:", font=("Arial", 13))
        self.label_instructions.pack()

        # Game buttons
        self.frame_buttons = tk.Frame(master)
        self.frame_buttons.pack(pady=10)
        for opt in OPTIONS:
            tk.Button(
                self.frame_buttons, text=opt, width=10, height=2, font=("Arial", 13),
                command=lambda o=opt: self.user_choice(o)
            ).pack(side='left', padx=8)

        # Results & Scoreboard
        self.label_round = tk.Label(master, text=f"Round: {self.round_num}", font=("Arial", 12))
        self.label_round.pack(pady=10)
        self.label_result = tk.Label(master, text="", font=("Arial", 13, "bold"), fg="navy")
        self.label_result.pack()
        self.label_user_choice = tk.Label(master, text="", font=("Arial", 12))
        self.label_user_choice.pack()
        self.label_comp_choice = tk.Label(master, text="", font=("Arial", 12))
        self.label_comp_choice.pack()
        self.label_scores = tk.Label(master, text=self._score_text(), font=("Arial", 14))
        self.label_scores.pack(pady=15)

        self.button_play_again = tk.Button(
            master, text="Play Again", font=("Arial", 11), command=self.play_again, state='disabled'
        )
        self.button_play_again.pack(pady=8)

    def _score_text(self):
        return f"Score — You: {self.user_score}  |  Computer: {self.comp_score}"

    def user_choice(self, user_pick):
        self.label_result.config(text="")
        self.label_user_choice.config(text="")
        self.label_comp_choice.config(text="")
        self.button_play_again.config(state='disabled')

        comp_pick = random.choice(OPTIONS)
        self.label_user_choice.config(text=f"You chose:      {user_pick}")
        self.label_comp_choice.config(text=f"Computer chose: {comp_pick}")
        if user_pick == comp_pick:
            result = "It's a Tie!"
        else:
            outcome = RULES.get((user_pick, comp_pick))
            if outcome == 'win':
                result = "You Win! 🎉"
                self.user_score += 1
            else:
                result = "Computer Wins! 😢"
                self.comp_score += 1
        self.label_result.config(text=result)
        self.label_scores.config(text=self._score_text())
        self.button_play_again.config(state='normal')
        for button in self.frame_buttons.winfo_children():
            button.config(state='disabled')

    def play_again(self):
        self.round_num += 1
        self.label_round.config(text=f"Round: {self.round_num}")
        self.label_result.config(text="")
        self.label_user_choice.config(text="")
        self.label_comp_choice.config(text="")
        self.button_play_again.config(state='disabled')
        for button in self.frame_buttons.winfo_children():
            button.config(state='normal')

if __name__ == "__main__":
    root = tk.Tk()
    game = RPSGame(root)
    root.mainloop()
