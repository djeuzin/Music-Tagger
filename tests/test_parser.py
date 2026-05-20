from src.parser import parse_file_path, FileTypeError

def test_get_year_from_path():
	year, _, _ = parse_file_path(".../.../something/[2015] Manual/Benzin .flac")
	assert year == str(2015)

def test_get_album_from_path():
	_, album, _ = parse_file_path(".../.../something/[2015] Manual/Benzin .flac")
	assert album == "Manual"

def test_get_track_from_path():
	_, _, track = parse_file_path(".../.../something/[2015] Manual/Benzin .flac")
	assert track == "Benzin"

def test_no_year_in_path():
	year, _, _ = parse_file_path(".../.../something/Coisas Estranhas/Luminária de Lava .flac")
	assert year is None

def test_no_album_name():
	_, album, _ = parse_file_path(".../.../something/Benzin .flac")
	assert album == "something"

def test_no_track_name():
	_, _, track = parse_file_path(".../.../something/[2015] Manual/ .flac")
	assert track is None

def test_special_character_album():
	_, album, _ = parse_file_path(".../.../something/[2017] Lá vem a morte/foimal .flac")
	assert album == "Lá vem a morte"

def test_special_character_track():
	_, _, track = parse_file_path(".../.../something/[2015] Manual/Sei lá .flac")
	assert track == "Sei lá"

def test_invalid_year_number():
	year, _, _ = parse_file_path(".../.../something/[20015] Manual/Benzin .flac")
	assert year is None

def test_invalid_year_not_number():
	year, _, _ = parse_file_path(".../.../something/[20I5] Manual/Benzin .flac")
	assert year is None

def test_invalid_file_type():
	with pytest.raises(FileTypeError, match="Invalid file type. Acceptable files: .flac"):
		parse_file_path(".../.../something/[20I5] Manual/Benzin .jpeg")

def test_invalid_file_type_2():
	with pytest.raises(FileTypeError, match="Invalid file type. Acceptable files: .flac"):
		parse_file_path(".../.../something/[20I5] Manual/Benzin .fla")
