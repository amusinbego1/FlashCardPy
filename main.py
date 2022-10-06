from tkinter import *
import messagebox, pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card")
window.configure(background=BACKGROUND_COLOR, padx=50, pady=50)
window.geometry("900x550")
#---------------------------------------------------------------
data = pandas.read_csv("data/italian_words.csv")
def choose_row():
    word = choice(data["Italian"].to_list())
    return ("".join(data[data["Italian"] == word]["Italian"].to_list()[0]), "/".join(data[data["Italian"] == word]["English"].to_list()))
#--------------------------------------------------------
def new_card():
    global t_pair
    change_color(BACKGROUND_COLOR)
    t_pair = choose_row()
    canvas.itemconfig(lan, text="Italian")
    canvas.itemconfig(word, text=t_pair[0])
    canvas.itemconfig(img, image=img_b)
#--------------------------------------------------------
def show_card():
    canvas.itemconfig(lan, text="English")
    canvas.itemconfig(word, text=t_pair[1])
    canvas.itemconfig(img, image=img_f)

#--------------------------------------------------------
def change_color(color):
    window.configure(background=color)
    canvas.configure(bg=color)
    total_text.configure(bg=color)
    guessed_text.configure(bg=color)

#----------------------------------------------------------

def enable_button():
    submit.configure(state=NORMAL)
    window.update()

def check_word():
    global total, guessed
    submit.configure(state=DISABLED)
    window.update()
    total += 1
    english = t_pair[1].lower().split("/")
    if word_entry.get().lower() in english:
        change_color("lightgreen")
        guessed += 1
    else:
        change_color("pink")
    total_text.configure(text=f"/{total}")
    guessed_text.configure(text=f"{guessed}")
    show_card()
    window.after(3000, lambda:[new_card(), enable_button()])
    word_entry.delete(0, END)
    #change_color(BACKGROUND_COLOR)

#-------------------------------------------------------------

total = 0
guessed = 0
total_text = Label(text=f"/{total}", font=("Courier", 30, "bold"), bg=BACKGROUND_COLOR, anchor="w")
total_text.grid(row=0, column=2, sticky="sw")
guessed_text = Label(text=f"{guessed}", font=("Courier", 30,"bold"), bg=BACKGROUND_COLOR, anchor="e")
guessed_text.grid(row=0, column=1, sticky="se")

t_pair = choose_row()

canvas = Canvas(width=600, height=306, bg=BACKGROUND_COLOR, highlightthickness=0)
img_b = PhotoImage(file="images/card_back.png")
img_f = PhotoImage(file="images/card_front.png")
img = canvas.create_image(390, 153, image=img_b)
lan = canvas.create_text(390, 100, text="Italian", font=("Courier", 25, "italic"))
word = canvas.create_text(390, 180, text=t_pair[0], font=("Courier", 30, "bold"))
canvas.grid(row=1, column=1, columnspan=2)

word_entry = Entry(width=15, font=("Courier", 15))
word_entry.grid(row=2, column=1, sticky="e", padx=(120,0))
word_entry.focus()

submit = Button(text="Submit", height=2, width=10, font=("Courier", 12), command=check_word)
submit.grid(row=2, column=2, sticky="w", padx=(50, 0))







window.mainloop()