class ReadFile:
	def __init__(self, path:str='', file_name:str=''):
		self.path = path
		self.file_name = file_name
		self.file_location = path + file_name
		self.content = None
		self.extension = None

	def get_extension(self):
		self.extension = str(self.file_name[len(self.file_name)-3:])

	def read_txt(self):
		lines = []
		self.get_extension()

		if self.extension == 'txt':
			open_file = open(self.file_location)
			lines = open_file.readlines()
			self.content = lines
			open_file.close()
		else:
			self.content = 'El archivo no es txt, por favor intenta de nuevo...'

	def print_lines(self):
		print(f'Archivo {self.file_name}')
		if type(self.content) == list:
			count = 1
			for line in self.content:
				print(f'{count}. {line}')
				count += 1
		else:
			print(self.content)