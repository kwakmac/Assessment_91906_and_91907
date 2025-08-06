import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from customtkinter import *
import tkinter.font as font
import random, string, os, json, re

user_placeholder = "Username"
pass_placeholder = "Password"

player_accounts = "player_account_details.json"

def show_password():
    if create_account_password_entry.get() != pass_placeholder:
        create_account_password_entry.configure(show='')
        see_pass.configure(command=hide_password, text='i')

def hide_password():
    if create_account_password_entry.get() != pass_placeholder:
        create_account_password_entry.configure(show='*')
        see_pass.configure(command=show_password, text='i')


def game_window():
    game_menu = tk.Toplevel(main_window)
    game_menu.title("Game")
    game_menu.geometry("500x500+400+10")

    CTkButton(game_menu, text="play game", command=game).grid(columnspan=2, pady=0)
    CTkButton(game_menu, text="Quit", command=game_menu.destroy).grid(columnspan=2, pady=0)

def game():
    pass

def create_account():
    player_username = create_account_username_entry.get()
    player_password = create_account_password_entry.get()

    if player_username == "" or player_username == user_placeholder:
        tk.messagebox.showinfo(title="error", message="username can not be blank")
    elif len(player_username) <= 3:
        tk.messagebox.showinfo(title="error", message="username needs more than 3 characters")
    elif player_password == "" or player_password == pass_placeholder:
        tk.messagebox.showinfo(title="error", message="password can not be blank")
    elif len(player_password) <= 5:
        tk.messagebox.showinfo(title="error", message="password needs more than 5 characters")
        create_account_password_entry.delete(0, tk.END)
    else:
        existing_accounts = {}
        if os.path.exists(player_accounts):
            with open(player_accounts, "r") as file:
                try:
                    existing_accounts = json.load(file)
                except json.JSONDecodeError:
                    existing_accounts = {}

        if player_username in existing_accounts:
            tk.messagebox.showinfo(title="error", message="username already exists")
            return

        existing_accounts[player_username] = player_password

        with open(player_accounts, "w") as file:
            json.dump(existing_accounts, file, indent=4)

        tk.messagebox.showinfo(title="success", message="account created")
        create_account_username_entry.delete(0, tk.END)
        create_account_password_entry.delete(0, tk.END)
    



def log_in():
    player_username = create_account_username_entry.get()
    player_password = create_account_password_entry.get()

    if os.path.exists(player_accounts):
        with open(player_accounts, "r") as file:
            try:
                existing_accounts = json.load(file)
            except json.JSONDecodeError:
                existing_accounts = {}
    else:
        existing_accounts = {}

    if player_username in existing_accounts and existing_accounts[player_username] == player_password:
        tk.messagebox.showinfo(title="Login", message="Login successful!")
        game_window()
    else:
        tk.messagebox.showerror(title="Login Failed", message="Invalid username or password.")


    

#-------------------------------------------   entry focuses -----------------------------------

def user_on_focus_in(event):
    global create_account_username_entry
    if create_account_username_entry.get() == user_placeholder:
         create_account_username_entry.delete(0, tk.END)
         create_account_username_entry.configure()
         

def user_on_focus_out(event):
    global create_account_username_entry
    if create_account_username_entry.get() == "":
         create_account_username_entry.insert(0, user_placeholder)
         create_account_username_entry.configure()


def pass_on_focus_in(event):
    global create_account_password_entry
    if create_account_password_entry.get() == pass_placeholder:
         create_account_password_entry.delete(0, tk.END)
         create_account_password_entry.configure(show='*')
         

def pass_on_focus_out(event):
    global create_account_password_entry
    if create_account_password_entry.get() == "":
         create_account_password_entry.insert(0, pass_placeholder)
         create_account_password_entry.configure()
#-------------------------------------------------------------------------------------------

main_window = tk.Tk()
main_window.title("Main Menu")
main_window.geometry("320x320+10+10")

set_appearance_mode("light")


with open("equations.txt", "w") as file:
        file.write("")

CTkLabel(main_window, text="game",). grid(column = 0, row = 0, pady=30)

create_account_username_entry = CTkEntry(main_window)
create_account_username_entry.grid(column = 0, row = 1, pady=0)

create_account_password_entry = CTkEntry(main_window, show = "")
create_account_password_entry.grid(column=0, row = 2, pady=0)

create_account_username_entry.insert(0, user_placeholder)
create_account_password_entry.insert(0, pass_placeholder)

create_account_username_entry.bind("<FocusIn>", user_on_focus_in)
create_account_username_entry.bind("<FocusOut>", user_on_focus_out)

create_account_password_entry.bind("<FocusIn>", pass_on_focus_in)
create_account_password_entry.bind("<FocusOut>", pass_on_focus_out)

#buttons
see_pass = CTkButton(main_window, text="i ", command=show_password, width = 3)
see_pass.grid(column = 2, row = 2, pady=3)

CTkButton(main_window, text="Create account", command=create_account).grid(column = 0, row = 3, pady=3)
CTkButton(main_window, text="Log in", command=log_in).grid(column = 0, row = 4, pady=3)
CTkButton(main_window, text="Quit", command=main_window.destroy).grid(column = 0, row = 5, pady=3)



#main execution
main_window.mainloop()
