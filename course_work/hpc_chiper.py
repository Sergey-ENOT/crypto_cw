import os


class HPCMedium:
    def __init__(self, key_str, path_open, path_write):
        self.key_str = key_str
        self.key_256 = []
        self.list_keys = []
        self.fb_text = ""
        self.result_text = ""
        self.left_64 = ""
        self.right_64 = ""
        self.two_in_64 = 2**64
        self.pi19 = 31415922653589793238
        self.e19 = 2718281828459045235
        self.r220 = 14142135623730950488
        self.c1 = 64 + self.pi19
        self.nc = 3
        self.hex_key = bytes(key_str, "utf-8").hex()
        self.l_b = bin(int(self.hex_key, 16))[2:]
        self.path_open = path_open
        self.path_write = path_write
        self.first_write = True
        self.t_matrix = [
                    [1, 7, 14, 13, 0, 5, 8, 3, 4, 15, 10, 6, 9, 12, 11, 2],
                    [8, 14, 2, 5, 6, 9, 1, 12, 15, 4, 11, 0, 13, 10, 3, 7],
                    [5, 13, 15, 6, 9, 2, 12, 10, 11, 7, 8, 1, 4, 3, 14, 0],
                    [7, 15, 5, 10, 8, 1, 6, 13, 0, 9, 3, 14, 11, 4, 2, 12],
                    [12, 8, 2, 1, 13, 4, 15, 6, 7, 0, 10, 5, 3, 14, 9, 11],
                    [11, 3, 5, 8, 2, 15, 10, 13, 14, 1, 7, 4, 12, 9, 6, 0],
                    [6, 8, 2, 3, 9, 10, 5, 12, 1, 14, 4, 7, 11, 13, 0, 15],
                    [12, 4, 6, 2, 10, 5, 11, 9, 14, 8, 13, 7, 0, 3, 15, 1]
                ]

    def expand_key(self):
        self.list_keys[0] = self.pi19 + self.nc
        self.list_keys[1] = self.e19 + len(self.l_b)
        self.list_keys[2] = self.r220

    def read_file(self):
        if os.path.splitext(self.path_open)[1] == ".txt":
            with open(self.path_open, 'r') as f:
                self.fb_text = f.read()
        else:
            with open(self.path_open, 'rb') as f:
                self.fb_text = f.read().hex()

    def mod_2_in_32(self, value_1, value_2):
        return hex((int(value_1, 16) + int(value_2, 16)) % self.two_in_32)[2:]

    def transposition(self, value):
        res_str = ""
        temp_value = ""
        if len(value) != 8:
            for i in range(8-len(value)):
                temp_value += "0"
            temp_value += value
        else:
            temp_value = value
        for i in range(len(temp_value)):
            res_str += hex(self.t_matrix[i][int(temp_value[i], 16)])[2:]
        return res_str

    def left_shift(self, value, count):
        bin_value = bin(int(value, 16))[2:].zfill(32)
        list_value = list(bin_value)
        for i in range(count):
            el_0 = list_value[0]
            list_value.pop(0)
            list_value.append(el_0)
        return hex(int("".join(list_value), 2))[2:]

    def xor_operation(self, value_1, value_2):
        return hex(int(value_1, 16) ^ int(value_2, 16))[2:]

    def function_g(self, a_1, a_0, key_i):
        res_mod = self.mod_2_in_32(a_0, key_i)
        res_t = self.transposition(res_mod)
        res_l_s = self.left_shift(res_t, 11)
        res_xor = self.xor_operation(a_1, res_l_s)
        return res_xor

    def write_file(self, value):
        if self.first_write:
            mode = 'wb'
            self.first_write = False
        else:
            mode = 'ab'
        with open(self.path_write, mode) as f:
            f.write(value)

    def complete_to_8_block(self, value_h):
        temp_v = ""
        if len(value_h) < 8:
            for i in range(8-len(value_h)):
                temp_v += "0"
        temp_v += value_h
        return temp_v

    def clear_last_bytes(self, value_h):
        for i in range(-1, -len(value_h), -1):
            if value_h[i] == "0":
                pass
            elif value_h[i] != "0":
                return value_h[0:i+1]

    def encrypt(self):
        self.expand_key()
        self.read_file()
        # f_text = ""
        '''creates two blocks with 32 bits'''
        for i in range(0, len(self.fb_text), 16):
            self.left_32 = self.fb_text[i:i + 8]
            self.right_32 = self.fb_text[i + 8:i + 16]

            for j in range(0, 31):
                new_a_0 = self.function_g(self.left_32, self.right_32, self.list_keys[j])
                self.left_32 = self.right_32
                self.right_32 = new_a_0
            new_a_1 = self.function_g(self.left_32, self.right_32, self.list_keys[31])
            result_f_g = self.complete_to_8_block(new_a_1) + self.complete_to_8_block(self.right_32)
            # f_text += result_f_g
            self.write_file(bytes.fromhex(result_f_g))
        # print(bytes.fromhex(f_text))
        self.first_write = True

    def decrypt(self):
        self.expand_key()
        self.read_file()
        # f_text = ""
        '''creates two blocks with 32 bits'''
        for i in range(0, len(self.fb_text), 16):
            self.left_32 = self.fb_text[i:i+8]
            self.right_32 = self.fb_text[i+8:i+16]

            for j in range(31, 0, -1):
                new_a_0 = self.function_g(self.left_32, self.right_32, self.list_keys[j])
                self.left_32 = self.right_32
                self.right_32 = new_a_0

            new_a_1 = self.function_g(self.left_32, self.right_32, self.list_keys[0])
            result_f_g = self.complete_to_8_block(new_a_1) + self.complete_to_8_block(self.right_32)
            # f_text += result_f_g
            if (len(self.fb_text) - i) < 17:
                result_f_g = self.clear_last_bytes(result_f_g)
            self.write_file(bytes.fromhex(result_f_g))
        # print(bytes.fromhex(f_text))
        self.first_write = True
