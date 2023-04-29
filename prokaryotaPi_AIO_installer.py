#Importy
import os
import requests
import importlib.util
import sys

#Kontrola importů
pozadovane = ["customtkinter", "requests"]

print("kontrola požadavků...")
print("")

for i in range(len(pozadovane)):
	if (spec := importlib.util.find_spec(pozadovane[i])) is not None:
		
		print(f"{pozadovane[i]!r} je v souborech...")
		
		module = importlib.util.module_from_spec(spec)
		sys.modules[pozadovane[i]] = module
		spec.loader.exec_module(module)
		
		print(f"{pozadovane[i]!r} byl importován...")
		
	else:
		print(f"{pozadovane[i]!r} nebyl nalezen! (instalace: menu>pip>install>'{pozadovane[i]}'>install")
	print("")

#Program
slozka_programu = "./Prokaryota"

aktualni_slozka = os.getcwd()

if aktualni_slozka == "/storage/emulated/0/Documents":
	print("Instalační soubor je ve správné složce")
	print("")
else:
	print("Přemístěte prosím instalační soubor do složky 'Documents' a spusˇtte instalaci znovu")
	exit()

stahnuti_potvrzeni = input("Potrvˇdte stažení programu Prokaryota Pi [a/n]: " )

if aktualni_slozka == "/storage/emulated/0/Documents" and stahnuti_potvrzeni == "a":
	
	if os.path.exists(slozka_programu):
		
		stahovani_CORE = requests.get("https://raw.githubusercontent.com/smartSmark12/Prokaryota-Pi/main/prokaryotaPi_CORE.py")
		open(f"{slozka_programu}/prokaryotaPi_CORE.py", "wb").write(stahovani_CORE.content)
		
		stahovani_nastaveni = requests.get("https://raw.githubusercontent.com/smartSmark12/Prokaryota-Pi/main/prokaryotaPi_nastaveni.py")
		open(f"{slozka_programu}/prokaryotaPi_nastaveni.py", "wb").write(stahovani_nastaveni.content)
		
		stahovani_addons = requests.get("https://raw.githubusercontent.com/smartSmark12/Prokaryota-Pi/main/prokaryotaPi_addons.py")
		open(f"{slozka_programu}/prokaryotaPi_addons.py", "wb").write(stahovani_addons.content)
		
		stahovani_changelog = requests.get("https://raw.githubusercontent.com/smartSmark12/Prokaryota-Pi/main/prokaryotaPi_changelog.py")
		open(f"{slozka_programu}/prokaryotaPi_changelog.py", "wb").write(stahovani_changelog.content)
		
		stahovani_calc = requests.get("https://raw.githubusercontent.com/smartSmark12/Prokaryota-Pi/main/prokaryotaPi_calc.py")
		open(f"{slozka_programu}/prokaryotaPi_calc.py", "wb").write(stahovani_calc.content)
		
		stahovani_changelog_data = requests.get("https://raw.githubusercontent.com/smartSmark12/Prokaryota-Pi/main/prokaryotaPi_changelog_data.csv")
		open(f"{slozka_programu}/prokaryotaPi_changelog_data.csv", "wb").write(stahovani_changelog_data.content)
		
		stahovani_settings = requests.get("https://raw.githubusercontent.com/smartSmark12/Prokaryota-Pi/main/prokaryotaPi_settings.csv")
		open(f"{slozka_programu}/prokaryotaPi_settings.csv", "wb").write(stahovani_settings.content)
	
	else:
		os.mkdir(slozka_programu)
		print("slozka vytvořena, spusˇtte prosím instalaci znovu")
else:
	print("Program nebyl stažen")