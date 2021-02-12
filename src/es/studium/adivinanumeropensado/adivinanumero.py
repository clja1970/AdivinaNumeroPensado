'''
Created on 12 feb. 2021

@author: clja1
'''
import math
mi=1
mx=1000
veces=0
lastnum=0
 
while True:
    try:
        num=math.floor((mx-mi)/2)+mi
        if num==lastnum:
            print(f"Ya no hay mas posibilidades. El numero que pensaste fue el {num}")
            respuesta="="
        else:
            respuesta=input(f"El numero es {num} (< = >) : ")
            veces+=1
    except KeyboardInterrupt:
        break
    if respuesta not in ["<", "=", ">"]:
        print("Tienes que indicar <, = o >")
        continue
    if respuesta=="<":
        mx=num
    elif respuesta==">":
        mi=num
    else:
        print(f"Descubri el numero en {veces} veces")
        break
    lastnum=num