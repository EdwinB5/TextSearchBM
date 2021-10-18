from readfile import ReadFile

if __name__ == '__main__':
	file = ReadFile(file_name='text.txt')
	file.read_txt_lines()
	file.print_lines()

	print(file.get_content())