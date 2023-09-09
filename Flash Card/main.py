from tkinter import *
import random
import pandas


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
my_list = {}


try:
    DataFrame = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/german_word.csv")
    my_list = original_data.to_dict(orient="records")
else:
    my_list = DataFrame.to_dict(orient="records")




def change():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(my_list)
    word = current_card["GERMAN"]
    canvas.itemconfig(header_text, text="German", fill="black")
    canvas.itemconfig(WORD_text, text=word, fill="black")
    canvas.itemconfig(canvas_image, image=old_image)
    flip_timer = window.after(3000, flip)

def flip():
    canvas.itemconfig(canvas_image, image=new_image)
    canvas.itemconfig(header_text, text="English", fill="white")
    canvas.itemconfig(WORD_text, text=current_card["ENGLISH"], fill="white")

def is_known():
    my_list.remove(current_card)
    data = pandas.DataFrame(my_list)
    data.to_csv("data/words_to_learn.csv", index=False)

    change()


window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip)
# window.after_cancel()
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
new_image = PhotoImage(file="images/card_back.png")
old_image = PhotoImage(file="C:/Users/user/Desktop/Flash Card/images/card_front.png")
canvas_image = canvas.create_image(400, 265, image=old_image)
header_text = canvas.create_text(400, 150, text='Title', font=("Ariel", 40, "italic"))
WORD_text = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(column=1, row=1, columnspan=2)

#Cancel Button
my_image = PhotoImage(file="C:/Users/user/Desktop/Flash Card/images/wrong.png")
x_button = Button(image=my_image,  bg=BACKGROUND_COLOR, highlightthickness=0, command=change)
x_button.grid(column=1, row=2)

# Right Button
image_2 = PhotoImage(file="C:/Users/user/Desktop/Flash Card/images/right.png")
right_button = Button(image=image_2, bg=BACKGROUND_COLOR, highlightthickness=0, command=is_known)
right_button.grid(column=2, row=2)


change()

window.mainloop()
