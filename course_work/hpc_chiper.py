import os
import math


class HPCMedium:
    def __init__(self, key_str, spice_str, path_open="./", path_write="./"):
        self.key_str = key_str
        self.list_keys = []
        self.arr_key = []
        self.spice_str = spice_str
        self.spice_list = []
        self.fb_text = ""
        self.result_text = ""
        self.s_0 = ""
        self.s_1 = ""
        self.two_in_64 = 2**64
        self.pi19 = 3141592653589793238
        self.e19 = 2718281828459045235
        self.r220 = 14142135623730950488
        self.c1 = hex(128 + self.pi19)
        self.nc = 3
        self.hex_key = bytes(key_str, "utf-8").hex()
        self.l_b = len(bin(int(self.hex_key, 16))[2:])
        self.path_open = path_open
        self.path_write = path_write
        self.first_write = True
        self.expand_key()
        self.split_spice()

    def expand_key(self):
        self.list_keys.append(hex(self.pi19 + self.nc)[2:])
        self.list_keys.append(hex(self.e19 + self.l_b)[2:])
        self.list_keys.append(self.left_shift(self.r220, self.nc))
         # for i in range(3):
            # print(self.list_keys[i], len(self.list_keys[i]))
        for i in range(3, 256):
            # print("------------", i, "---------------")
            # print("list:", self.list_keys[i-3])
            res_r_s = self.right_shift(self.list_keys[i-3], 23)
            # print("res_r_s:", res_r_s)
            res_l_s = self.left_shift(self.list_keys[i-3], 41)
            # print("res_l_s", res_l_s)
            res_xor = self.xor_operation(self.xor_operation(self.list_keys[i-2], res_r_s), res_l_s)
            res_mod = self.plus_mod_64(res_xor)
            self.list_keys.append(self.complete_to_64_bit(self.add_hex(self.list_keys[i-1], hex(res_mod))))
        # for i in range(256):
        #     print(i+1, self.list_keys[i])
        self.xor_key()
        # for i in range(30):
        #     self.list_keys.append(self.list_keys[i])

    def split_spice(self):
        for i in range(0, len(self.spice_str), 16):
            self.spice_list.append(self.spice_str[i:i+16])
        # print(self.spice_list)

    def read_file(self):
        if os.path.splitext(self.path_open)[1] == ".txt":
            with open(self.path_open, 'r') as f:
                self.fb_text = f.read()
        else:
            with open(self.path_open, 'rb') as f:
                self.fb_text = f.read().hex()

    def mod(self, value):
        return value & 0xFFFFFFFFFFFFFFFF

    def plus_mod_64(self, value_1, value_2=None):
        if value_2 is None:
            return int(value_1, 16) % self.two_in_64
        else:
            return hex((int(value_1, 16) + int(value_2, 16)) % self.two_in_64)[2:]

    def minus_mod_64(self, value_1, value_2=None):
        if value_2 is None:
            return int(value_1, 16) % self.two_in_64
        else:
            return hex((int(value_1, 16) - int(value_2, 16)) % self.two_in_64)[2:]

    def right_shift(self, value, count):
        bin_value = ""
        if type(value) == int:
            bin_value = bin(value)[2:]
        elif type(value) == str:           # for hex string
            bin_value = bin(int(value, 16))[2:]

        # print("b_v_r_before:", bin_value, len(bin_value))
        list_value = list(bin_value)
        for i in range(count):
            el_0 = list_value[-1]
            list_value.pop(-1)
            list_value.insert(0, el_0)
        # print("b_v_r_after:", "".join(list_value), len(list_value))
        return hex(self.mod(int("".join(list_value), 2)))[2:]

    def left_shift(self, value, count):
        bin_value = ""
        if type(value) == int:
            bin_value = bin(value)[2:]
        elif type(value) == str:       # for hex string
            bin_value = bin(int(value, 16))[2:]

        # print("b_v_l_before:", bin_value, len(bin_value))
        list_value = list(bin_value)
        for i in range(count):
            el_0 = list_value[0]
            list_value.pop(0)
            list_value.append(el_0)
        # print("b_v_l_after:", "".join(list_value), len(list_value))
        return hex(self.mod(int("".join(list_value), 2)))[2:]

    def xor_operation(self, value_1, value_2):
        # print("val:", value_1, value_2)
        return self.complete_to_64_bit(hex(self.mod(int(value_1, 16) ^ int(value_2, 16)))[2:])

    def xor_key(self):
        self.arr_key = self.hex_str_to_arr(self.hex_key)
        for j in range(math.ceil(len(self.arr_key) / 128)):
            for i in range(min(len(self.arr_key) - 128 * j, 128)):
                self.list_keys[i] = self.xor_operation(self.list_keys[i], self.arr_key[i + j * 128])

    def hex_str_to_arr(self, txt):
        arr = []
        for i in range(len(txt) // 16):
            arr.append(txt[i * 16:(i + 1) * 16])
        if (len(txt) % 16) != 0:
            arr.append(txt[(len(txt) // 16) * 16:])
        return arr

    def add_hex(self, value_1, value_2):
        return hex(self.mod(int(value_1, 16) + int(value_2, 16)))[2:]

    def write_file(self, value):
        if self.first_write:
            mode = 'wb'
            self.first_write = False
        else:
            mode = 'ab'
        with open(self.path_write, mode) as f:
            f.write(value)

    def complete_to_64_bit(self, value_h):
        if len(value_h) < 16:
            temp_v = ""
            for i in range(16-len(value_h)):
                temp_v += "0"
            temp_v += value_h
            return temp_v
        elif len(value_h) > 16:
            return value_h[len(value_h)-16:len(value_h)]
        return value_h

    def complete_to_128_bit(self, value_h):
        if len(value_h) < 32:
            temp_v = ""
            for i in range(32 - len(value_h)):
                temp_v += "0"
            temp_v += value_h
            return temp_v
        elif len(value_h) > 32:
            return value_h[len(value_h) - 32:len(value_h)]
        return value_h

    def clear_last_bytes(self, value_h):
        for i in range(-1, -len(value_h), -1):
            if value_h[i] == "0":
                pass
            elif value_h[i] != "0":
                return value_h[0:i+1]

    def func_t(self, value, mod="direct"):
        if mod == "direct":
            temp_v = self.complete_to_64_bit(value)
            return temp_v[:14] + "00"
        elif mod == "reverse":
            pass

    def encrypt(self):
        self.expand_key()
        self.read_file()
        # f_text = ""
        '''creates two blocks with 64 bits'''
        for i in range(0, len(self.fb_text), 32):
            temp_str = self.fb_text[i:i + 32]
            if len(self.fb_text) < i + 32:
                self.s_0 = self.complete_to_64_bit(temp_str[:16])
                self.s_1 = self.complete_to_64_bit(temp_str[16:])
            # print(temp_str)
            else:
                self.s_0 = temp_str[:16]
                self.s_1 = temp_str[16:]
            result_hpc = ""
            print("s_0:", self.s_0, "s_1:", self.s_1)
            for j in range(8):
                k_1 = self.list_keys[int(self.s_0, 16) & 255]
                self.s_0 = self.xor_operation(self.s_0, self.left_shift(k_1, 8))
                self.s_1 = self.plus_mod_64(self.s_1, k_1)
                self.s_1 = self.xor_operation(self.s_0, self.s_1)
                self.s_0 = self.minus_mod_64(self.s_0, self.right_shift(self.s_1, 11))
                self.s_0 = self.xor_operation(self.s_0, self.left_shift(self.s_1, 2))
                sp_1 = self.spice_list[j ^ 4]
                self.s_0 = self.minus_mod_64(self.s_0, sp_1)
                temp_xor = self.xor_operation(self.left_shift(self.s_0, 32), self.c1)
                self.s_0 = self.plus_mod_64(self.s_0, temp_xor)
                self.s_0 = self.xor_operation(self.s_0, self.right_shift(self.s_0, 17))
                self.s_0 = self.xor_operation(self.s_0, self.right_shift(self.s_0, 34))
                sp_2 = self.spice_list[j]
                self.s_0 = self.xor_operation(self.s_0, sp_2)
                self.s_0 = self.plus_mod_64(self.s_0, self.left_shift(sp_2, 5))
                temp_r_s = self.right_shift(sp_2, 4)
                self.s_0 = self.plus_mod_64(self.s_0, self.left_shift(sp_2, 5))
                x_1 = 22 + (int(self.s_0, 16) & 31)
                self.s_1 = self.plus_mod_64(self.s_1, temp_r_s)
                self.s_0 = self.xor_operation(self.s_0, temp_r_s)
                temp_l_s = self.left_shift(self.s_0, x_1)
                self.s_0 = self.plus_mod_64(self.s_0, temp_l_s)
                self.s_0 = self.xor_operation(self.s_0, self.right_shift(self.s_0, 23))
                sp_3 = self.spice_list[j ^ 7]
                k_2 = self.list_keys[int(self.s_0, 16) & 255]
                self.s_0 = self.minus_mod_64(self.s_0, sp_3)
                self.s_1 = self.xor_operation(self.s_1, k_2)
                k_3 = self.list_keys[(int(self.s_0, 16) & 255) + 3 * j + 1]
                self.s_0 = self.xor_operation(self.s_0, self.left_shift(k_3, 8))
                xor_k_2_3 = self.xor_operation(k_2, k_3)
                self.s_1 = self.plus_mod_64(self.s_1, self.right_shift(xor_k_2_3, 5))
                self.s_0 = self.minus_mod_64(self.s_0, self.left_shift(xor_k_2_3, 12))
                self.s_0 = self.xor_operation(self.s_0, self.func_t(xor_k_2_3))
                self.s_1 = self.plus_mod_64(self.s_1, self.s_0)
                self.s_0 = self.plus_mod_64(self.s_0, self.left_shift(self.s_1, 3))
                sp_4 = self.spice_list[j ^ 2]
                self.s_0 = self.xor_operation(self.s_0, sp_4)
                k_4 = self.list_keys[128 + 16 + j]
                self.s_0 = self.plus_mod_64(self.s_0, k_4)
                self.s_0 = self.plus_mod_64(self.s_0, self.left_shift(self.s_0, 22))
                self.s_0 = self.xor_operation(self.s_0, self.right_shift(self.s_1, 4))
                sp_5 = self.spice_list[j ^ 1]
                self.s_0 = self.plus_mod_64(self.s_0, sp_5)
                x_2 = 33 + j
                self.s_0 = self.xor_operation(self.s_0, self.right_shift(self.s_0, x_2))
            self.s_0 = self.plus_mod_64(self.s_0, self.list_keys[128 + 8])
            self.s_1 = self.plus_mod_64(self.s_1, self.list_keys[128 + 9])
            result_hpc = self.complete_to_64_bit(self.s_0) + self.complete_to_64_bit(self.s_1)
            print("results:", result_hpc)
            self.write_file(bytes.fromhex(result_hpc))
        # print(bytes.fromhex(f_text))
        self.first_write = True

    def decrypt(self):
        self.expand_key()
        self.read_file()
        # f_text = ""
        '''creates two blocks with 64 bits'''
        for i in range(0, len(self.fb_text), 32):
            temp_str = self.fb_text[i:i + 32]
            if len(self.fb_text) < i + 32:
                self.s_0 = self.complete_to_64_bit(temp_str[:16])
                self.s_1 = self.complete_to_64_bit(temp_str[16:])
            # print(temp_str)
            else:
                self.s_0 = temp_str[:16]
                self.s_1 = temp_str[16:]
            result_hpc = ""
            print("s_0:", self.s_0, "s_1:", self.s_1)
            for j in range(7, -1, -1):

                x_1 = 22 + (int(self.s_0, 16) & 31)
                k_4 = self.list_keys[128 + 16 + j]
                k_3 = self.list_keys[(int(self.s_0, 16) & 255) + 3 * j + 1]
                k_2 = self.list_keys[int(self.s_0, 16) & 255]
                k_1 = self.list_keys[int(self.s_0, 16) & 255]
                sp_5 = self.spice_list[j ^ 1]
                sp_4 = self.spice_list[j ^ 2]
                sp_3 = self.spice_list[j ^ 7]
                sp_2 = self.spice_list[j]
                sp_1 = self.spice_list[j ^ 4]
                '''-----------------------------------------------------------------'''
                self.s_0 = self.minus_mod_64(self.s_0, self.list_keys[128 + 8])
                self.s_1 = self.minus_mod_64(self.s_1, self.list_keys[128 + 9])
                x_2 = 33 + j
                self.s_0 = self.xor_operation(self.s_0)
                '''---------------------------------------------------------------------'''
                k_1 = self.list_keys[int(self.s_0, 16) & 255]
                self.s_0 = self.xor_operation(self.s_0, self.left_shift(k_1, 8))
                self.s_1 = self.plus_mod_64(self.s_1, k_1)
                self.s_1 = self.xor_operation(self.s_0, self.s_1)
                self.s_0 = self.minus_mod_64(self.s_0, self.right_shift(self.s_1, 11))
                self.s_0 = self.xor_operation(self.s_0, self.left_shift(self.s_1, 2))
                sp_1 = self.spice_list[j ^ 4]
                self.s_0 = self.minus_mod_64(self.s_0, sp_1)
                temp_xor = self.xor_operation(self.left_shift(self.s_0, 32), self.c1)
                self.s_0 = self.plus_mod_64(self.s_0, temp_xor)
                self.s_0 = self.xor_operation(self.s_0, self.right_shift(self.s_0, 17))
                self.s_0 = self.xor_operation(self.s_0, self.right_shift(self.s_0, 34))
                sp_2 = self.spice_list[j]
                self.s_0 = self.xor_operation(self.s_0, sp_2)
                self.s_0 = self.plus_mod_64(self.s_0, self.left_shift(sp_2, 5))
                temp_r_s = self.right_shift(sp_2, 4)
                self.s_0 = self.plus_mod_64(self.s_0, self.left_shift(sp_2, 5))
                x_1 = 22 + (int(self.s_0, 16) & 31)
                self.s_1 = self.plus_mod_64(self.s_1, temp_r_s)
                self.s_0 = self.xor_operation(self.s_0, temp_r_s)
                temp_l_s = self.left_shift(self.s_0, x_1)
                self.s_0 = self.plus_mod_64(self.s_0, temp_l_s)
                self.s_0 = self.xor_operation(self.s_0, self.right_shift(self.s_0, 23))
                sp_3 = self.spice_list[j ^ 7]
                k_2 = self.list_keys[int(self.s_0, 16) & 255]
                self.s_0 = self.minus_mod_64(self.s_0, sp_3)
                self.s_1 = self.xor_operation(self.s_1, k_2)
                k_3 = self.list_keys[(int(self.s_0, 16) & 255) + 3 * j + 1]
                self.s_0 = self.xor_operation(self.s_0, self.left_shift(k_3, 8))
                xor_k_2_3 = self.xor_operation(k_2, k_3)
                self.s_1 = self.plus_mod_64(self.s_1, self.right_shift(xor_k_2_3, 5))
                self.s_0 = self.minus_mod_64(self.s_0, self.left_shift(xor_k_2_3, 12))
                self.s_0 = self.xor_operation(self.s_0, self.func_t(xor_k_2_3))
                self.s_1 = self.plus_mod_64(self.s_1, self.s_0)
                self.s_0 = self.plus_mod_64(self.s_0, self.left_shift(self.s_1, 3))
                sp_4 = self.spice_list[j ^ 2]
                self.s_0 = self.xor_operation(self.s_0, sp_4)
                k_4 = self.list_keys[128 + 16 + j]
                self.s_0 = self.plus_mod_64(self.s_0, k_4)
                self.s_0 = self.plus_mod_64(self.s_0, self.left_shift(self.s_0, 22))
                self.s_0 = self.xor_operation(self.s_0, self.right_shift(self.s_1, 4))
                sp_5 = self.spice_list[j ^ 1]
                self.s_0 = self.plus_mod_64(self.s_0, sp_5)
                x_2 = 33 + j
                self.s_0 = self.xor_operation(self.s_0, self.right_shift(self.s_0, x_2))
            self.s_0 = self.plus_mod_64(self.s_0, self.list_keys[128 + 8])
            self.s_1 = self.plus_mod_64(self.s_1, self.list_keys[128 + 9])
            result_hpc = self.complete_to_64_bit(self.s_0) + self.complete_to_64_bit(self.s_1)
            print("results:", result_hpc)
            self.write_file(bytes.fromhex(result_hpc))
        # print(bytes.fromhex(f_text))
        self.first_write = True


spice_hpc_1 = "4957df9f02329f2d07289bb61a440e059f9c5dcb93048b5686208a26403c5e7f"
spice_hpc_2 = "706d0051cdb0d7bb8f0c6e4962e43023a0b02b363ffa0b53abf6d3f4f848f5e9"
hpc_alg = HPCMedium("very_secret_key", spice_hpc_1 + spice_hpc_2, "19-Magma.png", "19-Magma.png.hpc")
hpc_alg.encrypt()

# test_st = "0123456789abcdef"
# test_xor = hpc_alg.xor_operation(test_st, hpc_alg.right_shift(test_st, 23))
# print(test_xor)
# test_rev = hpc_alg.xor_operation(test_xor, hpc_alg.right_shift(test_st, 23))
# print(test_rev)
