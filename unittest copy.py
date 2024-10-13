import PyPDF2
from oblig1 import *

def extract_text(pdf_file: str) -> list[str]:
	pdf_text : list[str] = []

	with open(pdf_file, 'rb') as pdf:
		reader = PyPDF2.PdfReader(pdf, strict=False)
		for page in reader.pages:
			content = page.extract_text()
			pdf_text.append(content)
	
	return pdf_text

def find_dataset_indexes(text_array: list[str]) -> list[int]:
	index_array: list[int] = []
	for i, text in enumerate(text_array):
		if "Test Set " in text and not "..." in text:
			index_array.append(i)
	return index_array

def split_to_lines(text_array: list[str]) -> list[str]:
	out_array: list[str] = []
	for page in text_array:
		temp_array = page.split("\n")
		for line in temp_array:
			out_array.append(line)
	return out_array

def remove_empty_lines(text_array: list[str]) -> list[str]:
	out_array: list[str] = []
	for line in text_array:
		if line.replace(" ", "") != "":
			out_array.append(line)
	return out_array

def get_dataset_at(index: int, text_array: list[str]) -> dict[str:str]:
	hex_dict: dict[str:str] = {
		"K"	:	text_array[index+2][2:].replace(" ", ""),
		"RAND"	:	text_array[index+3][5:].replace(" ", ""),
		"SQN"	:	text_array[index+4][4:].replace(" ", ""),
		"AMF"	:	text_array[index+5][4:].replace(" ", ""),
		"OP"	:	text_array[index+6][3:].replace(" ", ""),
		"OPc"	:	text_array[index+7][4:].replace(" ", ""),
		"f1"	:	text_array[index+8][3:].replace(" ", ""),
		"f1*"	:	text_array[index+9][4:].replace(" ", ""),
		"f2"	:	text_array[index+10][3:].replace(" ", ""),
		"f3"	:	text_array[index+12][3:].replace(" ", ""),
		"f4"	:	text_array[index+13][3:].replace(" ", ""),
		"f5"	:	text_array[index+11][3:].replace(" ", ""),
		"f5*"	:	text_array[index+14][4:].replace(" ", ""),
	}
	data_dict: dict = {}
	for key in hex_dict:
		data_dict[key] = bytes.fromhex(hex_dict[key])
	return data_dict

def load_data_from_pdf(pdf_path: str) -> list[dict[str:str]]:
	text_array : list[str] = remove_empty_lines(split_to_lines(extract_text(pdf_path)))
	index_array : list[int] = find_dataset_indexes(text_array)

	out_list: list[dict[str:str]] = []
	for i in index_array:
		out_list.append(get_dataset_at(i, text_array))
	return out_list




if __name__ == '__main__':
	test_set_array : list[dict[str:str]] = load_data_from_pdf('35208-h00.pdf')
	for i, test_set in enumerate(test_set_array):
		K = test_set['K']
		RAND = test_set['RAND']
		SQN = test_set['SQN']
		AMF = test_set['AMF']
		OP = test_set['OP']

		success: bool = True
		if f1(K, RAND, SQN, AMF, OP) != test_set['f1']:
			success = False
			print(f"Test set {i} f1 failed - Got {f1(K, RAND, SQN, AMF, OP)}, but expected {test_set['f1']}")
		if f2(K, RAND, OP) != test_set['f2']:
			success = False
			print(f"Test set {i} f2 failed - Got {f2(K, RAND, OP)}, but expected {test_set['f2']}")
		if f3(K, RAND, OP) != test_set['f3']:
			success = False
			print(f"Test set {i} f3 failed - Got {f3(K, RAND, OP)}, but expected {test_set['f3']}")
		if f4(K, RAND, OP) != test_set['f4']:
			success = False
			print(f"Test set {i} f4 failed - Got {f4(K, RAND, OP)}, but expected {test_set['f4']}")
		if f5(K, RAND, OP) != test_set['f5']:
			success = False
			print(f"Test set {i} f5 failed - Got {f5(K, RAND, OP)}, but expected {test_set['f5']}")

		if success:
			print(f"Test set {i+1} passed")

