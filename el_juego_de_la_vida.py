#Crea un script en Python que tome como argumento una secuencia proteica e imprima una cadena de 
#ARN codificante. Podés usar de ejemplo el siguiente péptido (cadena corta de aminoácidos):

#Sec1: 'ATVEKGGKHKTGPNEKGKKIFVQKCSQCHTVLHGLFGRKTGQA'

genetic_code = {
    'UUU': 'Phe',
    'UUC': 'Phe',
    'UUA': 'Leu',
    'UUG': 'Leu',
    'CUU': 'Leu',
    'CUC': 'Leu',
    'CUA': 'Leu',
    'CUG': 'Leu',
    'AUU': 'Iso',
    'AUC': 'Iso',
    'AUA': 'Iso',
    'AUG': 'Met',
    'GUU': 'Val',
    'GUC': 'Val',
    'GUA': 'Val',
    'GUG': 'Val',
    'UCU': 'Ser',
    'UCC': 'Ser',
    'UCA': 'Ser',
    'UCG': 'Ser',
    'CCU': 'Pro',
    'CCC': 'Pro',
    'CCA': 'Pro',
    'CCG': 'Pro',
    'ACU': 'Thr',
    'ACC': 'Thr',
    'ACA': 'Thr',
    'ACG': 'Thr',
    'GCU': 'Ala',
    'GCC': 'Ala',
    'GCA': 'Ala',
    'GCG': 'Ala',
    'UAU': 'Tyr',
    'UAC': 'Tyr',
    'UAA': 'STOP',
    'UAG': 'STOP',
    'CAU': 'His',
    'CAC': 'His',
    'CAU': 'His',
    'CAA': 'Gln',
    'CAG': 'Gln',
    'AAU': 'Asn',
    'AAC': 'Asn',
    'AAA': 'Lys',
    'AAG': 'Lys',
    'GAU': 'Asp',
    'GAC': 'Asp',
    'GAA': 'Glu',
    'GAG': 'Glu',
    'UGU': 'Cys',
    'UGC': 'Cys',
    'UGA': 'STOP',
    'UGG': 'Tyr',
    'UGG': 'Tyr',
    'CGU': 'Arg',
    'CGC': 'Arg',
    'CGA': 'Arg',
    'CGG': 'Arg',
    'AGU': 'Ser',
    'AGC': 'Ser',
    'AGA': 'Arg',
    'AGG': 'Arg',
    'GGU': 'Gly',
    'GGC': 'Gly',
    'GGA': 'Gly',
    'GGG': 'Gly',
}

def encode(sequence):
    index_start = 0
    index_end = index_start + 2
    while index_end < len(sequence):
        sequence[index_start, index_end]