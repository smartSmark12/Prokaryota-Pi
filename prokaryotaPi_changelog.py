#Importy
import tkinter as tk
import tkinter.messagebox
import customtkinter as ctk
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
        def exit_nastaveni():
        	with open("prokaryotaPi_CORE.py") as f:
        		self.destroy()
        		exec(f.read())
        
        # okno
        self.title("Prokaryota Pi")
        self.geometry(f"{720}x{950}")
        
        # mrizka
        self.grid_rowconfigure((0, 1), weight = 1)
        self.grid_columnconfigure((0, 1), weight = 1)
        
        # widgety
        ramecek_clog = ctk.CTkFrame(self)
        ramecek_clog.grid(row = 1, column = 0, columnspan = 2, padx = 20, pady = (20, 0), sticky = "nsew")
        
        #nacteni changelogu
        with open("prokaryotaPi_changelog_data.csv", "r") as f:
        	csv_reader = csv.reader(f)
        	
        	# vytištění changelogu
        	for i in csv_reader:
        		changelog_text = ctk.CTkLabel(ramecek_clog, text = (f"-{i}"), font = ("", 20))
        		changelog_text.pack()
        
        nadpis = ctk.CTkLabel(self, text = "Prokaryota Pi - seznam změn", font = ("", 36), anchor = "n")
        nadpis.grid(row = 0, column = 0, columnspan = 2, padx = 20, pady = (20, 0), sticky = "nsew")
        
        back_button = ctk.CTkButton(self, text = "Zpět", font = ("", 40), corner_radius = 15, command = exit_nastaveni)
        back_button.grid(row = 2, column = 0, columnspan = 2, padx = 50, pady = (20, 30), sticky = "nsew")
        
if __name__ == "__main__":
    app = App()
    app.mainloop()