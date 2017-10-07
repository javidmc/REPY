import re

##NO OLVIDAR: importa el tipo en las variables asi que tener ojo con eso.

#crea una lista con el contenido del archivo de texto
# texto = open("codigo_rust.txt")


###

#expresiones regulares

declaracion = re.compile('\s*let mut ([A-z]+_*[A-z]*) : (i16|i32|f64) = ((-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+)|([A-z]+_*[A-z]*)|(([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+)|\(([A-z]+_*[A-z]*) as (i16|i32|f64)\)) (\+|\-) (([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+)|\( ([A-z]+_*[A-z]*) as (i16|i32|f64) \))|(([A-z]+_*[A-z]*)\((([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+))\)));')
asignacion = re.compile('\s*([A-z]+_*[A-z]*) = ((-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+)|([A-z]+_*[A-z]*)|(([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+)|\( ([A-z]+_*[A-z]*) as (i16|i32|f64) \)) (\+|\-) (([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+)|\( ([A-z]+_*[A-z]*) as (i16|i32|f64) \))|(([A-z]+_*[A-z]*)\((([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+))\)));')
operacion = re.compile('\s*((([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+)|\( ([A-z]+_*[A-z]*) as (i16|i32|f64) \)) (\+|\-) (([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+)|\( ([A-z]+_*[A-z]*) as (i16|i32|f64) \)));?')
casteo = re.compile('\s*(\( ([A-z]+_*[A-z]*) as (i16|i32|f64) \));?')
ctrl_if = re.compile('\s*if ([A-z]+_*[A-z]*) (>|<|=|<=|>=) (([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+)) {')
ctrl_elseif = re.compile('\s*} else if ([A-z]+_*[A-z]*) (>|<|=|<=|>=) (([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+)) {')
ctrl_else = re.compile('\s*} else {')
fin = re.compile('\s*}')
ctrl_while = re.compile('\s*while ([A-z]+_*[A-z]*) (>|<|=|<=|>=) (([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+)) {')
boolean = re.compile('(\s*[A-z]+_*[A-z]*) (>|<|=|<=|>=) (([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+))')
printeo = re.compile('\s*println! \(([A-z]+_*[A-z]*)\);') 
funcioninit = re.compile('fn ([A-z]+_*[A-z]*)\(([A-z]+_*[A-z]*): (i16|i32|f64)\) - > (i16|i32|f64){')
ret = re.compile('\s*return (([A-z]+_*[A-z]*)|(([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+)|\( ([A-z]+_*[A-z]*) as (i16|i32|f64) \)) (\+|\-) (([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+)|\( ([A-z]+_*[A-z]*) as (i16|i32|f64) \))|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+));')
fun_main =re.compile('fn main\(\) {')
funcion=re.compile("(([A-z]+_*[A-z]*)\((([A-z]+_*[A-z]*)|(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+))\))")
numvalue=re.compile("(-[0-9]+|[0-9]+|[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+)")
varnm=re.compile("([A-z]+_*[A-z]*)")



###########################MAIN###################
def getvalue(operando, dic):
	if re.match(casteo, operando) and "." in dic[re.match(casteo,operando).group(1)][0]:
		return float(dic[re.match(casteo,operando).group(1)][0])
	elif re.match(casteo, operando):
		return int(dic[re.match(casteo,operando).group(1)][0])
	elif re.match(varnm, operando) and "." in dic[operando][0]:
		return float(dic[operando][0])
	elif re.match(varnm,operando):
		return int(dic[operando][0])
	elif re.match(numvalue, operando) and "." in operando:
		return float(operando)
	elif re.match(numvalue, operando):
		return int(operando)

def guardar_fn(linea,dic):
	varname=re.match(funcioninit,linea).group(2)
	nombre=re.match(funcioninit,linea).group(1)
	tipo_input=re.match(funcioninit,linea).group(3)
	tipo_output=re.match(funcioninit,linea).group(4)
	dic[nombre]=[]
	dic[nombre].append(tipo_input)
	dic[nombre].append(tipo_output)
	dic[nombre].append([])
	for linea in texto:
		dic[nombre][2].append(linea.strip())
		if re.match(ret,linea):
			break
	return 1

def castear(linea,dic):
	nombre=re.match(casteo,linea).group(1)
	tipo=re.match(casteo,linea).group(2)
	dic[nombre][1]=tipo
	return

def operar(linea):
	suma = 0
	operando1= re.match(operacion,linea).group(1)
	operando2= re.match(operacion,linea).group(3)
	operacion= re.match(operacion,linea).group(2)
	if dic[operando1][1] != dic[operando2][1]:
		print 'Error de tipo'
		exit(1)
	if operacion == '+': #ver en caso de que sen 3 variables en vez de 2
		suma = operando1 + operando2
	else:
		suma = operando1  - operando2
	return suma

def mostrar(linea):

	variable = re.match(printeo,linea).group(1)
	print 'El valor es: ' + str(variable)
	print '. Su tipo es:' + str(type(variable)) #reemplazar type(variable) por el tipo de la variable que esta en el dic
	
def variab(linea, dic):
	variable = re.match(declaracion,linea).group(1)
	print variable
	tipo =re.match(declaracion,linea).group(2)
	valor = re.match(declaracion,linea).group(3)
	dic[variable]=[]
	dic[variable].append(tipo)
	dic[variable].append(valor)
	return 1


texto = open("codigo_rust.txt", 'r')
main_var={} #{'nombrefuncion':[tipo input, tipo output, [codigo]] de las funciones antes que el main
main = {} #variables del main {'variable':[tipo, valor]}
for linea in texto:
	if re.match(funcioninit,linea):
		guardar_fn(linea,main_var) #[tipo input, tipo output, [codigo]]
	if re.match(printeo,linea):
		mostrar(linea)

	if re.match(declaracion,linea):
		variab(linea,main)
	if re.match(boolean,linea):




print main_var
print main
	








texto.close()
