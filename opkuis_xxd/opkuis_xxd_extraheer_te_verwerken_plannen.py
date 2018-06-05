import sys

if __name__ == "__main__":
	import os
	import shutil
	from functions import laad_plannen

	os.chdir("W:\\NVLA002\\Geolig\\Datalig")
	
	folder = input("Geef folderpad met te extraheren bestanden: ")
	extract_dirc = os.getcwd() + "\\" + folder	
	
	#Inladen plannen vanuit notepad naar list "plannen"
	from functions import laad_plannen
	dirc_plannen = "C:\\temp\\opkuis xxd\\plannen.txt"
	plannen = laad_plannen(dirc_plannen)

	#Extraheren plannen vanuit W-schijf
	for plan in plannen:
		if plan in os.listdir(extract_dirc):
			shutil.copy(extract_dirc+"\\"+plan, "C:\\temp\\opkuis xxd\\"+plan)
		else: 
			print("Plan " + plan + " bestaat niet in folder!")
	
	print("Bestanden geëxtraheerd")