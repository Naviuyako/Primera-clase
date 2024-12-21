print("Este es un diccionario con el cual podras entender palabras desconocidas de la cultura POP, escriba EXIT si quiere salir")

meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "una respuesta a una broma",
            "SHEESH": "ligera desaprobación",
            "CREEPY ": "aterrador, siniestro"
            }
for i in range(5):
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if word in meme_dict.keys():
        print("el significado de", word, "es:", meme_dict[word])
    elif word == "EXIT":
        break
    else:
        print("La palabra", word, "no esta en el diccionario")

print("El programa se ha cerrado") 

        
