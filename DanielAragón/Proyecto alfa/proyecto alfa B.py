print("**********BIENVENIDOS**********")
print("**** Inicio de sesión****")

with open("usuarios.txt") as usuarios:
    usuarios = usuarios.readlines()
    diccionarioA = {}
    diccionarioB = {}
    diccionarioC = {}
    intentos = 0
    print("intento ", intentos,"de 3")
    usu=1
    u=input("Usuario: ")
    c=input("Contraseña: ")
for usuario in usuarios:
    u==usuario.split('|')[0] and c==usuario.split('|')[1]      
if  u==usuario.split('|')[0] and c==usuario.split('|')[1]:
    print("Hola")
##           with open("peliculas.txt") as peliculas:
##                        peliculas = peliculas.readlines()
##                        peli=1
##            for pelicula in peliculas:
##                print(peli,'.',pelicula)
##                peli+=1
else:
    intentos+=1
            