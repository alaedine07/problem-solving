def to_rna(dna_strand):
    DNA = ""
    for char in dna_strand:
    	if char == "C":
    		DNA += "G"
    	if char == "G":
    		DNA += "C"	
    	if char == "T":
    		DNA += "A"	
    	if char == "A":
    		DNA += "U"	
    return DNA		