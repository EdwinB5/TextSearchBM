class WriteFile:
	def __init__(self, contenido='', patron='', lista_coincide=[]):
		self.contenido = contenido
		self.patron = patron
		self.lista_coincide = lista_coincide
		self.caracteres_patron = len(self.patron)
		self.contenido_para_archivo = []
		self.copia_contenido = contenido[:]

	def seleccionar_texto(self):
		linea = 0
		for elemento in self.lista_coincide:
			for index in elemento:
				if elemento.index(index) != 0:

					index += len(self.contenido[linea]) - len(self.copia_contenido[linea])

				self.contenido[linea] = self.contenido[linea][0:index] + '|' +self.contenido[linea][index:(index + self.caracteres_patron)] + '|' +self.contenido[linea][(index + self.caracteres_patron):] 
			self.contenido_para_archivo.append(self.contenido[linea])
			linea += 1

		self.imprimir_contenido()
		self.escribir_texto()

	def escribir_texto(self):
		try:
			name_file = 'salida/'+'salida.txt'
			print('-'*45)
			print(f'Nombre del archivo: {name_file}')
			print('-'*45)
			abrir_archivo = open(name_file, 'w')
			abrir_archivo.writelines(self.contenido_para_archivo)
			abrir_archivo.close()
			print('Archivo creado con exito...')
		except:
			print('-'*45)
			print('El archivo no se pudo crear...')

	def imprimir_contenido(self):
		print('-'*45)
		print('Contenido')
		print('-'*45)
		for line in self.contenido_para_archivo:
			print(line)