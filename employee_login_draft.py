import json
import os
from datetime import datetime
user_details_storage_dir = './assets/login_info'
from dependency_scripts.packageloader import LOADER
dependecyload = LOADER(['tk-tools','mysql-connector-python','customtkinter','pycryptodome'])
import tkinter as tk
import customtkinter as ui
from dependency_scripts.passwdencryptionscript import Crypt
encryptioner = Crypt()
testkey = 'threegaymenisten'
#import mysql.connector
class EMPLOYEE_LOGIN():
    def __init__(self) -> None:
        
        self.employee_login_window = ui.CTk()
        self.employee_login_window.title("Employee Login Window")
        self.employee_login_window.geometry("500x350")
        
        ui.set_appearance_mode("dark")
        ui.set_default_color_theme("dark-blue")

        self.frame = ui.CTkFrame(master=self.employee_login_window)
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)

        self.label = ui.CTkLabel(master=self.frame, text="Employee Login", font=("Arial", 24))
        self.label.pack(pady=12, padx=10)
        
        self.employee_id = ui.CTkEntry(master=self.frame, placeholder_text="Employee ID", font=("Arial",12),corner_radius=15)
        self.employee_id.pack(pady=12, padx=10)

        self.employee_passwd = ui.CTkEntry(master=self.frame, placeholder_text="Password", show="●", font=("Arial",12),corner_radius=15)
        self.employee_passwd.pack(pady=12, padx=10)

        self.button = ui.CTkButton(master=self.frame, text="Login", command=self.sign_in,corner_radius=15)
        self.button.pack(pady=12, padx=10)

        self.checkbox = ui.CTkCheckBox(master=self.frame, text="Save to Device")
        self.checkbox.pack(pady=12, padx=10)
        
    def sign_in(self):
        if self.checkbox.get() == 1:
            try:
                os.makedirs(user_details_storage_dir)
                print("[",datetime.now().strftime("%d/%m/%Y | %H:%M:%S"),"]: Folder %s created!" % user_details_storage_dir)
            except FileExistsError:
                pass
            self.local_login_data = {
                "employee_id": encryptioner.encrypt(self.employee_id.get(),testkey),
                "employee_passwd": encryptioner.encrypt(self.employee_passwd.get(),testkey),
            }
            self.json_object = json.dumps(self.local_login_data,indent=2)
            with open("./assets/login_info/local_employee.json", "w+") as outfile:
                outfile.write(self.json_object)
                
        self.employee_id.delete(0, 'end')
        self.employee_passwd.delete(0, 'end')
        self.checkbox.deselect()
        
    def mainlooper(self):
        self.employee_login_window.mainloop()
if __name__ == "__main__":
    empwin=EMPLOYEE_LOGIN()
    empwin.mainlooper()