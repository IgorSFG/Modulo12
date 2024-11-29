class Plugboard:
    def __init__(self, pairs):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for pair in pairs:
            a, b = pair
            pos_a = self.left.index(a)
            pos_b = self.left.index(b)
            self.left = self.left[:pos_a] + b + self.left[pos_a + 1:]
            self.left = self.left[:pos_b] + a + self.left[pos_b + 1:]
    
    def swap(self, index):
        char = self.right[index]
        return self.left.index(char)