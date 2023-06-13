""" Replacement tables """
S7 = (
    54, 50, 62, 56, 22, 34, 94, 96, 38, 6, 63, 93, 2, 18, 123, 33,
    55, 113, 39, 114, 21, 67, 65, 12, 47, 73, 46, 27, 25, 111, 124, 81,
    53, 9, 121, 79, 52, 60, 58, 48, 101, 127, 40, 120, 104, 70, 71, 43,
    20, 122, 72, 61, 23, 109, 13, 100, 77, 1, 16, 7, 82, 10, 105, 98,
    117, 116, 76, 11, 89, 106, 0, 125, 118, 99, 86, 69, 30, 57, 126, 87,
    112, 51, 17, 5, 95, 14, 90, 84, 91, 8, 35, 103, 32, 97, 28, 66,
    102, 31, 26, 45, 75, 4, 85, 92, 37, 74, 80, 49, 68, 29, 115, 44,
    64, 107, 108, 24, 110, 83, 36, 78, 42, 19, 15, 41, 88, 119, 59, 3,
)
S9 = (
    167, 239, 161, 379, 391, 334, 9, 338, 38, 226, 48, 358, 452, 385, 90, 397,
    183, 253, 147, 331, 415, 340, 51, 362, 306, 500, 262, 82, 216, 159, 356, 177,
    175, 241, 489, 37, 206, 17, 0, 333, 44, 254, 378, 58, 143, 220, 81, 400,
    95, 3, 315, 245, 54, 235, 218, 405, 472, 264, 172, 494, 371, 290, 399, 76,
    165, 197, 395, 121, 257, 480, 423, 212, 240, 28, 462, 176, 406, 507, 288, 223,
    501, 407, 249, 265, 89, 186, 221, 428, 164, 74, 440, 196, 458, 421, 350, 163,
    232, 158, 134, 354, 13, 250, 491, 142, 191, 69, 193, 425, 152, 227, 366, 135,
    344, 300, 276, 242, 437, 320, 113, 278, 11, 243, 87, 317, 36, 93, 496, 27,
    487, 446, 482, 41, 68, 156, 457, 131, 326, 403, 339, 20, 39, 115, 442, 124,
    475, 384, 508, 53, 112, 170, 479, 151, 126, 169, 73, 268, 279, 321, 168, 364,
    363, 292, 46, 499, 393, 327, 324, 24, 456, 267, 157, 460, 488, 426, 309, 229,
    439, 506, 208, 271, 349, 401, 434, 236, 16, 209, 359, 52, 56, 120, 199, 277,
    465, 416, 252, 287, 246, 6, 83, 305, 420, 345, 153, 502, 65, 61, 244, 282,
    173, 222, 418, 67, 386, 368, 261, 101, 476, 291, 195, 430, 49, 79, 166, 330,
    280, 383, 373, 128, 382, 408, 155, 495, 367, 388, 274, 107, 459, 417, 62, 454,
    132, 225, 203, 316, 234, 14, 301, 91, 503, 286, 424, 211, 347, 307, 140, 374,
    35, 103, 125, 427, 19, 214, 453, 146, 498, 314, 444, 230, 256, 329, 198, 285,
    50, 116, 78, 410, 10, 205, 510, 171, 231, 45, 139, 467, 29, 86, 505, 32,
    72, 26, 342, 150, 313, 490, 431, 238, 411, 325, 149, 473, 40, 119, 174, 355,
    185, 233, 389, 71, 448, 273, 372, 55, 110, 178, 322, 12, 469, 392, 369, 190,
    1, 109, 375, 137, 181, 88, 75, 308, 260, 484, 98, 272, 370, 275, 412, 111,
    336, 318, 4, 504, 492, 259, 304, 77, 337, 435, 21, 357, 303, 332, 483, 18,
    47, 85, 25, 497, 474, 289, 100, 269, 296, 478, 270, 106, 31, 104, 433, 84,
    414, 486, 394, 96, 99, 154, 511, 148, 413, 361, 409, 255, 162, 215, 302, 201,
    266, 351, 343, 144, 441, 365, 108, 298, 251, 34, 182, 509, 138, 210, 335, 133,
    311, 352, 328, 141, 396, 346, 123, 319, 450, 281, 429, 228, 443, 481, 92, 404,
    485, 422, 248, 297, 23, 213, 130, 466, 22, 217, 283, 70, 294, 360, 419, 127,
    312, 377, 7, 468, 194, 2, 117, 295, 463, 258, 224, 447, 247, 187, 80, 398,
    284, 353, 105, 390, 299, 471, 470, 184, 57, 200, 348, 63, 204, 188, 33, 451,
    97, 30, 310, 219, 94, 160, 129, 493, 64, 179, 263, 102, 189, 207, 114, 402,
    438, 477, 387, 122, 192, 42, 381, 5, 145, 118, 180, 449, 293, 323, 136, 380,
    43, 66, 60, 455, 341, 445, 202, 432, 8, 237, 15, 376, 436, 464, 59, 461,
)

""" Class """


class Kasumi:
    def __init__(self):
        self.list_keys = []
        self.list_const_keys = []
        self.left = None
        self.right = None
        self.constant = ("0123", "4567", "89AB", "CDEF", "FEDC", "BA98", "7654", "3210")
        self.key_KL1 = ""
        self.key_KL2 = ""
        self.key_KO1 = ""
        self.key_KO2 = ""
        self.key_KO3 = ""
        self.key_KI1 = ""
        self.key_KI2 = ""
        self.key_KI3 = ""
        self.base_vi = "1234abcd5678ef90"
        self.new_vi = ""
        self.last_vi = ""
        self.added_null = 0

    @staticmethod
    def complete_str(in_str, req_len):
        fill_str = ""
        if len(in_str) < req_len:
            for i in range(req_len - len(in_str)):
                fill_str += "0"
        return fill_str + in_str

    @staticmethod
    def complete_res_hex(in_str, req_len):
        fill_str = ""
        str_in_hex = hex(int(in_str, 2))[2:]
        len_hex = len(str_in_hex)
        if len_hex < req_len:
            for i in range(req_len - len_hex):
                fill_str += "0"
        return "0x" + fill_str + str_in_hex

    @staticmethod
    def xor_hex(value_1, value_2):
        return hex(int(value_1, 16) ^ int(value_2, 16))[2:]

    @staticmethod
    def xor_bitstr(value_1, value_2):
        return bin(int(value_1, 2) ^ int(value_2, 2))[2:]

    @staticmethod
    def left_shift(value, count, is_int=False):
        if is_int:
            bin_value = bin(value)[2:]
        else:
            bin_value = bin(int(value, 16))[2:]

        list_value = list(bin_value)
        for i in range(count):
            el_0 = list_value[0]
            list_value.pop(0)
            list_value.append(el_0)

        if is_int:
            res_str = "".join(list_value)
        else:
            res_str = hex(int("".join(list_value), 2))[2:]
        return res_str

    def generate_round_keys(self, number_round):
        self.key_KL1 = self.left_shift(self.list_keys[number_round], 1)
        self.key_KL2 = self.list_const_keys[(number_round + 2) % 8]
        self.key_KO1 = self.left_shift(self.list_keys[(number_round + 1) % 8], 5)
        self.key_KO2 = self.left_shift(self.list_keys[(number_round + 5) % 8], 8)
        self.key_KO3 = self.left_shift(self.list_keys[(number_round + 6) % 8], 13)
        self.key_KI1 = self.list_const_keys[(number_round + 4) % 8]
        self.key_KI2 = self.list_const_keys[(number_round + 3) % 8]
        self.key_KI3 = self.list_const_keys[(number_round + 7) % 8]

    def set_key(self, user_key):
        self.list_keys.clear()
        self.list_const_keys.clear()
        print("start_set_key")
        if user_key[:2] == "0x":
            user_key = user_key[2:]
        if len(user_key) < 32:
            user_key = self.complete_str(user_key, 32)
        elif len(user_key) > 32:
            user_key = user_key[:32]
        print("user_key:", user_key)
        for i in range(0, len(user_key), 4):
            cur_key = user_key[i:i+4]
            self.list_keys.append(cur_key)
            self.list_const_keys.append(self.xor_hex(cur_key, self.constant[i // 4]))
        print("key_ready")

    def func_fl(self, left_block):
        left_block = self.complete_str(left_block, 32)
        left_16 = left_block[:16]
        right_16 = left_block[16:]
        new_right_16 = self.xor_bitstr(right_16, self.left_shift(int(left_16, 2) & int(self.key_KL1, 16), 1, True))
        new_left_16 = self.xor_bitstr(left_16, self.left_shift(int(new_right_16, 2) | int(self.key_KL2, 16), 1, True))
        return self.complete_str(new_left_16, 16) + self.complete_str(new_right_16, 16)

    def func_fo(self, in_text):
        in_text = self.complete_str(in_text, 32)
        in_left = in_text[:16]
        in_right = in_text[16:]

        """ round 1"""
        left_1 = in_right
        right_1 = self.xor_bitstr(self.func_fi(int(in_left, 2) ^ int(self.key_KO1, 16)), in_right)

        """ round 2"""
        in_left = right_1
        in_right = self.xor_bitstr(self.func_fi(int(left_1, 2) ^ int(self.key_KO2, 16)), right_1)

        """ round 3 """
        left_1 = in_right
        right_1 = self.xor_bitstr(self.func_fi(int(in_left, 2) ^ int(self.key_KO3, 16)), in_right)

        return self.complete_str(left_1, 16) + self.complete_str(right_1, 16)

    def func_fi(self, in_text):
        bin_text = self.complete_str(bin(in_text)[2:], 16)
        in_left = bin_text[:9]
        in_right = bin_text[9:]

        r_key1 = int(bin_text[:7], 2)
        r_key2 = int(bin_text[7:], 2)

        out_left_1 = int(in_right, 2)
        out_right_1 = S9[int(in_left, 2)] ^ int(in_right, 2)

        in_left = out_right_1 ^ r_key2
        in_right = (S7[out_left_1] ^ (out_right_1 & 0b1111111)) ^ r_key1

        out_left_1 = in_right
        out_right_1 = S9[in_left] ^ in_right

        in_right = out_right_1
        in_left = S7[out_left_1] ^ (out_right_1 & 0b1111111)

        return self.complete_str(bin(in_left)[2:], 9) + self.complete_str(bin(in_right)[2:], 7)

    def last_block(self, in_plaintext, mode):
        new_part = ""
        if mode == "encrypt":
            self.added_null = 16 - len(in_plaintext)
            for i in range(self.added_null):
                new_part += "0"
            return new_part

    def encrypt_file(self, path_input, path_output, mode_ecb=False):
        try:
            with open(path_input, "rb") as f:
                plaintext = f.read().hex()
                res_file_enc = self.encrypt(plaintext, mode_ecb)[2:]
                try:
                    with open(path_output, "wb") as g:
                        print(len(res_file_enc))
                        g.write(bytes.fromhex(res_file_enc))
                except ValueError as err:
                    try:
                        with open(path_output, "wb") as g:
                            g.write(bytes.fromhex(self.complete_str(res_file_enc, len(res_file_enc)+1)))
                    except ValueError as error:
                        print(error)
                        return error
                    return err
            return "Операция зашифрования успешно выполнена"
        except FileNotFoundError:
            return "Файл для считывания не найден"

    def encrypt(self, plaintext, mode_ecb=False):
        print("plain_text:", plaintext)
        if plaintext[:2] == "0x":
            plaintext = plaintext[2:]
        res_str = ""
        self.new_vi = self.base_vi

        for i in range(0, len(plaintext), 16):
            if i + 16 >= len(plaintext):
                new_part = self.last_block(plaintext[i:], "encrypt")
                plaintext += new_part
                print("added_part", plaintext)
            if mode_ecb:
                ecb_plaintext = self.complete_str(self.xor_hex(plaintext[i:i+16], self.new_vi), 16)
                self.left = bin(int(ecb_plaintext[:8], 16))[2:]
                self.right = bin(int(ecb_plaintext[8:], 16))[2:]
            else:
                self.left = bin(int(plaintext[i:i+8], 16))[2:]
                self.right = bin(int(plaintext[i+8:i+16], 16))[2:]
            self.left = self.complete_str(self.left, 32)
            self.right = self.complete_str(self.right, 32)
            res_enc = self.encrypt_block()
            res_str += self.complete_str(res_enc, 64)
            if mode_ecb:
                self.new_vi = hex(int(res_enc, 2))[2:]
        final_block = "1" * 32 + self.complete_str(bin(self.added_null)[2:], 32)
        res_str += final_block
        print("final_res", hex(int(final_block, 2)), len(res_str))
        return self.complete_res_hex(res_str, len(plaintext))

    def encrypt_block(self):
        for j in range(8):
            self.generate_round_keys(j)
            if (j % 2) == 0:
                temp = self.left
                res_fl = self.func_fl(self.left)
                res_fo = self.func_fo(res_fl)
                self.left = self.xor_bitstr(res_fo, self.right)
                self.right = temp
            else:
                temp = self.left
                res_fo = self.func_fo(self.left)
                res_fl = self.func_fl(res_fo)
                self.left = self.xor_bitstr(res_fl, self.right)
                self.right = temp

        return self.complete_str(self.left, 32) + self.complete_str(self.right, 32)

    def decrypt_file(self, path_input, path_output, mode_ecb=False):
        try:
            with open(path_input, "rb") as f:
                plaintext = f.read().hex()
                res_file_dec = self.decrypt(plaintext, mode_ecb)[2:]
                try:
                    with open(path_output, "wb") as g:
                        g.write(bytes.fromhex(res_file_dec))
                except Exception as err:
                    return err
            return "Операция расшифрования успешно выполнена"
        except FileNotFoundError:
            return "Файл для считывания не найден"

    def decrypt(self, chipertext, mode_ecb=False):
        if chipertext[:2] == "0x":
            chipertext = chipertext[2:]
        res_str = ""
        self.last_vi = self.base_vi
        print("chiper_text", chipertext[len(chipertext)-16:len(chipertext)-1])
        if chipertext[len(chipertext)-16:len(chipertext)-1] == "ffffffff0000000":
            self.added_null = int(chipertext[-1], 16)
            print("успех")
        else:
            print("error_input")
            raise ValueError

        for i in range(0, len(chipertext)-16, 16):
            print(chipertext[:len(chipertext)-16])
            if mode_ecb:
                self.new_vi = chipertext[i:i+16]
            self.left = bin(int(chipertext[i:i+8], 16))[2:]
            self.right = bin(int(chipertext[i+8:i+16], 16))[2:]
            res_dec = self.decrypt_block()

            if mode_ecb:
                res_str += self.complete_str(self.xor_bitstr(bin(int(self.last_vi, 16)), res_dec), 64)
                self.last_vi = self.new_vi
            else:
                res_str += self.complete_str(res_dec, 64)
        print("success_dec")
        return self.complete_res_hex(res_str, len(chipertext) - 16)[:len(chipertext)-14-self.added_null]

    def decrypt_block(self):
        for j in range(7, -1, -1):
            self.generate_round_keys(j)
            if (j % 2) == 0:
                temp = self.right
                res_fl = self.func_fl(self.right)
                res_fo = self.func_fo(res_fl)
                self.right = self.xor_bitstr(res_fo, self.left)
                self.left = temp
            else:
                temp = self.right
                res_fo = self.func_fo(self.right)
                res_fl = self.func_fl(res_fo)
                self.right = self.xor_bitstr(res_fl, self.left)
                self.left = temp
        return self.complete_str(self.left, 32) + self.complete_str(self.right, 32)


""" TESTS """
# # u_key = "0x9900aabbccddeeff1122334455667788"
# u_key = "12356"
# # u_text = "0x0123456789abcdef1234567890abcdeffedcba09876543211"
# u_text = "привет мир".encode("utf-8").hex()
# # u_text = "123".encode("utf-8").hex()
#
# test_kasumi = Kasumi()
# test_kasumi.set_key(u_key)
#
# print("Original__text:", u_text)
# res_enc = test_kasumi.encrypt(u_text)
# print("res_encryption:", res_enc)
# #
# # # test_enc = res_enc
# # # for i in range(99):
# # #     test_enc = test_kasumi.encrypt(test_enc, True)
# # # for i in range(99):
# # #     test_enc = test_kasumi.decrypt(test_enc, True)
# #
# test_kasumi.set_key("12334")
# res_dec = test_kasumi.decrypt(res_enc)
# print("res_decryption:", res_dec)
# print(bytes.fromhex(res_dec[2:]).decode("utf-8"))
# # 0x3236fdc67fb023eb
# if u_text == res_dec:
#     print("\n", "WE ARE THE CHAMPIONS!!!")

# in_path = "test_work/7744.jpg"
# out_path = "test_work/7744.jpg.kasumi"
# dec_path = "test_work/7744_decrypted.png"

# in_path = "test_work/Разумов.С.Ю.БИ20_НИР.docx"
# out_path = "test_work/Разумов.С.Ю.БИ20_НИР.docx.kasumi"
# dec_path = "test_work/Разумов.С.Ю.БИ20_НИР_decrypted.docx"

# in_path = "test_work/kandinsky-cat-samurai.png"
# out_path = "test_work/kandinsky-cat-samurai.png.kasumi"
# dec_path = "test_work/kandinsky-cat-samurai_decrypted.png"

# in_path = "test_work/aorus 4k_black.jpg"
# out_path = "test_work/aorus 4k_black.jpg.kasumi"
# dec_path = "test_work/aorus 4k_black_decrypted.jpg"

# in_path = "apples.jpg"
# out_path = "apples.jpg.kasumi"
# dec_path = "apples_decrypted.png"
#
# res_enc_file = test_kasumi.encrypt_file(in_path, out_path, True)
# print(res_enc_file)
#
# res_dec_file = test_kasumi.decrypt_file(out_path, dec_path, True)
# print(res_dec_file)
