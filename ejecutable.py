import panzer
# a little Spanish and English translating you idiots
print(
    """
    [Bienbenido]

    * para salir de la ejecucion presiona 'e' si no quieres salir de la ejecucion presiona intro y la ejecucion seguira

    * si quieres salir de la ejecucion en cualquier parte que este presiona 'ctrl + c'

    1* primero le ba a preguntar hasta que numero desea iterar, esto es importante si no sabe binario por que al
    2* poner un numero le aparecera el numero y ala derecha el numero en binario si ba a itera hasta el 7 ponga 8
    3* siempre ponga un numero mas de el que quiere poner

    5* despues le ba a preguntar el numero que desea poner,como ya saber el valor de un numero en binario solo
    6* tendra que poner un numero en entero para realizar una operacion bit a bit,(aqui no tiene que poner un numero mas)
    7* despues le ba a preguntar que letra desea poner, la letra y el numero soy importantes [LEA EL ARCHIBO panzer.py Y LO ENTENDERA]
    8* puede poner mas de una letra pero eso alteraria el numero que a puesto es decir si usted pone 4 y luego la letra aa dos veces
    9* ya no sera 4 el resultado sera 8 por so solo es recomendable poner una sola letra
    10* despues le ba a preguntar de nuevo que numero desea poner y despues la letra que desea poner
    11* solo puede hacer operaciones con dos operadores pero usted puede extenderlo mas
    12* despues de que a puesto el numero y la letra,
    13* [SE LE MOSTRARA LA LETRA QUE A PUESTO Y EL NUMERO EN BINARIO Y EL NUMERO QUE A PUESTO]
    14*
    15* despues le dira en que operador bit a bit quiere tener el resultado
    16* le retornara el resultado
    17*  
    """ 

)
def bit():
    try:
        leave = input(
             """\nsalir: "
             
        [si quieres abanzar presiona INTRO!]
        \n"""
        )
             
            
    
        if leave == "e":
            return print("\na salido de la funcion\n")
        
        
        black_penis = int(input("escriba hasta que numero quiere iterar: "))
        
        viagra_for_your_micro_penis = 0

        for x in range(black_penis):          
            print(             
                f"""                
              {viagra_for_your_micro_penis} = {bin(viagra_for_your_micro_penis)}            
                """
            )
            viagra_for_your_micro_penis += 1  
            
        
        a = panzer.Fun_1()
    
        print(
            f"""
            \nla longitud de la cadena de caracteres de <<{a.c}>> en binario: {bin(len(a.c))} y en entero <{len(a.c)}>\n"""
            )

        b = panzer.Fun_1()
        print(f"\nla longitud de la cadena de caracteres de <<{b.c}>> en binario: {bin(len(b.c))} y en entero <{len(b.c)}>\n")
        
        
        wrinkled_anus = input(
            """
        [EN QUE OPERADOR BIT A BIT QUIERES TENER EL RESULTADO]
        |
        |----------* & == AND
        |
        |----------* | == OR
        |
        |----------* ^ == XOR
        |
        |----------* ~ == NOT
        |
        |----------* << corrimiento de bits ala izquierda = [multiplicacion],!(escriba i)
        |
        |----------* >> corrimiento de bits ala derecha = [divicion],!(escriba d)

        !puedes escribir en mayusculas o menuscalas!...

            """
        )

    
        resultado1 = len(a.c)
        resultado2 = len(b.c)
        
        if wrinkled_anus.upper() == "I":
            print(f"\nel resultado en coma flotante: {float(resultado1 << resultado2)}")
            print(f"el resultado en binario: {bin(resultado1 << resultado2)}")
            print(f"el resultado en numero entero: {resultado1 << resultado2}\n")

        if wrinkled_anus.upper() == "D":
            print(f"\nel resultado en coma flotante: {float(resultado1 >> resultado2)}")
            print(f"el resultado en binario {bin(resultado1 >> resultado2)}")
            print(f"el resultado en numero entero: {resultado1 >> resultado2}")
        
        if wrinkled_anus.upper() =="AND":
            print(f"\nel resultado en coma flotante: {float(resultado1 & resultado2)}")
            print(f"el resultado en binario: {bin(resultado1 & resultado2)}")
            print(f"el resultado en numero entero: {resultado1 & resultado2}\n")

        if wrinkled_anus.upper() == "OR":
            print(f"\nel resultadoen coma flotante: {float(resultado1 | resultado2)}")    
            print(f"el resultado en binario: {bin(resultado1 | resultado2 )}")
            print(f"el resultado en numero entero: {resultado1 |resultado2}\n")

        if wrinkled_anus.upper() == "XOR":
            print(f"el resultado en coma flotante: {float(resultado1 ^ resultado2)}")
            print(f"el resultado en binario: {bin(resultado1 ^ resultado2 )}")
            print(f"el resultado en numero entero: {resultado1 ^ resultado2}\n")

        if wrinkled_anus.upper() == "NOT":
            print(f"\nel resultado en coma flotante del primer numero: {float(~resultado1)}")
            print(f"el resultado en binario del primer numero: {bin(~resultado1)}")
            print(f"el resultado en numero entero {~resultado1}\n")
            print(f"\nel resultado en coma flotante del segundo numero: {float(~resultado2)}")
            print(f"el resultado en binario del segundo numero: {bin(~resultado2)}")
            print(f"el resultado en numero entero: {~resultado2}\n")

        
        recursion = input("dar recursion: ")
        
        if recursion == "0":
            return bit()

        if recursion == "":
            return bit()

    except KeyboardInterrupt as f:
        print(f"\nhas interrumpido la ejecucion de la funcion con ctrl + c {f}")
        
bit()


