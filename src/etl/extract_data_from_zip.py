import zipfile


def extract_data_from_zip(path_to_zip_file,directory_to_extract_to):
	zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
	zip_ref.extractall(directory_to_extract_to)
	zip_ref.close()
	print('zip file extracted')