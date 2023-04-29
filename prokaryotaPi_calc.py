#Importy
import tkinter as tk
import tkinter.messagebox
import customtkinter as ctk
import math
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
        
        # příkazy
        def exit_calc():
        	with open("prokaryotaPi_CORE.py") as f:
        		self.destroy()
        		exec(f.read())
        		
        # prikazy ramecek
        def calc_fn():
	        vstup = calc_input.get()
	        if vstup == "":
		        print()
	        else:
	        	vysledek = eval(vstup)
		        calc_vysledek.configure(text = vysledek)
		        print("calc_vysledek= " + str(vysledek))
        
        # okno
        self.title("Prokaryota Pi")
        self.geometry(f"{720}x{950}")
        
        # mrizka
        self.grid_rowconfigure((0, 1), weight = 1)
        self.grid_columnconfigure((0, 1), weight = 1)
        
        # widgety
        nadpis = ctk.CTkLabel(self, text = "Prokaryota Pi - kalkulačka", font = ("", 36), anchor = "n")
        nadpis.grid(row = 0, column = 0, columnspan = 2, padx = 20, pady = (20, 0), sticky = "nsew")
        
        ramecek_calc = ctk.CTkFrame(self)
        ramecek_calc.grid(row = 1, column = 0, columnspan = 2, padx = 20, pady = (20, 0), sticky = "new")
        
        back_button = ctk.CTkButton(self, text = "Zpět", font = ("", 40), corner_radius = 15, command = exit_calc)
        back_button.grid(row = 2, column = 0, columnspan = 2, padx = 50, pady = (20, 30), sticky = "nsew")
        
        # mrizka ramecek
        ramecek_calc.grid_rowconfigure(0, weight = 1)
        ramecek_calc.grid_columnconfigure((0, 1), weight = 1)
        
        # widgety ramecek
        calc_input = ctk.CTkEntry(ramecek_calc, height = 40, font = ("", 20), placeholder_text = "Příklad")
        calc_input.grid(row = 0, column = 0, columnspan = 2, padx = 20, pady = (20, 20), sticky = "nsew")
        
        calc_button = ctk.CTkButton(ramecek_calc, text = "Vypočítat", font = ("", 20), command = calc_fn)
        calc_button.grid(row = 0, column = 2, padx = 20, pady = (20, 20), sticky = "nsew")
        
        calc_vysledek = ctk.CTkLabel(ramecek_calc, text = "0", font = ("", 36))
        calc_vysledek.grid(row = 1, column = 0, columnspan = 2, padx = 20, pady = (10, 20), sticky = "w")
        
if __name__ == "__main__":
    app = App()
    app.mainloop()