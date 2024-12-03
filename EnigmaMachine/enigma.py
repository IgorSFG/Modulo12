class Enigma:
    def __init__(self, reflector, plugboard, rotor1, rotor2, rotor3, positions=[0, 0, 0]):
        self.ref = reflector
        self.pb = plugboard
        self.r1 = rotor1
        self.r2 = rotor2
        self.r3 = rotor3
        self.positions = positions

        self.r1.rotate_to(self.positions[0])
        self.r2.rotate_to(self.positions[1])
        self.r3.rotate_to(self.positions[2])

    def encipher(self, char):
        if not char.isalpha():
            return char
        char = char.upper()

        # Rotacionar rotores
        reached_notch = self.r3.rotate()
        if reached_notch:
            reached_notch = self.r2.rotate()
            if reached_notch:
                self.r1.rotate()

        # Passar pelo Plugboard
        char = self.pb.swap(char)
        
        # Passar pelos rotores (direção direta)
        char = self.r3.forward(char)
        char = self.r2.forward(char)
        char = self.r1.forward(char)

        # Passar pelo refletor
        char = self.ref.reflect(char)

        # Voltar pelos rotores (direção inversa)
        char = self.r1.backward(char)
        char = self.r2.backward(char)
        char = self.r3.backward(char)

        # Passar pelo Plugboard novamente
        char = self.pb.swap(char)

        return char
