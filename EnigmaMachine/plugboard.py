class Plugboard:
    def __init__(self, wiring=''):
        self.left = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.right = {}
        for c in self.left:
            self.right[c] = c
        pairs = wiring.upper().split()
        for pair in pairs:
            if len(pair) == 2:
                a, b = pair[0], pair[1]
                self.right[a] = b
                self.right[b] = a

    def swap(self, c):
        output = self.right[c]
        return output