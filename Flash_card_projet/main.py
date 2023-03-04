from tkinter import *
import pandas
import pandas as pd
import random
import math

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
dict_word = {}
# ---------------------------- Data  ------------------------------- #

try:
    df = pd.read_csv(r"data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv(r"data/french_words.csv")
    dict_word = original_data.to_dict(orient='records')
else:
    dict_word = df.to_dict(orient='records')


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(dict_word)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(background_image, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(background_image, image=card_back)


def is_known():
    if len(current_card) != 0:
        dict_word.remove(current_card)
        data = pd.DataFrame(dict_word)
        data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file=r"images/card_front.png")
card_back = PhotoImage(file=r"images/card_back.png")

background_image = canvas.create_image(400, 263, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

wrong_image = PhotoImage(file=r"images/wrong.png")
right_image = PhotoImage(file=r"images/right.png")

# Button
button_wrong = Button(image=wrong_image, highlightthickness=0, command=next_card)
button_wrong.grid(column=0, row=1)

button_right = Button(image=right_image, highlightthickness=0, command=is_known)
button_right.grid(column=1, row=1)

# text

language_text = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

window.mainloop()
