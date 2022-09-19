# RETO I
# ¿Podés descubrir y anotar el orden en que se ha ejecutado cada operación?
#((4+5)*2)/5

# 1) 4 + 5
# 2) * 2
# 3) / 5

#RETO II

#RETO II: Creá una variable llamada doble, que sea el doble de la suma entre a y b.
a = 10
b = 10
doble = (a + b) * 2

#RETO III

values = {
    'Met': 'AUG',
    'Lis': 'AAA',
    'Leu': 'CUA'
}

peptido = 'Met-Lis-Lis-Lis-Leu-Leu-Met'
resultado = ''
idx = 0

while idx + 3 < len(peptido):
    amin = peptido[idx: idx + 3]
    resultado = resultado + values[amin]
    idx += 4
#print("resultado " + resultado)

#RETO IV

ADN = 'TGATAAGAGTACCCAGAATAAAATGAATAACTTTTTAAAGACAAAATCCTCTGTTATAATATTGCTAAAATTATTCAGAGTAATATTGTGGATTAAAGCCACAATAAGATTTATAATCTTAAATGATGGGACTACCATCCTTACTCTCTCCATTTCAAGGCTGACGATAAGGAGACCTGCTTTGCCGAGGAGGTACTACAGTTCTCTTCACAAACAATTGTCTTACAAAATGAATAAAACAGCACTTTGTTTTTATCTCCTGCTTTTAATATGTCCAGTATTCATTTTTGCATGTTTGGTTAGGCTAGGGCTTAGGGATTTATATATCAAAGGAGGCTTTGTACATGTGGGACAGGGATCTTATTTTAGATTTATATATCAAAGGAGGCTTTGTACATGTGGGACAGGGATCTTATTTTACAAACAATTGTCTTACAAAATGAATAAAACAGCACTTTGTTTTTATCTCCTGCTCTATTGTGCCATACTGTTGAATGTTTATAATGCATGTTCTGTTTCCAAATTTCATGAAATCAAAACATTAATTTATTTAAACATTTACTTGAAATGTTCACAAACAATTGTCTTACAAAATGAATAAAACAGCACTTTGTTTTTATCTCCTGCTTTTAATATGTCCAGTATTCATTTTTGCATGTTTGGTTAGGCTAGGGCTTAGGGATTTATATATCAAAGGAGGCTTTGTACATGTGGGACAGGGATCTTATTTTAGATTTATATATCAAAGGAGGCTTTGTACATGTGGGACAGGGATCTTATTTTACAAACAATTGTCTTACAAAATGAATAAAACAGCACTTTGTTTTTATCTCCTGCTCTATTGTGCCATACTGTTGAATGTTTATAATGCATGTTCTGTTTCCAAATTTCATGAAATCAAAACATTAATTTATTTAAACATTTACTTGAAATGTGGTGGTTTGTGATTTAGTTGATTTTATAGGCTAGTGGGAGAATTTACATTCAAATGTCTAAATCACTTAAAATTTCCCTTTATGGCCTGACAGTAACTTTTTTTTATTCATTTGGGGACAACTATGTCCGTGAGCTTCCATCCAGAGATTATAGTAGTAAATTGTAATTAAAGGATATGATGCACGTGAAATCACTTTGCAATCAT'

count = ADN.count('CG')
porcentaje = str((count * 100) / len(ADN))

#print("count: " + str(count))
#print("len ADN: " + str(len(ADN)))
#print("%: " + porcentaje)

#RETO V

GEN = 'ATGGAACTTGCAATCGAAGTTGGC'
GEN_MUTADO_AM = 'GTTTGTGGTTG'

NEW_GEN = GEN
CANTIDAD = 0

REEMPLAZOS = {
    1: ["C", "T"]
    ,
    2: ["A", "G"]
    ,
    3: ["C", "A"]
}
for idx in range(1,4):
    reemplazo_actual = REEMPLAZOS[idx]
    NEW_GEN = NEW_GEN.replace(reemplazo_actual[0], reemplazo_actual[1])
    if(GEN_MUTADO_AM not in NEW_GEN):
        CANTIDAD = idx + 1
    else:
        break

print("NEW_GEN: " + NEW_GEN)
print("CANTIDAD: " + str(CANTIDAD))

#RETO VI: ¿Se te ocurre qué operadores podrías usar para las listas?

#RETO VII: 
# Ya que encontramos el espécimen de rana con pelo en marte, nos gustaría contrastar sus características con las ranas terrestres. Sabiendo que el gen de la proteína diminuta es ‘ATGGAAGTTGGAATCCAAGTTGGA’ y el gen de una proteína similar de rana terrestre es ‘ATGGAAGTTAATGGAAGTTGGAGGAGA’ ¿podés crear un programa que compare la longitud de ambos genes y según cuál sea más grande nos imprima un mensaje informándonos el resultado?

gen_rana_diminuta = 'ATGGAAGTTGGAATCCAAGTTGGA'
gen_rana_terrestre = 'ATGGAAGTTAATGGAAGTTGGAGGAGA'

if(len(gen_rana_terrestre) > len(gen_rana_diminuta)):
    print('GEN de la RANA TERRESTRE es MAYOR')
else:
    print('GEN de la RANA TERRESTRE es MAYOR')
    
#RETO VIII: Si nos ponemos un poco más estrictos, y siguiendo con el tema de los clones de bacterias,
#el programa que creamos antes tiene algunas fallas ‘numéricas’: en cada vuelta de división
#celular binaria se generarán dos clones, no uno. 
#¿Podrías escribir un programa que imprima ‘¡Somos 2 clones nuevos!’ en cada una de 20 vueltas?

#for i in range(0,20):
	#print('¡Somos 2 clones nuevos!')
    
#RETO IX: Si ahora queremos hacer nuestro programa un poco más estricto, por cada vuelta 
#deberíamos sumar el total de células que tenemos e imprimir ese número en el mensaje.
#Entonces, por ejemplo, como en la primer vuelta tenemos dos células,
#imprimimos como mensaje ‘¡Somos 2 clones!’ , pero en la segunda vuelta serán en total 4 células
#y el mensaje a imprimir debería ser ‘¡Somos 4 clones!’.
#¿Podrías escribir esta modificación del programa?

total = 0
for i in range(0,20):
    total += 2
    print('¡Somos {total_clones} clones nuevos!'.format(total_clones = total))