# oblig1.py
import unittest
from oblig1 import *
from enum import Enum

kats : list[dict[str:str]] = [
    {
        "K": "465b5ce8b199b49faa5f0a2ee238a6bc",
        "RAND": "23553cbe9637a89d218ae64dae47bf35",
        "SQN": "ff9bb4d0b607",
        "AMF": "b9b9",
        "OP": "cdc202d5123e20f62b6d676ac72cb318",
        "OPc": "cd63cb71954a9f4e48a5994e37a02baf",
        "f1": "4a9ffac354dfafb3",
        "f1*": "01cfaf9ec4e871e9",
        "f2": "a54211d5e3ba50bf",
        "f3": "b40ba9a3c58b2a05bbf0d987b21bf8cb",
        "f4": "f769bcd751044604127672711c6d3441",
        "f5": "aa689c648370",
        "f5*": "451e8beca43b",
    },
    {
        "K": "fec86ba6eb707ed08905757b1bb44b8f",
        "RAND": "9f7c8d021accf4db213ccff0c7f71a6a",
        "SQN": "9d0277595ffc",
        "AMF": "725c",
        "OP": "dbc59adcb6f9a0ef735477b7fadf8374",
        "OPc": "1006020f0a478bf6b699f15c062e42b3",
        "f1": "9cabc3e99baf7281",
        "f1*": "95814ba2b3044324",
        "f2": "8011c48c0c214ed2",
        "f3": "5dbdbb2954e8f3cde665b046179a5098",
        "f4": "59a92d3b476a0443487055cf88b2307b",
        "f5": "33484dc2136b",
        "f5*": "deacdd848cc6",
    },
    {
        "K": "9e5944aea94b81165c82fbf9f32db751",
        "RAND": "ce83dbc54ac0274a157c17f80d017bd6",
        "SQN": "0b604a81eca8",
        "AMF": "9e09",
        "OP": "223014c5806694c007ca1eeef57f004f",
        "OPc": "a64a507ae1a2a98bb88eb4210135dc87",
        "f1": "74a58220cba84c49",
        "f1*": "ac2cc74a96871837",
        "f2": "f365cd683cd92e96",
        "f3": "e203edb3971574f5a94b0d61b816345d",
        "f4": "0c4524adeac041c4dd830d20854fc46b",
        "f5": "f0b9c08ad02e",
        "f5*": "6085a86c6f63",
    },
    {
        "K": "4ab1deb05ca6ceb051fc98e77d026a84",
        "RAND": "74b0cd6031a1c8339b2b6ce2b8c4a186",
        "SQN": "e880a1b580b6",
        "AMF": "9f07",
        "OP": "2d16c5cd1fdf6b22383584e3bef2a8d8",
        "OPc": "dcf07cbd51855290b92a07a9891e523e",
        "f1": "49e785dd12626ef2",
        "f1*": "9e85790336bb3fa2",
        "f2": "5860fc1bce351e7e",
        "f3": "7657766b373d1c2138f307e3de9242f9",
        "f4": "1c42e960d89b8fa99f2744e0708ccb53",
        "f5": "31e11a609118",
        "f5*": "fe2555e54aa9",
    },
    {
        "K": "6c38a116ac280c454f59332ee35c8c4f",
        "RAND": "ee6466bc96202c5a557abbeff8babf63",
        "SQN": "414b98222181",
        "AMF": "4464",
        "OP": "1ba00a1a7c6700ac8c3ff3e96ad08725",
        "OPc": "3803ef5363b947c6aaa225e58fae3934",
        "f1": "078adfb488241a57",
        "f1*": "80246b8d0186bcf1",
        "f2": "16c8233f05a0ac28",
        "f3": "3f8c7587fe8e4b233af676aede30ba3b",
        "f4": "a7466cc1e6b2a1337d49d3b66e95d7b4",
        "f5": "45b0f69ab06c",
        "f5*": "1f53cd2b1113",
    },
    {
        "K": "2d609d4db0ac5bf0d2c0de267014de0d",
        "RAND": "194aa756013896b74b4a2a3b0af4539e",
        "SQN": "6bf69438c2e4",
        "AMF": "5f67",
        "OP": "460a48385427aa39264aac8efc9e73e8",
        "OPc": "c35a0ab0bcbfc9252caff15f24efbde0",
        "f1": "bd07d3003b9e5cc3",
        "f1*": "bcb6c2fcad152250",
        "f2": "8c25a16cd918a1df",
        "f3": "4cd0846020f8fa0731dd47cbdc6be411",
        "f4": "88ab80a415f15c73711254a1d388f696",
        "f5": "7e6455f34cf3",
        "f5*": "dc6dd01e8f15",
    },
    {
        "K": "a530a7fe428fad1082c45eddfce13884",
        "RAND": "3a4c2b3245c50eb5c71d08639395764d",
        "SQN": "f63f5d768784",
        "AMF": "b90e",
        "OP": "511c6c4e83e38c89b1c5d8dde62426fa",
        "OPc": "27953e49bc8af6dcc6e730eb80286be3",
        "f1": "53761fbd679b0bad",
        "f1*": "21adfd334a10e7ce",
        "f2": "a63241e1ffc3e5ab",
        "f3": "10f05bab75a99a5fbb98a9c287679c3b",
        "f4": "f9ec0865eb32f22369cade40c59c3a44",
        "f5": "88196c47986f",
        "f5*": "c987a3d23115",
    },
    {
        "K": "d9151cf04896e25830bf2e08267b8360",
        "RAND": "f761e5e93d603feb730e27556cb8a2ca",
        "SQN": "47ee0199820a",
        "AMF": "9113",
        "OP": "75fc2233a44294ee8e6de25c4353d26b",
        "OPc": "c4c93effe8a08138c203d4c27ce4e3d9",
        "f1": "66cc4be44862af1f",
        "f1*": "7a4b8d7a8753f246",
        "f2": "4a90b2171ac83a76",
        "f3": "71236b7129f9b22ab77ea7a54c96da22",
        "f4": "90527ebaa5588968db41727325a04d9e",
        "f5": "82a0f5287a71",
        "f5*": "527dbf41f35f",
    },
    {
        "K": "a0e2971b6822e8d354a18cc235624ecb",
        "RAND": "08eff828b13fdb562722c65c7f30a9b2",
        "SQN": "db5c066481e0",
        "AMF": "716b",
        "OP": "323792faca21fb4d5d6f13c145a9d2c1",
        "OPc": "82a26f22bba9e9488f949a10d98e9cc4",
        "f1": "9485fe24621cb9f6",
        "f1*": "bce325ce03e2e9b9",
        "f2": "4bc2212d8624910a",
        "f3": "08cef6d004ec61471a3c3cda048137fa",
        "f4": "ed0318ca5deb9206272f6e8fa64ba411",
        "f5": "a2f858aa9e5d",
        "f5*": "74e76fbbec38",
    },
    {
        "K": "0da6f7ba86d5eac8a19cf563ac58642d",
        "RAND": "679ac4dbacd7d233ff9d6806f4149ce3",
        "SQN": "6e2331d692ad",
        "AMF": "224a",
        "OP": "4b9a26fa459e3acbff36f4015de3bdc1",
        "OPc": "0db1071f8767562ca43a0a64c41e8d08",
        "f1": "2831d7ae9088e492",
        "f1*": "9b2e16951135d523",
        "f2": "6fc30fee6d123523",
        "f3": "69b1cae7c7429d975e245cacb05a517c",
        "f4": "74f24e8c26df58e1b38d7dcd4f1b7fbd",
        "f5": "4c539a26e1fa",
        "f5*": "07861e126928",
    },
    {
        "K": "77b45843c88e58c10d202684515ed430",
        "RAND": "4c47eb3076dc55fe5106cb2034b8cd78",
        "SQN": "fe1a8731005d",
        "AMF": "ad25",
        "OP": "bf3286c7a51409ce95724d503bfe6e70",
        "OPc": "d483afae562409a326b5bb0b20c4d762",
        "f1": "08332d7e9f484570",
        "f1*": "ed41b734489d5207",
        "f2": "aefa357beac2a87a",
        "f3": "908c43f0569cb8f74bc971e706c36c5f",
        "f4": "c251df0d888dd9329bcf46655b226e40",
        "f5": "30ff25cdadf6",
        "f5*": "e84ed0d4677e",
    },
    {
        "K": "729b17729270dd87ccdf1bfe29b4e9bb",
        "RAND": "311c4c929744d675b720f3b7e9b1cbd0",
        "SQN": "c85c4cf65916",
        "AMF": "5bb2",
        "OP": "d04c9c35bd2262fa810d2924d036fd13",
        "OPc": "228c2f2f06ac3268a9e616ee16db4ba1",
        "f1": "ff794fe2f827ebf8",
        "f1*": "24fe4dc61e874b52",
        "f2": "98dbbd099b3b408d",
        "f3": "44c0f23c5493cfd241e48f197e1d1012",
        "f4": "0c9fb81613884c2535dd0eabf3b440d8",
        "f5": "5380d158cfe3",
        "f5*": "87ac3b559fb6",
    },
    {
        "K": "d32dd23e89dc662354ca12eb79dd32fa",
        "RAND": "cf7d0ab1d94306950bf12018fbd46887",
        "SQN": "484107e56a43",
        "AMF": "b5e6",
        "OP": "fe75905b9da47d356236d0314e09c32e",
        "OPc": "d22a4b4180a5325708a5ff70d9f67ec7",
        "f1": "cf19d62b6a809866",
        "f1*": "5d269537e45e2ce6",
        "f2": "af4a411e1139f2c2",
        "f3": "5af86b80edb70df5292cc1121cbad50c",
        "f4": "7f4d6ae7440e18789a8b75ad3f42f03a",
        "f5": "217af49272ad",
        "f5*": "900e101c677e",
    },
    {
        "K": "af7c65e1927221de591187a2c5987a53",
        "RAND": "1f0f8578464fd59b64bed2d09436b57a",
        "SQN": "3d627b01418d",
        "AMF": "84f6",
        "OP": "0c7acb8d95b7d4a31c5aca6d26345a88",
        "OPc": "a4cf5c8155c08a7eff418e5443b98e55",
        "f1": "c37cae7805642032",
        "f1*": "68cd09a452d8db7c",
        "f2": "7bffa5c2f41fbc05",
        "f3": "3f8c3f3ccf7625bf77fc94bcfd22fd26",
        "f4": "abcbae8fd46115e9961a55d0da5f2078",
        "f5": "837fd7b74419",
        "f5*": "56e97a6090b1",
    },
    {
        "K": "5bd7ecd3d3127a41d12539bed4e7cf71",
        "RAND": "59b75f14251c75031d0bcbac1c2c04c7",
        "SQN": "a298ae8929dc",
        "AMF": "d056",
        "OP": "f967f76038b920a9cd25e10c08b49924",
        "OPc": "76089d3c0ff3efdc6e36721d4fceb747",
        "f1": "c3f25cd94309107e",
        "f1*": "b0c8ba343665afcc",
        "f2": "7e3f44c7591f6f45",
        "f3": "d42b2d615e49a03ac275a5aef97af892",
        "f4": "0b3f8d024fe6bfafaa982b8f82e319c2",
        "f5": "5be11495525d",
        "f5*": "4d6a34a1e4eb",
    },
    {
        "K": "6cd1c6ceb1e01e14f1b82316a90b7f3d",
        "RAND": "f69b78f300a0568bce9f0cb93c4be4c9",
        "SQN": "b4fce5feb059",
        "AMF": "e4bb",
        "OP": "078bfca9564659ecd8851e84e6c59b48",
        "OPc": "a219dc37f1dc7d66738b5843c799f206",
        "f1": "69a90869c268cb7b",
        "f1*": "2e0fdcf9fd1cfa6a",
        "f2": "70f6bdb9ad21525f",
        "f3": "6edaf99e5bd9f85d5f36d91c1272fb4b",
        "f4": "d61c853c280dd9c46f297baec386de17",
        "f5": "1c408a858b3e",
        "f5*": "aa4ae52daa30",
    },
    {
        "K": "b73a90cbcf3afb622dba83c58a8415df",
        "RAND": "b120f1c1a0102a2f507dd543de68281f",
        "SQN": "f1e8a523a36d",
        "AMF": "471b",
        "OP": "b672047e003bb952dca6cb8af0e5b779",
        "OPc": "df0c67868fa25f748b7044c6e7c245b8",
        "f1": "ebd70341bcd415b0",
        "f1*": "12359f5d82220c14",
        "f2": "479dd25c20792d63",
        "f3": "66195dbed0313274c5ca7766615fa25e",
        "f4": "66bec707eb2afc476d7408a8f2927b36",
        "f5": "aefdaa5ddd99",
        "f5*": "12ec2b87fbb1",
    },
    {
        "K": "5122250214c33e723a5dd523fc145fc0",
        "RAND": "81e92b6c0ee0e12ebceba8d92a99dfa5",
        "SQN": "16f3b3f70fc2",
        "AMF": "c3ab",
        "OP": "c9e8763286b5b9ffbdf56e1297d0887b",
        "OPc": "981d464c7c52eb6e5036234984ad0bcf",
        "f1": "2a5c23d15ee351d5",
        "f1*": "62dae3853f3af9d2",
        "f2": "28d7b0f2a2ec3de5",
        "f3": "5349fbe098649f948f5d2e973a81c00f",
        "f4": "9744871ad32bf9bbd1dd5ce54e3e2e5a",
        "f5": "ada15aeb7bb8",
        "f5*": "d461bc15475d",
    },
    {
        "K": "90dca4eda45b53cf0f12d7c9c3bc6a89",
        "RAND": "9fddc72092c6ad036b6e464789315b78",
        "SQN": "20f813bd4141",
        "AMF": "61df",
        "OP": "3ffcfe5b7b1111589920d3528e84e655",
        "OPc": "cb9cccc4b9258e6dca4760379fb82581",
        "f1": "09db94eab4f8149e",
        "f1*": "a29468aa9775b527",
        "f2": "a95100e2760952cd",
        "f3": "b5f2da03883b69f96bf52e029ed9ac45",
        "f4": "b4721368bc16ea67875c5598688bb0ef",
        "f5": "83cfd54db913",
        "f5*": "4f2039392ddc",
    },
]


class MilenageTest(unittest.TestCase):
    """Testing class made to test every helper function for milenage"""
    class helper_function(Enum):
         F1=0
         F2=1
         F3=2
         F4=3
         F5=4

    def get_compare_data(self,test_set, set:helper_function):
            K = bytes.fromhex(test_set["K"])
            RAND = bytes.fromhex(test_set["RAND"])
            SQN = bytes.fromhex(test_set["SQN"])
            AMF = bytes.fromhex(test_set["AMF"])
            OP = bytes.fromhex(test_set["OP"])
            hp = self.helper_function
        
            expected_kats = { # gets the expected data from the kats list
                hp.F1: bytes.fromhex(test_set["f1"]),
                hp.F2: bytes.fromhex(test_set["f2"]),
                hp.F3: bytes.fromhex(test_set["f3"]),
                hp.F4: bytes.fromhex(test_set["f4"]),
                hp.F5: bytes.fromhex(test_set["f5"]),
            }

            testing_kats = { # computes results from functions f1, f2, f3, f4, f5
                hp.F1: f1(K, RAND, SQN, AMF, OP),
                hp.F2: f2(K, RAND, OP),
                hp.F3: f3(K, RAND, OP),
                hp.F4: f4(K, RAND, OP),
                hp.F5: f5(K, RAND, OP),
            }
            return testing_kats[set], expected_kats[set] # returns the computed and expected results


    def test_f1(self):
        """
        Tests our f1 function against expected f1 from the kats list
        """
        for i, test_set in enumerate(kats):
            tested_result, expected_result = self.get_compare_data(test_set, self.helper_function.F1)
            with self.subTest(i=i):
                self.assertEqual(tested_result, expected_result)

    def test_f2(self):
        """
        Tests our f2 function against expected f2 from the kats list
        """
        for i, test_set in enumerate(kats):
            tested_result, expected_result = self.get_compare_data(test_set, self.helper_function.F2)
            with self.subTest(i=i):
                self.assertEqual(tested_result, expected_result)

    def test_f3(self):
        """
        Tests our f3 function against expected f3 from the kats list
        """
        for i, test_set in enumerate(kats):
            tested_result, expected_result = self.get_compare_data(test_set, self.helper_function.F3)
            with self.subTest(i=i):
                self.assertEqual(tested_result, expected_result)

    def test_f4(self):
        """
        Tests our f4 function against expected f4 from the kats list
        """
        for i, test_set in enumerate(kats):
            tested_result, expected_result = self.get_compare_data(test_set, self.helper_function.F4)
            with self.subTest(i=i):
                self.assertEqual(tested_result, expected_result)

    def test_f5(self):
        """
        Tests our f5 function against expected f5 from the kats list
        """
        for i, test_set in enumerate(kats):
            tested_result, expected_result = self.get_compare_data(test_set, self.helper_function.F5)
            with self.subTest(i=i):
                self.assertEqual(tested_result, expected_result)



         


# When this file is run, test all the KATs using the f1 -> f5 functions from the main code file.
# The kats list store all values in hex, so they need to be converted to bytes before being input
# into any function using the bytes.fromhex() method

if __name__ == '__main__':
	unittest.main()

