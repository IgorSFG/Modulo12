class Reflector:
    def __init__(self, mapping):
        self.left   = mapping
        self.right  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    def reflect(self, index):
        char = self.right[index]
        return self.left.index(char)