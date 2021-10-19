from readfile import ReadFile
from boyer_moore import buscar
from writefile import WriteFile

class ControladorBM:
	'''
	Esta clase se encarga de integrar todos los
	componentes, creando así el funcionamiento
	del programa
	'''
	def __init__(self):
		'''
		Constructor de la clase ControladorBM
		'''
		self.opcion = None

	def menu_usuario(self):
		'''
		El menu que se desplega al usuario al ingresar al 
		programa
		'''
		print('-'*45)
		print('Bievenido al programa de búsqueda de texto BM')
		while True:
			print('-'*45)
			print('1. Introducir archivo de texto')
			print('2. Introducir texto mediante consola')
			print('3. Salir')
			print('-'*45)
			opcion = str(input('--> '))
			print('-'*45)
			try:
				if int(opcion) < 4 and int(opcion) != 0:
					self.opcion = opcion
					break
				else:
					print('Opcion no válida, intente otra vez...')
					
			except:
				print('Opcion no válida, intente otra vez...')
				
	def texto_pantalla(self):
		'''
		El proceso que se ejecuta si el usuario solicita
		digitar la información por pantalla
		'''
		lineas_indice = []
		list_contenido = []
		
		print('-'*45)
		contenido = str(input('Introduzca el contenido: '))
		print('-'*45)
		list_contenido.append(contenido)
		patron = str(input('Introduzca el patron: '))
		print('-'*45)
		encontrado = buscar(contenido=contenido, patron=patron)
		lineas_indice.append(encontrado)

		escribir_archivo = WriteFile(contenido = list_contenido, patron=patron, lista_coincide=lineas_indice)
		escribir_archivo.seleccionar_texto()


	def preguntar_usuario_archivo(self):
		'''
		En caso de que el usuario digite la opción
		de archivo, se le solicita que introduzca el nombre
		:returns: el nombre del archivo
		:rtype: str
		'''
		print('-'*45)
		print('El archivo debe estar en la carpeta entrada...')
		archivo = str(input('Introduzca el nombre del archivo: '))
		return archivo

	def usar_archivos(self):
		'''
		Implementación del código para archivos de texto
		'''
		lineas_indice = []

		archivo_entrada = self.preguntar_usuario_archivo()
		archivo = ReadFile(nombre_archivo=archivo_entrada)
		archivo.leer_txt_lineas()

		if archivo.existe:
			contenido_archivo = archivo.obtener_contenido()
			archivo.imprimir_lineas()
			print('-'*45)
			patron = str(input('Introduzca el patron: '))
			print('-'*45)

			for linea in contenido_archivo:
				encontrado = buscar(contenido=linea, patron=patron)
				lineas_indice.append(encontrado)

			escribir_archivo = WriteFile(contenido = contenido_archivo, patron=patron, lista_coincide=lineas_indice)
			escribir_archivo.seleccionar_texto()

	def ejecutar_programa(self):
		'''
		Esta función integra todos los componentes
		descritos en el menú en una sola función
		haciendo los llamados necesarios
		'''
		self.menu_usuario()

		if self.opcion == '1':
			print('Utilizando archivos de texto...')
			self.usar_archivos()
		elif self.opcion == '2':
			print('Utilizando texto en pantalla...')
			self.texto_pantalla()
		elif self.opcion == '3':
			return
