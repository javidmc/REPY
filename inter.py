import re

##NO OLVIDAR: importa el tipo en las variables asi que tener ojo con eso.

rust = []

#crea una lista con el contenido del archivo de texto
texto = open("codigo_rust.txt")
for linea in texto:
    rust.append(linea)
texto.close()
###

#expresiones regulares
#funcion = re.compile('fn \S+ ( \S+ : \S+ ) - > \S+ {') 
variable = re.compile('let mut \S+ : \S+ = \S+ ;')
asignacion = re.compile('\S+ = \S+ ;')
mas = re.compile('\+')
menos = re.compile('-')
mayor_igual = re.compile('>=')
menor_igual = re.compile('<=')
mayor = re.compile('>')
menor = re.compile('<')
igual = re.compile('=')
printeo = re.compile('println!') ##arreglar esto.


#for ln in rust:
#    if 








###########################MAIN###################
#def main(codigo_rust):
    
