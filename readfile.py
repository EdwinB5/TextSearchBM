class ReadFile:
	'''
	Esta clase permite leer archivos de texto
	de dos maneras, verificando de tal manera
	que solo sean archivos de texto y asigne un
	contenido de tipo lista de líneas o una
	cadena de texto
	'''
	def __init__(self, path:str='', file_name:str=''):
		'''
		Constructor de la clase ReadFile
		:param path: la ruta donde estará el archivo
		:type path: str
		:param file_name: el nombre del archivo
		:type file_name: str
		'''
		self.path = path
		self.file_name = file_name
		self.file_location = path + file_name
		self.content = None
		self.extension = None

	def get_extension(self):
		'''
		Esta función obtiene la extensión del archivo
		y la almacena en los atributos de la clase
		'''
		self.extension = str(self.file_name[len(self.file_name)-3:])

	def read_txt_string(self):
		'''
		Esta función lee el archivo de texto a manera
		de cadena de texto y la asigna al contenido
		'''
		self.get_extension()

		if self.extension == 'txt':
			open_file = open(self.file_location, 'r')
			text = open_file.read()
			self.content = text

			#self.print_txt()

	def read_txt_lines(self):
		'''
		Esta función lee el archivo, línea a línea
		y lo almacena todo en una lista
		'''
		lines = []
		self.get_extension()

		if self.extension == 'txt':
			open_file = open(self.file_location, 'r')
			lines = open_file.readlines()
			self.content = lines
			open_file.close()
			
			#self.print_lines()
		else:
			self.content = 'El archivo no es txt, por favor intenta de nuevo...'

	def print_lines(self):
		'''
		Esta función imprime el contenido, si solo sí el 
		contenido es una lista
		'''
		if type(self.content) == list:
			print(f'Archivo {self.file_name}')
			count = 1
			for line in self.content:
				line = line.replace('\n', '')
				print(f'{count}. {line}')
				count += 1

	def print_txt(self):
		'''
		Esta función imprime el contenido, si solo sí el
		contenido es una cadena de texto
		'''
		if type(self.content) == str:
			print(f'Archivo {self.file_name}')
			print(self.content)

	def get_content(self):
		'''
		Esta función permite recuperar el contenido de la clase,
		siendo este el contenido del archivo
		'''
		return self.content