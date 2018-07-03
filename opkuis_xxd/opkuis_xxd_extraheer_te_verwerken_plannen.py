import sys

if __name__ == "__main__":
    import os
    import shutil
    from functions import laad_plannen

	#os.chdir("W:\\NVLA002\\Geolig\\Datalig")
	
	#folder = input("Geef folderpad met te extraheren bestanden: ")
	#extract_dirc = os.getcwd() + "\\" + folder	
	
    print("Inlezen plannen vanuit plannen.txt...")
    from functions import laad_plannen
    dirc_plannen = "C:\\temp\\opkuis xxd\\plannen.txt"
    plannen = laad_plannen(dirc_plannen)
    
    print("Extraheren plannen vanuit W-schijf...")
    for plan in plannen:
        src = plan
        dst = r"C:\temp\opkuis xxd"
        if os.path.exists(src):
            shutil.copy(src, dst)
        else: 
            print("Plan " + plan + " bestaat niet!")
    
    print("Bestanden geëxtraheerd")
    programPause = input("Press the <ENTER> key to continue...")