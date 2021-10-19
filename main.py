from readfile import ReadFile
from boyer_moore import buscar
from writefile import WriteFile

if __name__ == '__main__':
	lineas_indice = []

	archivo = ReadFile(nombre_archivo='text.txt')
	archivo.leer_txt_lineas()

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


