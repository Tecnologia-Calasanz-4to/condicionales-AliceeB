año= int(input("ingresa un año"))
if(año % 4)==0 and (año % 100) != 0 or (año % 400 )==0:
    print("año bisiesto")
else:
    print("año no bisiesto") 
