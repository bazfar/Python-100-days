from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project

def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'
        , 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E'
        , 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U'
        , 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list1 = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_list2 = [random.choice(symbols) for char in range(random.randint(2, 4))]
    password_list3 = [random.choice(numbers) for char in range(random.randint(2, 4))]

    password_list = password_list1 + password_list2 + password_list3
    random.shuffle(password_list)
    password = ""
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please fill all the fields and save")
    else:
        # is_ok = messagebox.askokcancel(title=website, message=f"Are you sure about this information?\nEmail: "
        #                                                       f"{email}\nPassword: {password}\n Would you like to save?")
        # if is_ok:
        try:
            with open("data.json", "r") as file:
                # json.dump(new_data, file, indent=4)
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
                # file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
        finally:
            clear()


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    try:
        with open("data.json", "r") as file:
            # json.dump(new_data, file, indent=4)
            data = json.load(file)
    except json.decoder.JSONDecodeError:
        messagebox.showinfo(title="Oops", message="No password saved please add new ones")
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No password saved")
        save()
    else:
        website = website_entry.get()
        if len(website) == 0:
            messagebox.showinfo(title="Oops", message="Please fill the Website name")
            clear()
        elif website not in data:
            messagebox.showinfo(title="Oops", message="No website with this name saved")
            clear()
        else:
            password_entry.insert(0, data[website]["password"])


def clear():
    website_entry.delete(0, END)
    password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
window.grid()

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
logo_image = canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Texts
site_text = Label(text="Website: ")
site_text.grid(column=0, row=1)

email_text = Label(text="Email/Username: ")
email_text.grid(column=0, row=2)

password_text = Label(text="Password:")
password_text.grid(column=0, row=3)

# Entries
website_entry = Entry(width=24, highlightthickness=0)
website_entry.grid(column=1, row=1, columnspan=1)

email_entry = Entry(width=42, highlightthickness=0)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "araara@gmail.com")

password_entry = Entry(width=24, highlightthickness=0)
password_entry.grid(column=1, row=3)

# Buttons
add_button = Button(width=36, text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2)

generate_button = Button(text="Generate Password", command=password_generator, highlightthickness=0)
generate_button.grid(column=2, row=3)

search_button = Button(width=15, text="Search", command=find_password, highlightthickness=0)
search_button.grid(column=2, row=1)

window.mainloop()
