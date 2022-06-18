import json
import random
import os

def borrar_consola():
    os.system("cls" if os.name=="nt" else "clear")


def carga_datos():
    arch=open("preguntas.json", "r")
    datos=arch.read()
    js=json.loads(datos)
    return js

def jugar():
    
    js=carga_datos()
    preguntas=list(js.keys())

    correctas=0
    incorrectas=0

    for i in range(len(preguntas)):
        preg_selec=preguntas[i]
        op_literal=js[preg_selec]["opciones"]
        random.shuffle(op_literal)
        print(js[preg_selec]["pregunta"])

        letras=['A','B','C','D','E']
        
        lista_preg_op=[]
        for x,y in zip(letras, op_literal):
            lista_preg_op.append((x,y))
            
            print(x,')',y)
        resp_user=input('Ingrese su respuesta (A - B - C - D - E): ')

        if resp_user.upper() in letras:
            c=0

            borrar_consola()
            for x,y in lista_preg_op:
                
                if (x==resp_user.upper()) and (y==js[preg_selec]["correcta"]):
                    c+=1
                    print(f'{x}) {y} --> Es la respuesta correcta!')
                    correctas+=1
            if c!=1:
                print(f'{resp_user.upper()})--> Es incorrecta!')
                incorrectas+=1

        else:
            print('Respuesta ingresada no está dentro de las opciones-----contabiliza como Incorrecta')
            incorrectas+=1
        
        
    print(f'Tu resultado es; Correctas: {correctas} e Incorrectas: {incorrectas} ')

def reintentar():

    resp=['A','B']
    
    seguir=True

    while seguir:
        continuar=input('Volver a jugar A) Si o B) No: ')  
        if  continuar.upper() in resp:
            if continuar.upper()=='A':
                seguir=True
                jugar()
            else:
                seguir=False
                borrar_consola()
                print('------Juego Finalizado----------')
        else:
            print('Respuesta mal ingresada')





