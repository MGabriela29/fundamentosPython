import random

int_rand = random.randint(0,2)

if int_rand == 0:
    choice_maq = "Piedra"
elif int_rand == 1:
    choice_maq = "Papel"
else:
    choice_maq = "Tijera"


#Elige usuario
choice_txt = """
Elige una Opcion:
    Piedra
    Papel
    Tijera
"""

Choice_user = input(choice_txt)

print("Maquina ->", choice_maq)
print("Usuario", Choice_user)

if choice_maq == Choice_user:
    print("Es un empate")
else:
    if choice_maq == "Piedra" and Choice_user == "Papel":
        print("Gano Usuario..!")
    elif choice_maq== "Piedra" and Choice_user == "Tijera":
        print("Gana Maquina")

    if choice_maq == "Papel" and Choice_user == "Tijera":
        print("Gano Usuario..!")
    elif choice_maq== "Papel" and Choice_user == "Piedra":
        print("Gana Maquina")

    if choice_maq == "Tijera" and Choice_user == "Piedra":
        print("Gano Usuario..!")
    else:
        print("Gana Maquina")
