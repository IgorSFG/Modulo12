class Rotor:
    def __init__(self, wiring, notch, position=0):
        self.left = wiring
        self.right = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.notch = notch
        self.position = position % 26

    def forward(self, c):
        idx = (self.right.index(c) + self.position) % 26
        letter = self.left[idx]
        output = self.right[(self.right.index(letter) - self.position) % 26]
        return output

    def backward(self, c):
        idx = (self.right.index(c) + self.position ) % 26
        letter = self.right[self.left.index(self.right[idx])]
        output = self.right[(self.right.index(letter) - self.position) % 26]
        return output

    def rotate(self):
        self.position = (self.position + 1) % 26
        return self.right[self.position] == self.notch
    
    def rotate_to(self, pos):
        self.position = pos % 26