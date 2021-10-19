class ReadFile:
	'''
	Esta clase permite leer archivos de texto
	de dos maneras, verificando de tal manera
	que solo sean archivos de texto y asigne un
	contenido de tipo lista de líneas o una
	cadena de texto
	'''
	def __init__(self, ruta:str='', nombre_archivo:str=''):
		'''
		Constructor de la clase ReadFile
		:param ruta: la ruta donde estará el archivo
		:type ruta: str
		:param nombre_archivo: el nombre del archivo
		:type nombre_archivo: str
		'''
		self.ruta = ruta
		self.nombre_archivo = nombre_archivo
		self.archivo_localizacion = ruta + nombre_archivo
		self.contenido = None
		self.extension = None

	def obtener_extension(self):
		'''
		Esta función obtiene la extensión del archivo
		y la almacena en los atributos de la clase
		'''
		self.extension = str(self.nombre_archivo[len(self.nombre_archivo)-3:])

	def leer_txt_lineas(self):
		'''
		Esta función lee el archivo, línea a línea
		y lo almacena todo en una lista
		'''
		lineas = []
		self.obtener_extension()

		if self.extension == 'txt':
			try:
				abrir_archivo = open(self.archivo_localizacion, 'r')
				lineas = abrir_archivo.readlines()
				self.contenido = lineas
				abrir_archivo.close()
			
			#self.imprimir_lineas()
			except:
				print('El archivo no existe, intenta de nuevo...')
		else:
			print('El archivo no es txt, por favor intenta de nuevo...')

	def imprimir_lineas(self):
		'''
		Esta función imprime el contenido, si solo sí el 
		contenido es una lista
		'''
		if type(self.contenido) == list:
			print('-'*45)
			print(f'Archivo {self.nombre_archivo}')
			print('-'*45)
			for linea in self.contenido:
				linea = linea.replace('\n', '')
				print(linea)

	def obtener_contenido(self):
		'''
		Esta función permite recuperar el contenido de la clase,
		siendo este el contenido del archivo
		'''
		return self.contenido