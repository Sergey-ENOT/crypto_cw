import ctypes
import string


class ScreenResolution:
    def __init__(self):
        self.user32 = ctypes.windll.user32
        self.width = 0
        self.height = 0
        self.dict_res = {}
        self.screen_resolution()

    def screen_resolution(self):
        self.width = self.user32.GetSystemMetrics(0)
        self.height = self.user32.GetSystemMetrics(1)

    def get_resolution(self, type_answer=None):
        if (type_answer == "dict") or (type_answer is None):
            self.dict_res["width"] = self.width
            self.dict_res["height"] = self.height
            return self.dict_res


scr = ScreenResolution()
print(scr.get_resolution())
