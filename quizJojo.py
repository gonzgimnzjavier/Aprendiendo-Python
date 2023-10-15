# Programa en Python quiz sobre la serie manga de Jojo
puntuacion = 0
titulo = "Bienvenido al Quiz sobre la serie manga de Jojo's Bizarre Adventure"
print("-" * len(titulo))
print(titulo)
print("-" * len(titulo))
input("Presiona enter para comenzar")
print("")
pregunta = input("¿En la parte 4, Diamond is Unbreakable, ¿cuál es el nombre del arco argumental centrado en el antagonista Yoshikage Kira?"
    "\na) Sheer Heart Attack\nb) Killer Queen\nc) Bites the Dust\n").lower()
if pregunta == "a":
    puntuacion += 1
elif pregunta == "b":
    puntuacion += 2
elif pregunta == "c":
    puntuacion += 3
else:
    print("Las respuestas son a, b o c")
    exit()
pregunta = input("¿En qué año se publicó por primera vez el manga de Jojo's Bizarre Adventure?\n"
    "a) 1980\nb) 1987\nc) 1989").lower()
if pregunta == "a":
    puntuacion += 1
elif pregunta == "b":
    puntuacion += 3
elif pregunta == "c":
    puntuacion += 2
else:
    print("Las respuestas son a, b, c o d")
    exit()

pregunta = input("¿Cual es el nombre del stand de Enya?\n"
    "a) Strength\nb) Wheel of Fortune\n""c) Justice\n").lower()
if pregunta == "a":
    puntuacion += 1
elif pregunta == "b":
    puntuacion += 2
elif pregunta == "c":
    puntuacion += 3
else:
    print("Las respuestas son a, b, c o d")
    exit()

if puntuacion == 9:
    print("Has acertado todas: Di Molto!")
elif puntuacion < 9 and puntuacion > 6:
    print("Has acertado muchas: Nice Nice very Nice Caser-chan")
elif puntuacion < 6 and puntuacion > 4:
    print("Has acertado algunos: Yare Yare Daze")
else:
    print("Has fallado bastante: Nani???")


