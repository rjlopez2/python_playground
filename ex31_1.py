print("""\nBienvenido al super super super
divertidisimo juego de 1 dia en la vida de Ruben """)
print("\nIntroduce tu nombre para empezar\n")
user_name = input(">>> ")
print(f"\nBienvenido {user_name}...")
print("""\nEste podria parecer un juego muy aburrido al principio pero...

Tal vez empiece a gustarte cuando te adrentres en el...
""")
input(f"""Quieres intentarlo?

preisona Enter para continuar o para salir presiona \"CTRL+C or (^C)\".

>>> """ )
print(f"""\nA ver {user_name} empecemos con la rutina diaria de Ruben

Ruben cuando se levanta de la cama que crees que hace?

\t1. Se levanta como soldado y arregla inmediatamente su cama.
\t2. Apaga el despertador y duermem otros 5 min más.

Escribe acontinuacion tu opción""")
ruben_al_depertar = input(">>> ")

if(ruben_al_depertar == "1"):

    print(f"\nEn serio crees que Ruben es asi de disciplinado?\n\njejeje pues fijate que no estás tan mal...\n\nEs correcto, Ruben cada mañana se levanta muy temprano como pajarito madruguero y lo primero que hace es arreglar su cama, sepillarse los dientes, tomar una ducha para prepararse para lo que le traiga el día")
    print(f"\n\nAunque con la pandepia producida por el nuevo COVID-19 estamos confinados a una cuarentena y todos los dias empiezan a ser un poco iguales...")
    print(f"\nQué crees que hace Ruben despues que se levanta en dias de pandemia?\n\n\t1. Empieza a trabajar diligentemente por horas hasta el cansansio.\n\t2. Se toma 5 min para prepararse mentalmente a su rutina diaria. \n\t3. Ve el Wasapt o Faceboof para actualizarce de los eventos sociales mas importantes en las ultimas 8 horas.\n\t4. Busca como loco a su espoza para llenarse de alegria viendola como cresce su bebe en su barriguita""")
    print("\nEscribe tu opcion")

    input_1_en_dias_de_pandemia = input(">>> ")
    if(input_1_en_dias_de_pandemia):

        print(f"ok tu opcion fue ->>> {input_1_en_dias_de_pandemia}")

elif(ruben_al_depertar == "2"):

    print(f"\nTu opcion fue {ruben_al_depertar}, no bad..., pero subestimas la disciplina de Ruben.\n\nEn verdad en que concepto tienes al pobre Ruben??? \nDecepcionante...""")

else:
    print(f""" la opcion \"{ruben_al_depertar}\" no es valida."""  )
