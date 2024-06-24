from tkinter import *


# def button_clicked():
#     print("I got Clicked")
#     new_text = input.get()
#     my_label.config(text=new_text)
#
#
# window = Tk()
# window.title("My First GUI Project")
# window.minsize(width=500, height=300)
# window.config(padx=20, pady=20)
#
# #label
# my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label["text"] = "New Text"
# my_label.config(text="New Text")
# my_label.grid(column=3, row=5)
# my_label.config(padx=50, pady=50)
#
# #Buttons
#
# button = Button(text="Click me", command=button_clicked)
# button.grid(column=2, row=2)
#
#
# #New_Button
# new_button = Button(text="Baby mapami na")
# new_button.grid(column=3, row=1)
#
#
#
# #Entry
# input = Entry(width=10)
# input.grid(column=4, row=3)
# input.get()
#
#


def button_clicked():
    new_text = int(input_1.get())
    answer = round(new_text * float(1.60934))
    label_4.config(text=answer)


window = Tk()
window.title("Miles to KM Converter")
window.minsize(height=100, width=250)
window.config(padx=20, pady=20)

# IS EQUAL TO
label_1 = Label(text="text_mess", font=("Arial", 12, "bold"))
label_1["text"] = "is equal to"
label_1.grid(column=0, row=2)

# MILES
label_2 = Label(text="Miles", font=("Arial", 12, "bold"))
label_2.grid(column=2, row=1)


# KM
label_3 = Label(text="Km", font=("Arial", 12, "bold"))
label_3.grid(column=2, row=2)


# SOLUTION
label_4 = Label(font=("Arial", 12, "bold"))
label_4.grid(column=1, row=2)


# Entry
input_1 = Entry(width=5, font=("Arial", 12, "bold"))
input_1.grid(column=1, row=1)
input_1.get()


# CALCULATE
calc_button = Button(text="Calculate", command=button_clicked, font=("Arial", 12, "bold"))
calc_button.grid(column=1, row=3)


window.mainloop()
