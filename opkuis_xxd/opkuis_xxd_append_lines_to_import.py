if __name__ == "__main__":
    print("Inlezen plannen vanuit plannen.txt...")
    from functions import laad_plannen
    dirc_plannen = "C:\\temp\\opkuis xxd\\plannen.txt"
    plannen = laad_plannen(dirc_plannen)
    
    file = "C:\\Cleanseed\\Import\\import.txt"
    
    plan = plannen[0]
    discipline = plan[len(plan)-3:].upper()
    print("Bestandstype: " + discipline)
    
    print("Delete current sourcefile lines...")
    with open(file, "r") as f:
        lines = f.readlines()
    
    print("Append new sourcefile lines...")
    with open(file, "w") as f:
        for line in lines:
            if "sourcefile" not in line:
                f.write(line)
        for plan in plannen:
            plannaam = plan[len(plan)-12:]    
            f.write("sourcefile:C:\Cleanseed\Plannen\\" + discipline + "\\" + plannaam + "\n")
            
    programPause = input("Press the <ENTER> key to continue...")