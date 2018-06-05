import sys

if __name__ == "__main__":
	import os
	import shutil

	os.chdir("C:\\Cleanseed\\Import")

	#Inladen plannen vanuit notepad naar list "plannen"
	from functions import laad_plannen
	dirc_plannen = "C:\\temp\\opkuis xxd\\plannen.txt"
	plannen = laad_plannen(dirc_plannen)
	
	file = "import.txt"

	#delete sourcefile lines
	with open("import.txt", "r") as f:
		lines = f.readlines()

	plan = plannen[0]
	discipline = plan[len(plan)-3:].upper()
	print("Bestandstype: " + discipline)

	#append new sourcefile lines
	with open("import.txt", "w") as f:
		for line in lines:
			if "sourcefile" not in line:
				f.write(line)
		for plan in plannen:
			f.write("sourcefile:C:\Cleanseed\Plannen\\" + discipline + "\\" + plan + "\n")
