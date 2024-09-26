def load_data(set_number: int = 1) -> dict[str, bytes]:
	'''
	Loads testdata into a dictionary, contains six sets of test data
	---
	set_number: which of the predefined datasets to use. 
	Value between 1 and 5, anything else defaults to dataset 6
	---
	returns: dict{str:bytes}
	'''
	hex_dict: dict
	match set_number:
		case 1:
			hex_dict : dict = {
				"K"		:"465b5ce8 b199b49f aa5f0a2e e238a6bc",
				"RAND"	:"23553cbe 9637a89d 218ae64d ae47bf35",
				"SQN"	:"ff9bb4d0 b607",
				"AMF"	:"b9b9",
				"OP"	:"cdc202d5 123e20f6 2b6d676a c72cb318",
				"OPc"	:"cd63cb71 954a9f4e 48a5994e 37a02baf",
				"f1"	:"4a9ffac3 54dfafb3",
				"f1*"	:"01cfaf9e c4e871e9",
				"f2"	:"a54211d5 e3ba50bf",
				"f3"	:"b40ba9a3 c58b2a05 bbf0d987 b21bf8cb",
				"f4"	:"f769bcd7 51044604 12767271 1c6d3441",
				"f5"	:"aa689c64 8370",
				"f5*"	:"451e8bec a43b"
			}
		case 2:
			hex_dict : dict = {
				"K"		:"465b5ce8 b199b49f aa5f0a2e e238a6bc",
				"RAND"	:"23553cbe 9637a89d 218ae64d ae47bf35",
				"SQN"	:"ff9bb4d0 b607",
				"AMF"	:"b9b9",
				"OP"	:"cdc202d5 123e20f6 2b6d676a c72cb318",
				"OPc"	:"cd63cb71 954a9f4e 48a5994e 37a02baf",
				"f1"	:"4a9ffac3 54dfafb3",
				"f1*"	:"01cfaf9e c4e871e9",
				"f2"	:"a54211d5 e3ba50bf",
				"f3"	:"b40ba9a3 c58b2a05 bbf0d987 b21bf8cb",
				"f4"	:"f769bcd7 51044604 12767271 1c6d3441",
				"f5"	:"aa689c64 8370",
				"f5*"	:"451e8bec a43b"
			}
		case 3:
			hex_dict : dict = {
				"K"		:"fec86ba6 eb707ed0 8905757b 1bb44b8f",
				"RAND"	:"9f7c8d02 1accf4db 213ccff0 c7f71a6a",
				"SQN"	:"9d027759 5ffc",
				"AMF"	:"725c",
				"OP"	:"dbc59adc b6f9a0ef 735477b7 fadf8374",
				"OPc"	:"1006020f 0a478bf6 b699f15c 062e42b3",
				"f1"	:"9cabc3e9 9baf7281",
				"f1*"	:"95814ba2 b3044324",
				"f2"	:"8011c48c 0c214ed2",
				"f3"	:"5dbdbb29 54e8f3cd e665b046 179a5098",
				"f4"	:"59a92d3b 476a0443 487055cf 88b2307b",
				"f5"	:"33484dc2 136b",
				"f5*"	:"deacdd84 8cc6"
			}
		case 4:
			hex_dict : dict = {
				"K"		:"9e5944ae a94b8116 5c82fbf9 f32db751",
				"RAND"	:"ce83dbc5 4ac0274a 157c17f8 0d017bd6",
				"SQN"	:"0b604a81 eca8",
				"AMF"	:"9e09",
				"OP"	:"223014c5 806694c0 07ca1eee f57f004f",
				"OPc"	:"a64a507a e1a2a98b b88eb421 0135dc87",
				"f1"	:"74a58220 cba84c49",
				"f1*"	:"ac2cc74a 96871837",
				"f2"	:"f365cd68 3cd92e96",
				"f3"	:"e203edb3 971574f5 a94b0d61 b816345d",
				"f4"	:"0c4524ad eac041c4 dd830d20 854fc46b",
				"f5"	:"f0b9c08a d02e",
				"f5*"	:"6085a86c 6f63"
			}
		case 5:
			hex_dict : dict = {
				"K"		:"4ab1deb0 5ca6ceb0 51fc98e7 7d026a84",
				"RAND"	:"74b0cd60 31a1c833 9b2b6ce2 b8c4a186",
				"SQN"	:"e880a1b5 80b6",
				"AMF"	:"9f07",
				"OP"	:"2d16c5cd 1fdf6b22 383584e3 bef2a8d8",
				"OPc"	:"dcf07cbd 51855290 b92a07a9 891e523e",
				"f1"	:"49e785dd 12626ef2",
				"f1*"	:"9e857903 36bb3fa2",
				"f2"	:"5860fc1b ce351e7e",
				"f3"	:"7657766b 373d1c21 38f307e3 de9242f9",
				"f4"	:"1c42e960 d89b8fa9 9f2744e0 708ccb53",
				"f5"	:"31e11a60 9118",
				"f5*"	:"fe2555e5 4aa9"
			}
		case _:
			hex_dict : dict = {
				"K"		:"6c38a116 ac280c45 4f59332e e35c8c4f",
				"RAND"	:"ee6466bc 96202c5a 557abbef f8babf63",
				"SQN"	:"414b9822 2181",
				"AMF"	:"4464",
				"OP"	:"1ba00a1a 7c6700ac 8c3ff3e9 6ad08725",
				"OPc"	:"3803ef53 63b947c6 aaa225e5 8fae3934",
				"f1"	:"078adfb4 88241a57",
				"f1*"	:"80246b8d 0186bcf1",
				"f2"	:"16c8233f 05a0ac28",
				"f3"	:"3f8c7587 fe8e4b23 3af676ae de30ba3b",
				"f4"	:"a7466cc1 e6b2a133 7d49d3b6 6e95d7b4",
				"f5"	:"45b0f69a b06c",
				"f5*"	:"1f53cd2b 1113"
			}
	
	data_dict: dict = {}
	for key in hex_dict:
		data_dict[key] = bytes.fromhex(hex_dict[key])
	return data_dict


if __name__ == "__main__":
	print(load_data(1))