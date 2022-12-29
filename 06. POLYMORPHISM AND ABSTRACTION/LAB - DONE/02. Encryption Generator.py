class EncryptionGenerator:
    def __init__(self, text):
        self.text = text

    def __add__(self, other):
        if not isinstance(other, int):
            raise ValueError("You must add a number.")

        result = ''
        for el in self.text:
            enc = ord(el) + other

            while enc < 32:
                enc += 95
            while enc > 126:
                enc -= 95

            result += chr(enc)

        return result

# 100/100
