class Enigma:
    def __init__(self, reflector, rotor1, rotor2, rotor3, plugboard):
        self.ref = reflector
        self.r1 = rotor1
        self.r2 = rotor2
        self.r3 = rotor3
        self.pb = plugboard

    def set_rotors(self, positions):
        self.r1.rotate_to(positions[0])
        self.r2.rotate_to(positions[1])
        self.r3.rotate_to(positions[2])

    def encipher(self, char):
        if not char.isalpha():
            return char
        char = char.upper()

        index = ord(char) - ord('A')

        # Passar pelo Plugboard
        index = self.pb.swap(index)
        
        # Passar pelos rotores (direção direta)
        index = self.r1.forward(index)
        index = self.r2.forward(index)
        index = self.r3.forward(index)

        # Passar pelo refletor
        index = self.ref.reflect(index)

        # Voltar pelos rotores (direção inversa)
        index = self.r3.backward(index)
        index = self.r2.backward(index)
        index = self.r1.backward(index)

        # Passar pelo Plugboard novamente
        index = self.pb.swap(index)

        # Rotacionar rotores
        self.r1.rotate()
        if self.r1.reached_notch():
            self.r2.rotate()
            if self.r2.reached_notch():
                self.r3.rotate()
        
        char = chr(index + ord('A'))

        return char
