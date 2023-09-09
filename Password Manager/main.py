from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for letter in range(randint(8, 10))]
    password_symbols = [choice(symbols) for symbol in range(randint(2, 4))]
    password_numbers = [choice(numbers) for number in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)

    password = "".join(password_list)

    pass_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    web_info = web_entry.get()
    email_info = Email_entry.get()
    password_info = pass_entry.get()
    new_data = {
        web_info: {
            "email": email_info,
            "password": password_info
        }
    }
    if len(web_info) == 0 or len(password_info) == 0:
        messagebox.showinfo(title="Oops", message="You left an Entry empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                # reading the data
                data = json.load(data_file)
        # except json.decoder.JSONDecodeError:
        #     pass
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            # updating the data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)

        finally:
            web_entry.delete(0, END)
            pass_entry.delete(0, END)


def find_password():
    web_info = web_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

            if web_info in data:
                messagebox.showinfo(title="Search Result", message=f"Website: {web_info}\n Password:{data[web_info]['password']}")
            else:
                messagebox.showinfo(title="Error", message="No details for the website exists")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200, highlightthickness=0)
password_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_image)
canvas.grid(column=1, row=0)

# Website label
website = Label(text="Website:")
website.grid(column=0, row=1)

# Website Entry
web_entry = Entry(width=39)
web_entry.grid(column=1, row=1, columnspan=2)
web_entry.focus()

# Email/username
email = Label(text="Email/Username:")
email.grid(column=0, row=2)

# Email Entry
Email_entry = Entry(width=39)
Email_entry.grid(column=1, row=2, columnspan=2)
Email_entry.insert(0, "iamhector576@gmail.com")

# Password
Password = Label(text="Password:")
Password.grid(column=0, row=3)

# Password_entry
pass_entry = Entry(width=35)
pass_entry.grid(column=1, row=3)

# Generate Password
generate_password = Button(text="Generate Password", command=gen_password)
generate_password.grid(column=3, row=3)

# Add
Add = Button(text="Add", width=35, command=save)
Add.grid(column=1, row=4, columnspan=2)

# Search Button
search1 = Button(text="Search", command=find_password)
search1.grid(column=3, row=1)
window.mainloop()
