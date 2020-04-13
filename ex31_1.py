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

    print(f"\nEn serio crees que Ruben es asi de disciplinado?\n\njejeje pues fijate que no estás tan mal...\n\nEs correcto, Ruben cada mañana se levanta muy temprano como pajarito madruguero y lo primero que hace es arreglar su cama, sepillarse los dientes, tomar una ducha y comer su desalluno para prepararse para lo que le traiga el día")
    print(f"\n\nAunque con la pandepia producida por el nuevo COVID-19 estamos confinados a una cuarentena y todos los dias empiezan a ser un poco iguales...")
    print(f"\nQué crees que hace Ruben despues que se levanta en dias de pandemia?\n\n\t1. Empieza a trabajar diligentemente por horas hasta el cansansio.\n\t2. Se toma 5 min para prepararse mentalmente a su rutina diaria. \n\t3. Ve el Wasap y Facebook para actualizarce de los eventos sociales mas importantes en las ultimas 8 horas.\n\t4. Busca como loco a su esposa para llenarse de alegria viendola como cresce su bebe en su barriguita""")
    print("\nEscribe tu opcion")

    input_1_en_dias_de_pandemia = input(">>> ")
    if(input_1_en_dias_de_pandemia == "1"):

        print(f"ok tu opcion fue ->>> {input_1_en_dias_de_pandemia}")
        print("hey hey... en serio crees que Rubén es una máquina?\nSabemos que el pana es disciplinado y todo pero tampoco un esclavo")

    elif(input_1_en_dias_de_pandemia == "2"):
        print(f"ok tu opcion fue ->>> {input_1_en_dias_de_pandemia}")
        print(f"no es una mala opcion {user_name}, siempre es bueno meditar antes de empezar un largo y misteriosos dia pandemico")

    elif(input_1_en_dias_de_pandemia == "3"):
        print(f"ok tu opcion fue ->>> {input_1_en_dias_de_pandemia}")
        print(f"La opción {input_1_en_dias_de_pandemia} es tal vez lo más probable que esté pensando Eliane (la esposa de Ruben) sobre lo que hace ruben todo el dia...")

    elif(input_1_en_dias_de_pandemia == "4"):

        print(f"ok tu opcion fue ->>> {input_1_en_dias_de_pandemia}")
        print(f"ok ahora ya lo tienes,\nRuben probablemente se siente la persona mas afortunada en este mundo al lado de su esposa que gesta su bebe, que es ahora su motivacion, su energia e isnpiracion de seguir cada dia con su rutina diaria")
    else:
        print(f"ok tu opcion fue ->>> {input_1_en_dias_de_pandemia}")
        print(f"Esa opcion no estaba planificada... \npero porque no? siempre se pueden aceptar sugerencias")
        print("Quieres que Ruben haga algo nuevo en su set de rutinas?")
        input("\nEnter para continuar o \"CTRL+C or (^C)\" para dejarlo hasta aqui.")
        new_rutine_foor_ruben = input("\nQue le sugeririas a Ruben que incluya en su rutina?\n>>>")
        print(f"ok\nPasaremos tu propuesta \"{new_rutine_foor_ruben}\" al departamento de sugerencias (Eliane es la Jefa) y te contactaremos si es aprobado.\nGracias {user_name}, hasta pronto...")

elif(ruben_al_depertar == "2"):

    print(f"\nTu opcion fue {ruben_al_depertar}, no bad..., pero subestimas la disciplina de Ruben.\n\nEn verdad en que concepto tienes al pobre Ruben??? \nDecepcionante...""")

else:
    print(f""" la opcion \"{ruben_al_depertar}\" no es valida."""  )
