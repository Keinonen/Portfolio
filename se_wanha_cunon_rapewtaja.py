#se wanhan cunon ciälen rapewtaja

def SMgeneroi(mjono):
    if (len(mjono) == 0):
        return "Picaisin näcemisin!"

    mjono = mjono.replace("ks", "x")
    mjono = mjono.replace("k", "c")
    mjono = mjono.replace("K", "C")
    mjono = mjono.replace("j", "i")
    mjono = mjono.replace("J", "I")
    mjono = mjono.replace("uu", "w")
    mjono = mjono.replace("Uu", "W")
    mjono = mjono.replace("eu", "w")
    

    # for i in range (1, len(mjono)):
    #     print(i)
    #     print(mjono)
    #     if ((mjono[i]) == mjono[i-1]):
    #         mjono = mjono.replace(mjono[i], "")
    #         continue



    # mjono = list(mjono.rstrip())

    # j = 0
    # for i in range(len(mjono)):
    #     print(i)
    #     # If current character S[i]
    #     # is different from S[j]
    #     if (mjono[j] != mjono[i]):
    #         j += 1
    #         mjono[j] = mjono[i]
     
    # j += 1
    # mjono = mjono[:j]

    # mjono = (*S1, sep = "")
    
    return mjono
 
syote = "0" 
while (len(syote) != 0):    #silä wälin cieros cäytäiäle, sisän päin napin painaluxela tacaisin imeisten mailman
    syote = str(input("Cirioitapa cynäläs', mietesi selwäxi muta: "))
    print(SMgeneroi(syote))