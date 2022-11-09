#Crea un script en Python que tome como argumento una secuencia proteica e imprima una cadena de 
#ARN codificante. Podés usar de ejemplo el siguiente péptido (cadena corta de aminoácidos):

Sec1 = 'ATVEKGGKHKTGPNEKGKKIFVQKCSQCHTVLHGLFGRKTGQA'

import random

#print(random.randrange(3, 9))

genetic_code = {
    'V': ['GUU', 'GUC', 'GUA', 'GUG'], #Val
    'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'], #Leu
    'T': ['ACU' ,'ACC', 'ACA', 'ACG'], #Thr
    'K': ['AAA', 'AAG'], #Lys
    'W': ['UGG'], #Trp
    'H': ['CAU', 'CAC'], #His
    'F': ['UUU', 'UUC'], #Phe
    'I': ['AUU', 'AUC', 'AUA'], #Ile
    'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'], #Arg
    'M': ['AUG'], #Met
    'A': ['GCU', 'GCC', 'GCA', 'GCG'], #Ala
    'P': ['CCU', 'CCC', 'CCA', 'CCG'], #Pro
    'G': ['GGU', 'GGC', 'GGA', 'GGG'], #Gly
    'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'], #Ser
    'C': ['UGU', 'UGC'], #Cys
    'N': ['AAU', 'AAC'], #Asn
    'Q': ['CAA', 'CAG'], #Gln
    'Y': ['UAU', 'UAC'], #Tyr
    'D': ['GAU', 'GAC'], #Asp
    'E': ['GAA', 'GAG'], #Glu
}

def encode(sequence):
    final_string = ''
    for char in sequence:
        possible_codons = genetic_code[char]
        if(len(possible_codons) > 1):
            final_code_idx = random.randrange(0, len(possible_codons) - 1)
            final_string += possible_codons[final_code_idx]
        else:
            final_string += possible_codons[0]
    return final_string
    
print(encode(Sec1))