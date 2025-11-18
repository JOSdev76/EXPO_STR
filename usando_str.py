#INGRESA UN TEXTO O PALABRA
texto = input("Ingresa un texto :")
print("\nTexto original :" ,texto)
print("Sin espacios al inicio/final :" ,texto.strip())
print("En mayusculas :",texto.upper())
print("Cantidad de caracteres :" , len(texto))
#INGRESA UNA PALABRA A BUSCAR DENTRO DE LO QUE ESCRIBISTE
palabra = input("Palabra a buscar :")
pos = texto.fiend(palabra)
if pos != -1:
   print(f"La palabra "{palabra}" se encontro en la posicion {pos}")
else:
   print("Palabra no encontrada")
#INGRESA UNA PALABRA DENTRO DEL TEXTO QUE QUIERES REEMPLAZAR
nuevo = input("Palabra a remplazar :")
#INGRESA UNA PALABRA QUE DESES REEMPLAZAR EJEMPLO : (hola mundo) PALABRA A REEMPLAZAR tierra -> (hola tierra)
reemp = input("Reemplazar por :")
print("Texto modificado :" , texto.replace(nuevo,reemp))

