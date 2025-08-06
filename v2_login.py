#AUTHOR - KAEA MACDONALD
#DATE - 28/03/25 - 07/08/25
#PURPOSE - THE PURPOSE OF MY PROGRAM IS TO HELP PEOPLE AT ANY AGE WITH LEARNING MATH



import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from customtkinter import *
import tkinter.font as font
import random, string, os, json, re
from PIL import Image, ImageTk
from v11_game_feedback import run_game




user_placeholder = "Username"
pass_placeholder = "Password"

player_accounts = "player_account_details.json"

current_user = None

def create_account():
    player_username = create_account_username_entry.get()
    player_password = create_account_password_entry.get()

    if player_username == "":
        tk.messagebox.showinfo(title="error", message="username can not be blank")
    elif " " in player_username:
        tk.messagebox.showinfo(title="error", message="username can have spaces")
    elif len(player_username) <= 3:
        tk.messagebox.showinfo(title="error", message="username needs more than 3 characters")
    
    elif player_password == "":
        tk.messagebox.showinfo(title="error", message="password can not be blank")
    elif " " in player_password:
        tk.messagebox.showinfo(title="error", message="password can have spaces")
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

        existing_accounts[player_username] = {
            "password": player_password,
            "highscore": 100,
            "current score": 100,
            "current answered correctly": 0,
            "current spins": 0,
            "total answered correctly": 0,
            "total spins": 0,
        }

        with open(player_accounts, "w") as file:
            json.dump(existing_accounts, file, indent=4)

        tk.messagebox.showinfo(title="success", message="account created")
        create_account_username_entry.delete(0, tk.END)
        create_account_password_entry.delete(0, tk.END)
    


def log_in():
    global current_user
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

    if player_username in existing_accounts and existing_accounts[player_username]["password"] == player_password:
        tk.messagebox.showinfo(title="Login", message="Login successful!")
        current_user = player_username
        main_window.destroy()
        run_game(current_user) #runs the main game transfering the users login as current user to save data from the game to there account
    else:
        tk.messagebox.showerror(title="Login Failed", message="Invalid username or password.")


#main window
main_window = tk.Tk()
main_window.title("Main Menu")

window_width = 1000
window_height = 500

screen_width = main_window.winfo_screenwidth()
screen_height = main_window.winfo_screenheight()

win_middle_x = (screen_width // 2) - (window_width // 2) # uses 2 slashes because 1 slash gives a float (decimal point)
win_middle_y = (screen_height // 2) - (window_height // 2)

main_window.geometry(f"{window_width}x{window_height}+{win_middle_x}+{win_middle_y}")

set_appearance_mode("light")

#background imagea



#defining window columns and rows
main_window.columnconfigure((0,1,2,3,4), weight = 1)
main_window.rowconfigure((0,1,2,3,4,5,6,7), weight = 1)

main_window["background"] = "#98C7F6"

title = CTkLabel(main_window, text="Math Add-it", font = ("Terminal", 70,"bold"))
title.grid(column = 2, row = 0, pady = 30)

#Typo Draft Demo.otf

#username_frame = CTkFrame(main_window)
#username_frame.grid(column = 1, row = 1, pady=0)

#password_frame = CTkFrame(main_window)
#password_frame.grid(column = 1, row = 2, pady=0)

create_account_username_label = CTkLabel(main_window, text = "Username", font = ("Terminal", 25))
create_account_username_label.grid(column = 2, row = 1, sticky = SW)

create_account_username_entry = CTkEntry(main_window, font = ("Terminal", 30))
create_account_username_entry.grid(column = 2, row = 2, pady = 10, sticky = NSEW)
create_account_username_entry.focus()

create_account_password_label = CTkLabel(main_window, text = "Password", font = ("Terminal", 25))
create_account_password_label.grid(column = 2, row = 3, sticky = SW)

create_account_password_entry = CTkEntry(main_window, font = ("Terminal", 30))
create_account_password_entry.grid(column = 2, row = 4, pady = 10, sticky = NSEW)


#buttons

create_account_btn =CTkButton(main_window, text="Create account", command=create_account, font = ("Terminal ", 25))
create_account_btn.grid(column = 2, row = 5, pady = 10, sticky = NSEW)

log_in_btn = CTkButton(main_window, text="Log in", command=log_in, font = ("Terminal ", 25))
log_in_btn.grid(column = 2, row = 6, pady = 10, sticky = NSEW)

quit_menu_btn = CTkButton(main_window, text="Quit", command=main_window.destroy, font = ("Terminal ", 25))
quit_menu_btn.grid(column = 2, row = 7, pady = 10, sticky = NSEW)


#main execution
main_window.mainloop()
