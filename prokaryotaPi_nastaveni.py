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
		
	print(nastaveni_precteno[0])
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
        		
        # vyber barvy systému nastaveni
        def vyber_appearance_callback(vyber):
        	print("vybráno: ", vyber)
        	
        	with open("prokaryotaPi_settings.csv", "r") as f:
        		csv_reader = csv.reader(f)
        		nastaveni_precteno = []
        		for i in csv_reader:
        			nastaveni_precteno.append(i[1])
        	
        	if vyber == "Systém":
        		vyber = "System"
        	elif vyber == "Světlý":
        		vyber = "Light"
        	else:
        		vyber = "Dark"
        	
        	with open("prokaryotaPi_settings.csv", "w", newline = "") as settings_write:
        		csv_writer = csv.writer(settings_write)
        		
        		csv_writer.writerow(["appearance_mode", vyber])
        		csv_writer.writerow(["default_color_theme", nastaveni_precteno[1]])
        		ctk.set_appearance_mode(vyber)
        		
        # vyber barvy tlačítek nastaveni
        def vyber_button_callback(vyber_tlacitka):
        	print("vybráno: ", vyber_tlacitka)
        	
        	with open("prokaryotaPi_settings.csv", "r") as f:
        		csv_reader = csv.reader(f)
        		nastaveni_precteno = []
        		for i in csv_reader:
        			nastaveni_precteno.append(i[1])
        	
        	if vyber_tlacitka == "Modrá":
        		vyber_tlacitka = "blue"
        	else:
        		vyber_tlacitka = "green"
        	
        	with open("prokaryotaPi_settings.csv", "w", newline = "") as settings_write:
        		csv_writer = csv.writer(settings_write)
        		
        		csv_writer.writerow(["appearance_mode", nastaveni_precteno[0]])
        		csv_writer.writerow(["default_color_theme", vyber_tlacitka])
        		ctk.set_default_color_theme(vyber_tlacitka)
        # okno
        self.title("Prokaryota Pi")
        self.geometry(f"{720}x{950}")
        
        # mrizka
        self.grid_rowconfigure((0, 1), weight = 1)
        self.grid_columnconfigure((0, 1), weight = 1)
        
        # widgety
        nadpis = ctk.CTkLabel(self, text = "Prokaryota Pi - nastavení", font = ("", 36), anchor = "n")
        nadpis.grid(row = 0, column = 0, columnspan = 2, padx = 20, pady = (20, 0), sticky = "nsew")
        
        ramecek_main = ctk.CTkFrame(self)
        ramecek_main.grid(row = 1, column = 0, columnspan = 2, padx = 20, pady = (20, 20), sticky = "nsew")
        
        # vyber vzhledu: systém
        vyber_appearance_text = ctk.CTkLabel(ramecek_main, text = "Vzhled systému:", font = ("", 20), anchor = "e")
        vyber_appearance_text.grid(row = 0, column = 0, padx = 0, pady = (20, 0), sticky = "n")
        
        vyber_appearance_var = ctk.StringVar(value = "temp")
        vyber_appearance = ctk.CTkComboBox(ramecek_main, values = ["Systém", "Tmavý", "Světlý"], font = ("", 20), height = 40, width = 200, corner_radius = 12, dropdown_font = ("", 20), command = vyber_appearance_callback, variable = vyber_appearance_var)
        vyber_appearance.grid(row = 1, column = 0, columnspan = 2, padx = 35, pady = (0, 20), sticky = "n")
        vyber_appearance_var.set(nastaveni_precteno[0])
        
        # vyber zakladniho nazvu barva
        if nastaveni_precteno[0] == "Dark":
        	vyber_appearance_var.set("Tmavý")
        elif nastaveni_precteno[0] == "Light":
        	vyber_appearance_var.set("Světlý")
        else:
        	vyber_appearance_var.set("Systém")
        
        # vyber vzhledu: tlačítka
        vyber_button_text = ctk.CTkLabel(ramecek_main, text = "Vzhled tlačítek:", font = ("", 20), anchor = "e")
        vyber_button_text.grid(row = 2, column = 0, padx = 0, pady = (20, 0), sticky = "n")
        
        vyber_button_var = ctk.StringVar(value = "temp2")
        vyber_button = ctk.CTkComboBox(ramecek_main, values = ["Modrá", "Zelená"], font = ("", 20), height = 40, width = 200, corner_radius = 12, dropdown_font = ("", 20), command = vyber_button_callback, variable = vyber_button_var)
        vyber_button.grid(row = 3, column = 0, columnspan = 2, padx = 35, pady = (0, 20), sticky = "n")
        vyber_button_var.set(nastaveni_precteno[1])
        
        # vyber zakladniho nazvu barva
        if nastaveni_precteno[1] == "blue":
        	vyber_button_var.set("Modrá")
        else:
        	vyber_button_var.set("Zelená")
        
        # tlačítko zpět
        back_button = ctk.CTkButton(self, text = "Zpět", font = ("", 40), corner_radius = 15, command = exit_nastaveni)
        back_button.grid(row = 2, column = 0, columnspan = 2, padx = 50, pady = (20, 30), sticky = "nsew")
        
if __name__ == "__main__":
    app = App()
    app.mainloop()