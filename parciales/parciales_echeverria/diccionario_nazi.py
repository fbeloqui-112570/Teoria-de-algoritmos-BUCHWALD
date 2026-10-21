"""2) GREEDY (Sugerido): Alan Turing y su equipo están trabajando a contrarreloj para descifrar el código de comunicación de los
submarinos nazis. Se sabe que usan un algoritmo de sustitución simple: cada letra la reemplazan por otra letra específica. Los
espacios y los signos de puntuación no se cambian. La clave (es decir, qué letra reemplaza a cada una) se cambia diariamente por
otra clave similar. A las 6 AM reciben el primer mensaje del día con la nueva clave y quieren descifrarlo cuanto antes, para que
sea de utilidad. Para ello se centran en las palabras de cuatro letras del mensaje. Toman una lista de 20 palabras del mensaje.
También tienen un “diccionario” donde están casi todas las palabras de 4 letras que suelen usar los submarinos.
Desarrollar un algoritmo que encuentre una clave que traduzca las palabras de la lista y por lo menos 15 de ellas se encuentren
en el diccionario."""


def traduccion(mensaje: str, diccionario):
    palabras = mensaje.split()  # asumo que puedo ordenar esto por 4 letras
    palabras_traducidas = []
    primeras_veinte = []
    contador = 0
    for i in range(20):
        primeras_veinte.append(palabras[i])
    for palabra in primeras_veinte:
        if palabra in diccionario:
            palabras_traducidas.append(diccionario[palabra])
            contador += 1
    texto_traducido = "".join(palabras_traducidas)
    if contador >= 15:
        return texto_traducido
    return ""
