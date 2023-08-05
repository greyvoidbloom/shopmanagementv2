import sys
from settings import LOADER
dependecyload = LOADER(['tk-tools','mysql-connector-python','customtkinter'])
import tkinter as tk
import customtkinter as ui
import mysql.connector
# === manually add your password untill we write the sql user login window lol ===
mydb=mysql.connector.connect(host="localhost",user="root",passwd="user_password",auth_plugin='mysql_native_password')
if (mydb):
    print("\n\nconnection successful")
else:
    print("connection unsuccessful")

ui.set_appearance_mode("dark")
ui.set_default_color_theme("dark-blue")

employee_login_window = ui.CTk()
employee_login_window.title("Employee Login Window")
employee_login_window.geometry("500x350")

frame = ui.CTkFrame(master=employee_login_window)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = ui.CTkLabel(master=frame, text="Employee Login", font=("Hack Nerd Font", 24))
label.pack(pady=12, padx=10)


employee_id = ui.CTkEntry(master=frame, placeholder_text="Employee ID", font=("Hack Nerd Font",12),corner_radius=15)
employee_id.pack(pady=12, padx=10)

employee_passwd = ui.CTkEntry(master=frame, placeholder_text="Password", show="●", font=("Arial",12),corner_radius=15)
employee_passwd.pack(pady=12, padx=10)

def sign_in():
    print(employee_id.get())
    print(employee_passwd.get())
    employee_id.delete(0, 'end')
    employee_passwd.delete(0, 'end')

button = ui.CTkButton(master=frame, text="Login", command=sign_in,corner_radius=15)
button.pack(pady=12, padx=10)

checkbox = ui.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=12, padx=10)

employee_login_window.mainloop()