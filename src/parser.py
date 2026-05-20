import re

class FileTypeError(Exception):
	pass

def parse_file_path(p: str) -> (str, str, str):
	"""
	Realiza o parsing do path do arquivo. Se o formato do arquivo
	não for aceitável joga um erro.

	Args: 
	- p (str): Caminho do arquivo

	Return:
	- (str, str, str): Ano, nome do álbum e nome do arquivo
	"""
	year = None
	album = None
	track = None
	file_type = None

	contents = p.split('/')
	file_contents = contents[-1]

	file_type = file_contents.split('.')[-1]
	track 	  = file_contents.split('.')[0].rstrip()

	if file_type != "flac":
		raise FileTypeError("Invalid file type. Acceptable files: .flac")

	if track == '':
		track = None

	album = re.split(r'\[|\]', contents[-2])

	if len(album) != 1:
		year  = album[1]
		album = album[2][1:]

		try:
			_year = int(year)

			if _year > 9999:
				year = None
		except ValueError:
			year = None
	else:
		album = album[0]

	return year, album, track