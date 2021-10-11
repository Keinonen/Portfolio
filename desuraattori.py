#desuraattori

import random


def SMgeneroi(mjono):
    if (len(mjono) == 0):
        return "Voi piggu minkä desu yoooo teit!\"32!! (╬⓪益⓪)(╬⓪益⓪)"
    
    mjono = mjono.lower()
    for i in range (0,len(mjono)):
        if (mjono[i] == "l"):
            mjono = mjono.replace(mjono [i], "r")

    vali = ["（‐＾▽＾‐）", "(*´ω｀*))", "(´・ω・`)*", "(* ´ο`*)", "( ͡° ͜ʖ ͡°)", "｢(＝＞o≦＝)ﾉ", "( ´ ∀ ` )", "( ﾟДﾟ)＜!!", "(╬⓪益⓪)", "(☼Д☼)", "（・□・；）", "(　´Д｀)・;’.", "(￣￢￣)", "(ತ◞౪◟ತ ‵)", "_:(´ཀ`」∠):_"]
    lista = mjono.split(" ")

    for x in range (0,len(lista)):  #vali-lisäykset
        lisays = vali[random.randint(0,len(vali) - 1)] #vali-listan parametrit
        if random.randint(0,2) == 2: #lisäysten todennäköisyys
                if lisays not in lista: 
                    lista.insert(random.randint(x,len(lista) - 1), lisays)
                     
    tulos = " "
    tulos = tulos.join(lista)
    
    
    
    return tulos


syote = "0" 
while (len(syote) != 0):    #while-loop käyttäjälle, lopetus enterillä/tyhjällä syötteellä
    syote = str(input("Japaniraista des!#1\"! ( ´ ∀ ` ): "))
    print(SMgeneroi(syote))