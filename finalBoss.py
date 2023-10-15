# Juego de toma de decisiones
print("Despiertas en una habitación extraña con una sensación de confusión. Frente a ti, una figura misteriosa se materializa.\nTe informa que estás atrapado en un juego cósmico y que tu única esperanza de escapar es superar una serie de desafíos\nde toma de decisiones. Si fracasas, enfrentarás la muerte. Pero si tienes éxito, serás recompensado con la oportunidad de reencarnar.")
opcionesValidas = ["s", "n"]
while True:
    decision = input("¿Aceptas el desafío? (s/n)").lower()
    if decision == "s":
        break
    elif decision == "n" or decision != "s" or decision != "n":
        print("...")
        print("Me temo que no tienes otra opción a no ser que quiras quedarte en un limbo infinito.")
print("¡De acuerdo que comience el juego!")
opcionesValidas = ["a", "b", "c"]
while True:
    puerta=input("La figura desaprace dejando a la vista tres puertas de materiales diferentes a elegir:\na) madera\nb) metal\nc) oro\n").lower()
    if puerta in opcionesValidas:
        break
    else:
        print("Opcion invalida vuelve a intentarlo")
if puerta == "a":
    print("La puerta de madera te permite pasar")
    print("En ella encuentras un esqueleto parlante con un ojo de cristal.")
    print("Bienvenido camarada mi nombre es Femurcio y este es el desafio que te propongo")
    print("Tiraremos tres veces los dados cada uno y el que salga con mayor puntaje sera el ganador.")
    print("Si gano yo me quedare con tus huesos, pero si me ganas te dare mi ojo de cristal.")
    opcionesValidas = ["s", "n"]
    while True:
        decision = input("¿Qué me dices grumete Aceptas el desafío? (s/n)").lower()
        if decision == "s":
            break
        elif decision == "n" or decision != "s" or decision != "n":
            print("Es una pregunta retorica ni te molestes en contestar cualquier otra cosa que no sea un sí.")
    print("¡Entonces no esperemos más!")
    print("El juego de los dados comienza")
    import random
    puntajeProtagonista = 0
    puntajeFemurcio = 0
    contador = 0
    tienesOjoDeCristal = False
    while contador < 3:
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        contador += 1
        input("Presiona enter para tirar los dados por "+str(contador)+"ª vez")
        print(dado1, dado2)
        if dado1 > dado2:
            puntajeProtagonista += 1
        elif dado1 < dado2:
            puntajeFemurcio += 1
        elif dado1 == dado2:
            puntajeProtagonista += 1
            puntajeFemurcio += 1
    if puntajeProtagonista > puntajeFemurcio:
        print("¡Ganaste lo prometido es deuda! Te entrego mi ojo de cristal")
        tienesOjoDeCristal = True
    else:
        print("Me temo que has perdido")
    print("Pasa a la siguiente sala en ella se decidira tu destino.")
    print("Entras en la sala y en ella divisas un altar.")
    print("Una voz empieza a comunicarse contigo")
    print("Oh alma en pena deja tu ofrenda y que tu destino sea decido por el dios de lo material")
    if tienesOjoDeCristal:
        print("Depositas el ojo de Femurcio en el altar")
        print("Gracias por tu ofrenda ahora podras disfrutar de tu nueva vida recarnandote en nuevo ser")
        print("Has ganado y te has rencarnado en un nuevo ser")
        print("Fin del juego, Gracias por participar")
    else:
        print("No puedes depositar nada")
        print("Como osas decir que no")
        print("Fumercio quedate con los huesos de este ser")
        print("Fin del juego, Gracias por participar")

elif puerta == "b":
    print("La puerta de metal te permite pasar")
    print("En ella te encuentras un zombie")
    print("Hola mi nombre es Mike y este es el desafio que te propongo")
    print("Jugaremos 5 veces a piedra papel o tijera al perdedor se le arrancara el dedo en cada intento")
    print("Te preguntaria si quieres participar pero tampoco es que tengas otra opción")
    print("Así que comencemos")
    import random
    dedosProtagonista = 0
    dedosMike = 0
    contador = 0
    manodeMike = ""
    tienesSuficienteDedos = False
    while contador < 5:
        fortuna=random.randint(1, 3)
        contador += 1
        if fortuna == 1:
            manodeMike = "piedra"
        elif fortuna == 2:
            manodeMike = "papel"
        else:
            manodeMike = "tijera"
        manodelJugador = input("Escoge entre piedra, papel o tijera: ").lower()
        if (manodelJugador == "piedra" and manodeMike == "papel") or (manodelJugador == "papel" and manodeMike == "tijera") or (manodelJugador == "tijera" and manodeMike == "piedra"):
            print("Mike saca "+manodeMike)
            print("Mike te arranca un dedo")
            dedosMike += 1
        elif (manodelJugador == "piedra" and manodeMike == "piedra") or (manodelJugador == "papel" and manodeMike == "papel") or (manodelJugador == "tijera" and manodeMike == "tijera"):
            print("Mike saca "+manodeMike)
            print("Empate ambos jugadores conservan sus dedos")
        else:
            print("Mike saca " + manodeMike)
            print("Le arrancas un dedo a Mike")
            dedosProtagonista += 1
    if dedosProtagonista >=dedosMike:
        print("¡Ganaste!")
        tienesSuficienteDedos = True
    else:
        print("Me temo que has perdido")
    print("Pasa a la siguiente sala en ella se decidira tu destino.")
    print("Entras en la sala y en ella divisas un altar.")
    print("Una voz empieza a comunicarse contigo")
    print("¿Has traido algo de comer? Soy el dios de la Gula deja algun snack en el altar")
    print("Depositas el ojo de Femurcio en el altar")
    if tienesSuficienteDedos:
        print("Gracias por la comida ahora podras disfrutar de tu nueva vida recarnandote en nuevo ser")
        print("Has ganado y te has rencarnado en un nuevo ser")
        print("Fin del juego, Gracias por participar")
    else:
        print("No tienes suficiente dedos")
        print("Con el hambre que tengo y me dices que no")
        print("Entonces tendre que devorarte")
        print("Fin del juego, Gracias por participar")

elif puerta == "c":
    print("La puerta de oro te permite pasar")
    print("En ella te encuentras un buda dorado")
    print("Hola mi nombre es ChakraVartin y me encanta el dinero")
    print("La prueba que te propongo es simple")
    print("Tendremos que adivinar la fortuna que tuvo Elon Musk en diferentes años\nel que mas se acerque obtendra dinero \nel que acumule mas sera el ganador")
    print("No hay tiempo que perder que comience el juego")
    import random
    dineroProtagonista = 0
    dineroChakraVartin = 0
    contador = 0
    diferenciaJugador = 0
    diferenciaChakraVartin = 0
    suficienteDinero = False
    while contador < 3:
        anio = random.randint(2000, 2022)
        fortuna=random.randint(100000, 250000)
        numerodeChakraVartin =random.randint(90000, 350000)
        contador += 1
        opciondeljugador=int(input("Cunto dinero tuvo Elon Musk? en el año "+str(anio)+""))# Expresar en millones de dolares
        diferenciaJugador = abs(fortuna - opciondeljugador)
        diferenciaChakraVartin = abs(fortuna - numerodeChakraVartin)
        print("ChakraVartin ha apostado a que Elon Musk tuvo "+str(numerodeChakraVartin)+" millones de dolares")
        print("Elon Musk tuvo "+str(fortuna)+"  millones de dolares en el año "+str(anio))
        if diferenciaJugador > diferenciaChakraVartin:
            print("ChakraVartin gana la ronda")
            dineroChakraVartin += 1
        else:
            print("El jugador gana la ronda")
            dineroProtagonista += 1
    if dineroProtagonista >= dineroChakraVartin:
        suficienteDinero = True
        print("¡Ganaste!")

    else:
        print("Me temo que has perdido")
    print("Pasa a la siguiente sala en ella se decidira tu destino.")
    print("Entras en la sala y en ella divisas un altar.")
    print("Una voz empieza a comunicarse contigo")
    print("Necesito dinero para un lambo asi que date prisa soy el dios del capitalismo Y YA ESTOS PERDIENDO DINERO")

    if suficienteDinero:
        print("Depositas el dinero en el altar")
        print("Bien ahora disfruta de tu nueva vida llena de lujos un saludo fiera")
        print("Has ganado y te has rencarnado en un nuevo ser")
        print("Fin del juego, Gracias por participar")
    else:
        print("No tienes suficiente dinero")
        print("Y para esto me llamas en fin no se ni que hago perdiendo el tiempo")
        print("Quedas atrapado en el limbo")
        print("Fin del juego, Gracias por participar")



