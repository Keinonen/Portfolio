#setämies(de)generaattori
import random


def SMgeneroi(string):
    alku = "," * random.randint(1,4)
    loppu = "," * random.randint(2,3) + ")" * random.randint(3,6)
    vali = ["*LUUUURPS*", "hmhmhm", "*nuuh-nuuh*", "*märskistä*", "*nams*", "pillu-eläinprkl", "(setä tykköö)", "(tuotaku lipasis)" + "," * random.randint(0,3) + ")" * random.randint(1,4) ]
    pilkut = "," * random.randint(1,4)
    lista = string.split(" ");
    
    for x in range (0,len(lista)):  #vali-lisäykset
        lisays = vali[random.randint(0,len(vali) - 1)] #vali-listan parametrit
        if random.randint(0,2) == 2: #lisäysten todennäköisyys
                if lisays not in lista: 
                    lista.insert(random.randint(x,len(lista) - 1), lisays)
    
    for x in range (0,len(lista), random.randint(1,3)): #pilkkujen lisäys
        if random.randint(0,2) == 2: #pilkkujen todennäköisyys
            lista[x] = lista[x] + "," * random.randint(2,3)
                     
    tulos = " "
    tulos = tulos.join(lista)
    
        
    
    return tulos
 
#print("," * random.randint(2,6))

print(SMgeneroi(input("Setämiehistä: ")))

#print(SMgeneroi("testi"))