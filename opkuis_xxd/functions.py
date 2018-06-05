def laad_plannen(dirc):
	with open(dirc, "r") as f:
		lines = f.readlines()
		split_lines = [line.split("\n") for line in lines]
		plannen = [line[0] for line in split_lines]
	return plannen
	
