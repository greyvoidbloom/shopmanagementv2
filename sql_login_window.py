import json
import os
sql_details_storage_dir = './assets/login_info'
from assets.dependency_scripts.settings import LOADER
dependecyload = LOADER(['tk-tools','mysql-connector-python','customtkinter','datetime'])
from datetime import datetime
import tkinter as tk
import customtkinter as ui
import mysql.connector
class SQL_USER_LOGIN():
    def __init__(self) -> None:
        
        self.sql_user_window = ui.CTk()
        self.sql_user_window.title("SQL User Login")
        self.sql_user_window.geometry("500x350")
        
        ui.set_appearance_mode("dark")

        self.frame = ui.CTkFrame(master=self.sql_user_window)
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)

        self.sql_heading = ui.CTkLabel(master=self.frame, text="SQL Connection", font=("Arial", 24))
        self.sql_heading.pack(pady=12, padx=10)
        
        self.sql_user_id = ui.CTkEntry(master=self.frame, placeholder_text="SQL User", font=("Arial",12),corner_radius=15)
        self.sql_user_id.pack(pady=12, padx=10)

        self.sql_passwd = ui.CTkEntry(master=self.frame, placeholder_text="SQL Password", show="●", font=("Arial",12),corner_radius=15)
        self.sql_passwd.pack(pady=12, padx=10)

        self.button = ui.CTkButton(master=self.frame, text="Login", command=self.sign_in,corner_radius=15)
        self.button.pack(pady=12, padx=10)
        
        self.themeswitch = ui.CTkSwitch(master=self.frame,text="Light theme",command=self.themeswitcher)
        self.themeswitch.pack(pady=12, padx=10)
        
    def themeswitcher(self):
        if self.themeswitch.get() == 1:
            ui.AppearanceModeTracker.set_appearance_mode("Light")
        else:
            ui.AppearanceModeTracker.set_appearance_mode("Dark")
    def sign_in(self):
        try :
            self.mydb=mysql.connector.connect(host="localhost",user=self.sql_user_id.get(),passwd=self.sql_passwd.get(),auth_plugin='mysql_native_password')
            if self.mydb.is_connected():
                try:
                    os.makedirs(sql_details_storage_dir)
                    print("[",datetime.now().strftime("%d/%m/%Y | %H:%M:%S"),"]: Folder %s created!" % sql_details_storage_dir)
                except FileExistsError:
                    pass
                self.local_login_data = {
                "user id": self.sql_user_id.get(),
                "passwd": self.sql_passwd.get()
                }
                self.json_object = json.dumps(self.local_login_data,indent=2)
                with open("./assets/login_info/sql_user_data.json", "w+") as outfile:
                    outfile.write(self.json_object)
                print("\n[",datetime.now().strftime("%d/%m/%Y | %H:%M:%S"),"]: connection successful")
                self.sql_user_id.delete(0, 'end')
                self.sql_passwd.delete(0, 'end')
                
        except mysql.connector.Error:
            print("\n[",datetime.now().strftime("%d/%m/%Y | %H:%M:%S"),"]: connection failed")

        
    def mainlooper(self):
        self.sql_user_window.mainloop()
if __name__ == "__main__":
    empwin=SQL_USER_LOGIN()
    empwin.mainlooper()