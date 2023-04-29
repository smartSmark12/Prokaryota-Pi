#Importy
import tkinter as tk
import tkinter.messagebox
import customtkinter as ctk
import csv
import sys

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
        
        # kontrola adresáře a vytvoření složky 'Addons'
        if os.path.exists("./Addons"):
        	print("slozka addons existuje")
        else:
        	print("slozka addons neni")
        	os.mkdir("./Addons")
        
        # příkazy
        def exit_nastaveni():
        	with open("prokaryotaPi_CORE.py") as f:
        		self.destroy()
        		exec(f.read())
        
        #callback pro otevření souboru z comboboxu		
        def addons_vyber_callback(vyber):
        	with open(loaded_addons[vyber]) as f:
        		exec(f.read())
        
        # okno
        self.title("Prokaryota Pi")
        self.geometry(f"{720}x{950}")
        
        # mrizka
        self.grid_rowconfigure((0, 1), weight = 1)
        self.grid_columnconfigure((0, 1), weight = 1)
        
        # widgety
        nadpis = ctk.CTkLabel(self, text = "Prokaryota Pi - rozšíření", font = ("", 36), anchor = "n")
        nadpis.grid(row = 0, column = 0, columnspan = 2, padx = 20, pady = (20, 0), sticky = "nsew")
        
        # ramecek pro addony
        addon_frame = ctk.CTkFrame(self)
        addon_frame.grid(row = 1, column = 0, columnspan = 2, padx = 20, pady = (20, 20), sticky = "nsew")
        
        # addon_frame mřížka
        addon_frame.grid_rowconfigure((0, 1), weight = 1)
        addon_frame.grid_columnconfigure((0,1), weight = 1)
        
        # vytvoření seznamu addonů
        seznam_addons = os.listdir("./Addons")
        print(seznam_addons)
        
        # vytvoření seznamu zapsaných podsložek
        loaded_addons = {}
        loaded_addons_list = []
        
        for file in seznam_addons:
        	je_slozka = os.path.isdir(f"./Addons/{file}")
        	if je_slozka:
        		toto = sys.path.insert(0, f"./Addons/{file}")
        		print(toto)
        		
        		from prokaryotaPi_addonLaunchCfg import _prokaryotaPi_addon_name, _prokaryotaPi_launch_file
        		
        		loaded_addons[f"{_prokaryotaPi_addon_name}"] = f"./Addons/{file}/{_prokaryotaPi_launch_file}"
        		loaded_addons_list.append(_prokaryotaPi_addon_name)
        		
        		del sys.modules["prokaryotaPi_addonLaunchCfg"]
        		
        		print(f"addony: {loaded_addons}")
        		print(len(loaded_addons))
        		print(f"addony_list: {loaded_addons_list}")
        		
        # vykreslení seznamu addonů v comboboxu
        addons_vyber_var = ctk.StringVar(value = "Vyber rozšíření")
        
        addons_vyber = ctk.CTkComboBox(addon_frame, values = loaded_addons_list, font = ("", 20), height = 50, corner_radius = 15, dropdown_font = ("", 20), command = addons_vyber_callback, variable = addons_vyber_var)
        addons_vyber.grid(row = 0, column = 0, columnspan = 2, padx = 50, pady = (20, 20), sticky = "new")
        
        # tlačítko zpět
        back_button = ctk.CTkButton(self, text = "Zpět", font = ("", 40), corner_radius = 15, command = exit_nastaveni)
        back_button.grid(row = 2, column = 0, columnspan = 2, padx = 50, pady = (20, 30), sticky = "nsew")
        
if __name__ == "__main__":
    app = App()
    app.mainloop()