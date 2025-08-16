import tkinter as tk
import random

# --- Theme Settings: Cute Pastel Animal ---
BG_COLOR = "#FFF7F0"
TITLE_COLOR = "#FFB3C6"
BUTTON_BG = "#EBDFFC"
BUTTON_ACTIVE_BG = "#D3EDF7"
LABEL_COLOR = "#6B5B95"
RESULT_WIN = "🎉"
RESULT_LOSE = "😢"
RESULT_TIE = "🤝"
EMOJI_MAP = {
    'Rock': '🐶',     # Dog
    'Paper': '🐱',    # Cat
    'Scissors': '🐰'  # Rabbit
}
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
        master.geometry("400x435")
        master.configure(bg=BG_COLOR)
        master.resizable(False, False)
        self.user_score = 0
        self.comp_score = 0
        self.round_num = 1

        self.label_title = tk.Label(
            master, text="Rock 🐶 Paper 🐱 Scissors 🐰", 
            font=("Comic Sans MS", "18", "bold"), bg=TITLE_COLOR, fg="white"
        )
        self.label_title.pack(pady=18, fill=tk.X)

        self.label_instructions = tk.Label(
            master, text="Choose your move:",
            font=("Arial", 13), bg=BG_COLOR, fg=LABEL_COLOR
        )
        self.label_instructions.pack()

        # --- Game buttons with Animal Emojis
        self.frame_buttons = tk.Frame(master, bg=BG_COLOR)
        self.frame_buttons.pack(pady=12)
        self.buttons = {}
        for opt in OPTIONS:
            btn = tk.Button(
                self.frame_buttons,
                text=f"{EMOJI_MAP[opt]} {opt}",
                width=10, height=2,
                font=("Arial", 12, "bold"),
                bg=BUTTON_BG, fg=LABEL_COLOR,
                activebackground=BUTTON_ACTIVE_BG,
                relief="solid", bd=1,
                command=lambda o=opt: self.user_choice(o)
            )
            btn.pack(side='left', padx=9)
            self.buttons[opt] = btn

        # --- Results & Scoreboard
        self.label_round = tk.Label(master, text=f"Round: {self.round_num}",
                                    font=("Arial", 12), bg=BG_COLOR, fg=LABEL_COLOR)
        self.label_round.pack(pady=7)
        self.label_result = tk.Label(master, text="", font=("Arial", 14, "bold"), fg="#FFB3C6", bg=BG_COLOR)
        self.label_result.pack()
        self.label_user_choice = tk.Label(master, text="", font=("Arial", 12), bg=BG_COLOR)
        self.label_user_choice.pack()
        self.label_comp_choice = tk.Label(master, text="", font=("Arial", 12), bg=BG_COLOR)
        self.label_comp_choice.pack()
        self.label_scores = tk.Label(master, text=self._score_text(),
                                    font=("Arial", 14, "bold"), bg=BG_COLOR, fg=LABEL_COLOR)
        self.label_scores.pack(pady=13)

        self.button_play_again = tk.Button(
            master, text="🔄 Play Again", font=("Arial", 12, "bold"),
            command=self.play_again, state='disabled',
            bg="#FDF2F8", fg=LABEL_COLOR, relief="solid", bd=1,
            activebackground="#E4DCED"
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
        self.label_user_choice.config(text=f"You chose:      {EMOJI_MAP[user_pick]} {user_pick}")
        self.label_comp_choice.config(text=f"Computer chose: {EMOJI_MAP[comp_pick]} {comp_pick}")

        if user_pick == comp_pick:
            result = f"It's a Tie! {RESULT_TIE}"
        else:
            outcome = RULES.get((user_pick, comp_pick))
            if outcome == 'win':
                result = f"You Win! {RESULT_WIN}"
                self.user_score += 1
            else:
                result = f"Computer Wins! {RESULT_LOSE}"
                self.comp_score += 1
        self.label_result.config(text=result)
        self.label_scores.config(text=self._score_text())
        self.button_play_again.config(state='normal')
        for btn in self.buttons.values():
            btn.config(state='disabled')

    def play_again(self):
        self.round_num += 1
        self.label_round.config(text=f"Round: {self.round_num}")
        self.label_result.config(text="")
        self.label_user_choice.config(text="")
        self.label_comp_choice.config(text="")
        self.button_play_again.config(state='disabled')
        for btn in self.buttons.values():
            btn.config(state='normal')

if __name__ == "__main__":
    root = tk.Tk()

    # --- Optional: Set window icon using a PNG (requires Pillow)
    # try:
    #     from PIL import ImageTk, Image
    #     icon_img = ImageTk.PhotoImage(Image.open("animal_icon.png"))
    #     root.iconphoto(False, icon_img)
    # except Exception:
    #     pass

    game = RPSGame(root)
    root.mainloop()
