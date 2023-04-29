#Importy
import tkinter as tk
import tkinter.messagebox
import customtkinter as ctk
import os
import webbrowser
import csv

#Aplikování nastavení

with open("prokaryotaPi_settings.csv", "r") as csv_settings:
	csv_reader = csv.reader(csv_settings)
	
	nastaveni_precteno = []
	
	for line in csv_reader:
		nastaveni_precteno.append(line[1])
		
	print(nastaveni_precteno[1])

#Vzhled
ctk.set_appearance_mode(nastaveni_precteno[0])
ctk.set_default_color_theme(nastaveni_precteno[1])

#Program
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # verze
        Pi_ver = "1.0.0-alpha"
		
        # příkazy
        def start_nastaveni():
        	with open("prokaryotaPi_nastaveni.py") as f:
        		self.destroy()
        		exec(f.read())
        
        def start_calc():
        	with open("prokaryotaPi_calc.py") as f:
        		self.destroy()
        		exec(f.read())
        		
        def start_changelog():
        	with open("prokaryotaPi_changelog.py") as f:
        		self.destroy()
        		exec(f.read())
        
        def start_addons():
        	with open("prokaryotaPi_addons.py") as f:
        		self.destroy()
        		exec(f.read())
        		
        def exit_exit():
        	self.destroy()
		      
        # okno
        self.title("Prokaryota Pi")
        self.geometry(f"{720}x{950}")
        
        # mrizka
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure((0, 1), weight = 1)
        
        # widgety
        nadpis = ctk.CTkLabel(self, text = "Prokaryota Pi", font = ("", 36), anchor = "n")
        nadpis.grid(row = 0, column = 0, columnspan = 2, padx = 20, pady = (20, 0), sticky = "nsew")
        
        exit_button = ctk.CTkButton(self, text = "Odejít", fg_color = "red", hover_color = "crimson", font = ("", 40), corner_radius = 15, command = exit_exit)
        exit_button.grid(row = 0, column = 1, padx = 20, pady = (20, 0), sticky = "ne")
        
        calc_button = ctk.CTkButton(self, text = "Kalkulačka", font = ("", 40), corner_radius = 15, command = start_calc)
        calc_button.grid(row = 1, column = 0, padx = 50, pady = (40, 30), sticky = "nsew")
        
        changelog_button = ctk.CTkButton(self, text = "Seznam změn", font = ("", 40), corner_radius = 15, command = start_changelog)
        changelog_button.grid(row = 1, column = 1, padx = 50, pady = (40, 30), sticky = "nsew")
        
        addons_button = ctk.CTkButton(self, text = "Rozšíření", font = ("", 40), corner_radius = 15, command = start_addons)
        addons_button.grid(row = 2, column = 0, columnspan = 2, padx = 50, pady = (20, 0), sticky = "nsew")
        
        nastaveni_button = ctk.CTkButton(self, text = "Nastavení", font = ("", 40), corner_radius = 15, command = start_nastaveni)
        nastaveni_button.grid(row = 3, column = 0, columnspan = 2, padx = 50, pady = (40, 30), sticky = "nsew")
        
        version_text = ctk.CTkLabel(self, text = Pi_ver, font = ("", 15), anchor = "n")
        version_text.grid(row = 4, column = 1, padx = 10, pady = (10, 0), sticky = "w")
        
if __name__ == "__main__":
    app = App()
    app.mainloop()