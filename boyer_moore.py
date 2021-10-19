NO_OF_CHARS = 256

def bad_char_heuristic(cadena, tamaño):
	'''
	Esta función retorna el bad char generado 
	preprocesando el patrón
	'''
	bad_char = [-1] * NO_OF_CHARS
	for i in range(tamaño):
		bad_char[ord(cadena[i])] = i;
	return bad_char
 
def buscar(contenido, patron):
	'''
	Esta función implementa el algoritmo
	de Boyer Moore, teniendo en cuenta el
	bad char heuristic
	'''
	caracteres_contenido = len(contenido)
	caracteres_patron = len(patron)
	bad_char = bad_char_heuristic(patron, caracteres_patron)
	inicio = 0
	lista_indices = []

	while(inicio <= caracteres_contenido - caracteres_patron): 
		fin = caracteres_patron - 1
		while fin >= 0 and patron[fin] == contenido[inicio+fin]:
			fin -= 1
		if fin < 0:
			print(f'Patron encontrado en {inicio}')
			lista_indices.append(inicio)
			inicio += (caracteres_patron-bad_char[ord(contenido[inicio+caracteres_patron])] if inicio + caracteres_patron < caracteres_contenido else 1)
		else:
			inicio += max(1, fin - bad_char[ord(contenido[inicio+fin])])

	return lista_indices
 	

