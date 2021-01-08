# ---------------------------- IMPORTED MODULES ------------------------------- #
import tkinter
from tkinter import messagebox
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password_list = []

for char in range(nr_letters):
    password_list.append(random.choice(letters))

for char in range(nr_symbols):
    password_list += random.choice(symbols)

for char in range(nr_numbers):
    password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char


def password_generator():
    global password
    password_entry.delete(0, tkinter.END)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():

    converted_to_dict = {website_entry.get(): {
        'email': login_entry.get(),
        'password': password_entry.get(),
    }}

    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showinfo(message='Заполните пожалуйста все поля!')
    else:
        messagebox.askokcancel(message=f"Подтвердите данные:\n \n"
                                       f"Вэб-сайт: \n {website_entry.get()} \n \n Логин: \n {login_entry.get()} \n \n"
                                       f"Пароль: \n {password_entry.get()}")
        try:
            with open('passwords_data.json', 'r') as file:
                converted_json_data = json.load(file)
        except FileNotFoundError:
            with open('passwords_data.json', 'w') as file:
                json.dump(converted_to_dict, file, indent=4)
        else:
            converted_json_data.update(converted_to_dict)
            with open('passwords_data.json', 'w') as fl:
                json.dump(converted_json_data,  fl, indent=4)
        finally:

            website_entry.delete(0, tkinter.END)
            password_entry.delete(0, tkinter.END)


# ---------------------------- SEARCH BUTTON  ------------------------------- #
def search_info():
    try:
        with open('passwords_data.json', 'r') as file:
            dict_for_searching = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo('Извините, но в базе еще нет ни одной записи')
    else:
        if website_entry.get() in dict_for_searching:
            messagebox.showinfo(message=f"The Email is:\n \n {dict_for_searching[website_entry.get()]['email']} \n \n"
                                        f"And password is:\n \n {dict_for_searching[website_entry.get()]['password']}")
        else:
            messagebox.showinfo(message="Сорян братан, для такого сайта данных нет")


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title('Менеджер для хранения паролей')
window.config(padx=20, pady=20)

# Image adding
canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
image = tkinter.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

# Website Label
website_label = tkinter.Label()
website_label.config(text='Website: ', font=("Courier", 10, 'bold'))
website_label.grid(row=1, column=0)

# Email/Username Label
login_label = tkinter.Label()
login_label.config(text='Email/Username: ', font=("Courier", 10, 'bold'))
login_label.grid(row=2, column=0)

# Password
password_label = tkinter.Label()
password_label.config(text='Password: ', font=("Courier", 10, 'bold'))
password_label.grid(row=3, column=0)

# Website Entry
website_entry = tkinter.Entry(width=21)
website_entry.grid(row=1, column=1, sticky='w')
website_entry.focus()

# Login Entry
login_entry = tkinter.Entry(width=35)
login_entry.grid(row=2, column=1, columnspan=2)
login_entry.insert(0, 'prince_of_love93@mail.ru')

# Password Entry
password_entry = tkinter.Entry(width=21)
password_entry.grid(row=3, column=1, sticky='w')

# Password Generate Button
password_generate_button = tkinter.Button()
password_generate_button.config(pady=3, text='Generate Password', font=('Courier', 7, 'bold'), highlightthickness=0,
                                command=password_generator)
password_generate_button.grid(row=3, column=1, columnspan=2, sticky='e')

# Add Button
add_button = tkinter.Button(width=43)
add_button.config(pady=2, text='Add', font=('Courier', 7, 'bold'), highlightthickness=0, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)

# SEARCH BUTTON
search_button = add_button = tkinter.Button()
search_button.config(pady=3, text='SEARCH', font=('Courier', 7, 'bold'), highlightthickness=0, command=search_info)
search_button.grid(row=1, column=1, columnspan=2, sticky='e')
window.mainloop()
