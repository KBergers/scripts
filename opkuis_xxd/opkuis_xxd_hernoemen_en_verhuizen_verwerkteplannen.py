import sys

if __name__ == "__main__":
    import os
    import shutil
    
    print("Inlezen plannen vanuit plannen.txt...")
    from functions import laad_plannen
    dirc_plannen = "C:\\temp\\opkuis xxd\\plannen.txt"
    plannen = laad_plannen(dirc_plannen)
    
    print("Hernoemen voormalige plannen naar 'old_xxx' en kopiëren nieuwe plannen naar W-schijf...")
    for plan in plannen:
        folder = plan[:len(plan)-12]
        plannaam = plan[len(plan)-12:]    
    
        #hernoemen voormalig plan naar "old_" op W-schijf    
        try:    
            oud_plan = folder + "old_" + plannaam
            os.rename(plan, oud_plan)
        except Exception as exc:
            print(exc)
            
        #kopiëren nieuw plan van opkuis-folder naar W-schijf
        copy_dirc = "C:\\temp\\opkuis xxd\\" + plannaam
        new_dirc = plan
        if os.path.exists(new_dirc):
            print(new_dirc + " bestaat al!")
        else:
            shutil.copyfile(copy_dirc, new_dirc)
            print("-----")
            print("Plan " + plannaam + " gekopiëerd naar " + new_dirc)
            
    programPause = input("Press the <ENTER> key to continue...")
			
