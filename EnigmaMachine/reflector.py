class Reflector:
    def __init__(self, wiring):
        self.left   = wiring
        self.right  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    def reflect(self, c):
        idx = self.right.index(c)
        output = self.left[idx]
        return output