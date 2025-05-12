print("¡Ingrese sus 8 notas de Introduccion al calculo! (Use un digito decimal)")
S = 0.0
L = []
contador = 0

while contador <8:
    N = float(input())
    if (N < 1) or (N > 7):
        print("Por favor ingrese una Nota entre 7 y 1")
    else:
        L.append(N)
        contador += 1

for y in range(2):
    P = min(L)
    PO = L.index(P)
    L.pop(PO)

for z in range(6):
    S += L[z]

F = round(S / 6, 2)

if F >= 4.50:
    print("¡Felicidades! Pasaste el ramo de Introduccion al Calculo.")
    print("Tu promedio es:", F)
elif F < 4.50 and F >= 4.00:
    print("¡¡SALVASTE!! Pasaste el ramo de Introduccion al Calculo por lo justo.")
    print("Tu promedio es:", F)
elif F < 4.00:
    print("Lo lamento, te hechaste el ramo 🤣")
    print("Tu promedio es:", F)