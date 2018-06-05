import sys

if __name__ == "__main__":
	import os
	import shutil

	os.chdir("W:\\NVLA002\\Geolig\\Datalig")
	dirc = os.getcwd() + "\\"
	
	folder = input("Geef folderpad waar verwerkte bestanden moeten worden geplaatst: ")
	
	#Inladen plannen vanuit notepad naar list "plannen"
	from functions import laad_plannen
	dirc_plannen = "C:\\temp\\opkuis xxd\\plannen.txt"
	plannen = laad_plannen(dirc_plannen)
	
	for plan in plannen:
    #hernoemen oud plan naar "old_" op W-schijf
		try:
			plan_old_dirc = dirc + folder + "\\" + plan
			gewijzigd_plan = "old_" + plan
			plan_new_dirc = dirc + folder + "\\" + gewijzigd_plan
			os.rename(plan_old_dirc, plan_new_dirc)
		except Exception as exc:
			print(exc)

		#kopiëren nieuw plan van opkuis-folder naar W-schijf
		copy_dirc = "C:\\temp\\opkuis xxd\\" + plan
		new_dirc = dirc + folder + "\\" + plan
		if os.path.exists(new_dirc):
			print(new_dirc + " already exists!")
		else:
			shutil.copyfile(copy_dirc, new_dirc)
			print("Plan " + plan + " gekopiëerd naar " new_dirc)
			
		"""
		#hernoemen plan naar "_" op opkuis-folder 
		old_dirc = "C:\\temp\\opkuis xxd\\" + plan
		new_dirc = "C:\\temp\\opkuis xxd\\_" + plan
		os.rename(old_dirc, new_dirc)		
		"""
	
	