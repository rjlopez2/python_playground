print("""\nBienvenido al super super super
divertidisimo juego de la vida de Ruben """)
print("\nIntroduce tu nombre para empezar\n")
user_name = input(">>> ")
print(f"\nBienvenido {user_name} al mejor juego de tu vida")
print("""Este podria parecer un juego muy aburrido al principio pero...

Tal vez empiece a gustarte cuando te adrentres en el...

""")
input(f"""Quieres intentarlo {user_name}?

preisona Enter para continuar o para salir presiona \"CTRL+C or (^C)\".

>>> """ )
print(f"""\nA ver {user_name} empecemos con la rutina diaria de Ruben

Ruben cuando se levanta de la cama que crees que hace?

1. Se levanta como soldado y arregla inmediatamente su cama.
2. Apaga el despertador y duermem otros 5 min más.

Escribe acontinuacion tu opción""")
ruben_al_depertar = input(">>> ")

if(ruben_al_depertar == "1"):
    print("""En serio crees que Ruben es asi de disciplinado? jejeje pues
    fijate que no estás tan mal...
    Es correcto, Ruben cada mañana se levanta muy temprano como pajarito madruguero
    y lo primero que hace es arreglar su cama, sepillarse los dientes y tomar una ducha
    para prepararse para lo que le traiga el día""")

elif(ruben_al_depertar == "2"):

    print(f"""Tu opcion fue {ruben_al_depertar}, no bad..., pero subestimas la disciplina de Ruben.
    en verdad en que concepto tienes al pobre Ruben??? \nDecepcionante...""")

else:
    print(f""" la opcion {ruben_al_depertar} no es valida."""  )
