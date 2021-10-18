from readfile import ReadFile

if __name__ == '__main__':
	file = ReadFile(file_name='text.txt')
	file.read_txt()
	file.print_lines()
	print(file.__dict__)