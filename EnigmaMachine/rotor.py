class Rotor:
    def __init__(self, wiring, notch):
        self.left = wiring
        self.right = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.notch = notch

    def forward(self, index):
        char = self.right[index]
        return self.left.index(char)

    def backward(self, index):
        char = self.left[index]
        return self.right.index(char)

    def rotate(self):
        self.left = self.left[1:] + self.left[0]
        self.right = self.right[1:] + self.right[0]

    def rotate_to(self, pos):
        self.left = self.left[pos:] + self.left[:pos]
        self.right = self.right[pos:] + self.right[:pos]

    def reached_notch(self):
        return self.right[0] == self.notch


    
