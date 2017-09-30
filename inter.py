import re

##NO OLVIDAR: importa el tipo en las variables asi que tener ojo con eso.

#crea una lista con el contenido del archivo de texto
# texto = open("codigo_rust.txt")


###

#expresiones regulares

declaracion = re.compile('\s*let mut ([A-z]+_*[A-z]*) : (i16|i32|f64) = ((-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+)|([A-z]+_*[A-z]*)|(([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+)|\(([A-z]+_*[A-z]*) as (i16|i32|f64)\)) (\+|\-) (([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+)|\(([A-z]+_*[A-z]*) as (i16|i32|f64)\))|(([A-z]+_*[A-z]*)\((([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+))\)));')
asignacion = re.compile('\s*([A-z]+_*[A-z]*) = ((-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+)|([A-z]+_*[A-z]*)|(([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+)|\(([A-z]+_*[A-z]*) as (i16|i32|f64)\)) (\+|\-) (([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+)|\(([A-z]+_*[A-z]*) as (i16|i32|f64)\))|(([A-z]+_*[A-z]*)\((([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+))\)));')
operacion = re.compile('\s*((([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+)|\(([A-z]+_*[A-z]*) as (i16|i32|f64)\))\s*(\+|\-)\s*(([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+)|\(([A-z]+_*[A-z]*) as (i16|i32|f64)\)));?')
casteo = re.compile('\s*(\(([A-z]+_*[A-z]*) as (i16|i32|f64)\));?')
ctrl_if = re.compile('\s*if ([A-z]+_*[A-z]*) (>|<|=|<=|>=) (([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+)) {')
ctrl_elseif = re.compile('\s*} else if ([A-z]+_*[A-z]*)\s*(>|<|=|<=|>=)\s*(([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+)) {')
ctrl_else = re.compile('\s*} else {')
fin = re.compile('\s*}')
ctrl_while = re.compile('\s*while ([A-z]+_*[A-z]*)\s*(>|<|=|<=|>=)\s*(([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+)) {')
boolean = re.compile('(\s*[A-z]+_*[A-z]*)\s*(>|<|=|<=|>=)\s*(([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+))')
printeo = re.compile('\s*println!\s*\(([A-z]+_*[A-z]*)\);') 
funcioninit = re.compile('fn ([A-z]+_*[A-z]*) \(([A-z]+_*[A-z]*):(i16|i32|f64)\) - > (i16|i32|f64) {')
ret = re.compile('\s*return\s*(([A-z]+_*[A-z]*)|(([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+)|\(([A-z]+_*[A-z]*) as (i16|i32|f64)\)) (\+|\-) (([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+)|\(([A-z]+_*[A-z]*) as (i16|i32|f64)\))|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+));')
fun_main =re.compile('fn main\(\) {')
funcion=re.compile("(([A-z]+_*[A-z]*)\((([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+))\))")










###########################MAIN###################
def guardar_fn(linea,dic):
	nombre=linea.strip("{").split(" ")[1]
	tipo_input=linea.strip.split("(")[1].split(")")[0].split(":")[1]
	tipo_output=linea.strip("{").split(" ")[5]
	dic[nombre][0]=tipo_input
	dic[nombre][1]=tipo_output
	dic[nombre][2]=[]
	for linea in texto:
		dic[nombre][2].append(linea)
		if re.match(ret,linea):
			break
	return 1
def asignar(linea,dic):
	



texto = open("codigorust.txt", 'r')
main_var={}
	








texto.close()

