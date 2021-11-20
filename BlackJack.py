from random import choice, sample

cartas = {
    chr(0x1f0a1): 11,
    chr(0x1f0a2): 2,
    chr(0x1f0a3): 3,
    chr(0x1f0a4): 4,
    chr(0x1f0a5): 5,
    chr(0x1f0a6): 6,
    chr(0x1f0a7): 7,
    chr(0x1f0a8): 8,
    chr(0x1f0a9): 9,
    chr(0x1f0aa): 10,
    chr(0x1f0ab): 10,
    chr(0x1f0ad): 10,
    chr(0x1f0ae): 10,
}

print("Cartas: {}".format(" ".join(cartas.keys())))
print("Puntos: {}".format(list(cartas.values())))

print("1\ Iteración estándar sobre un diccionario")
for carta, valor in cartas.items():
    print("la carta {} vale {}".format(carta, valor))

print("2\ Iteración ordenada sobre un diccionario")
for carta in sorted(cartas.keys()):
    print("la carta {} vale {}".format(carta, cartas[carta]))

print("3\ Black Jack")
lista_cartas = list(cartas)

print("Ha seleccionado:", end=" ")
carta = choice(lista_cartas)
score = cartas[carta]
print(carta, end=" ")
carta = choice(lista_cartas)
score += cartas[carta]
print(carta, end=" ")
print(" >>> su puntuación es de", score)

main_banca = sample(lista_cartas, 2)
score_banca = sum(cartas[carta] for carta in main_banca)

juega=True
while(juega==True):
    respuesta = input('¿Quieres seguir jugando?(S/N): ')
    if(respuesta=="s"):
        print("Su nueva seleccion es:", end=" ")
        carta = choice(lista_cartas)
        score += cartas[carta]
        print(carta, end=" ")
        print(" >>> su puntuación es de", score)
    elif(respuesta=="n"):
        juega=False
    else:
        print("La respuesta debe ser una N o una S.")
    if(score_banca<13):
        main_banca = sample(lista_cartas, 1)
    if(score>21):
        print("Te has pasado de 21.")
        juega=False
print("La banca tiene: {} {}  >> su score es {}".format(main_banca[0],
                                                          main_banca[1],
                                                          score_banca))
if(score_banca<score):
    print("Has ganado")
else:
    print("Has perdido")
