nombre = "waffle"
energia = 100
felicidad = 100
print(f"Energia inicial de: {nombre}. energia: {energia}, felicidad: {felicidad} ")
while energia > 0:
    print("n\¿Que quieres hacer: ?")
    print("1.- Alimentar")
    print("2.- Jugar")
    print("3.- Ver estado de salud")
    print("4.- No hacer nada")
    opcion = input("Seleccione: ")
    if opcion == "1":
        energia = energia + 20
        felicidad = felicidad + 1
        print(f"Alimentaste a {nombre}, esta muy feliz contigo.. ")
    elif opcion == "2":
        energia = energia - 15
        felicidad = felicidad + 20
        print(f"{nombre} esta cansado")
    elif opcion == "3":
        print(f"Energia: {energia}")
        print(f"Felicidad: {felicidad}")
    elif opcion == "4":
        felicidad = felicidad - 10
        energia = energia - 5
        print(f"{nombre} esta muy aburrido")
    else:
        print("error de ingreso")        
