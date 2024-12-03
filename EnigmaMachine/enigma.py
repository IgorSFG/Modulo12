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

        # Rotacionar rotores
        reached_notch = self.r1.rotate()
        if reached_notch:
            reached_notch = self.r2.rotate()
            if reached_notch:
                self.r3.rotate()

        # Passar pelo Plugboard
        char = self.pb.swap(char)
        
        # Passar pelos rotores (direção direta)
        char = self.r1.forward(char)
        char = self.r2.forward(char)
        char = self.r3.forward(char)

        # Passar pelo refletor
        char = self.ref.reflect(char)

        # Voltar pelos rotores (direção inversa)
        char = self.r3.backward(char)
        char = self.r2.backward(char)
        char = self.r1.backward(char)

        # Passar pelo Plugboard novamente
        char = self.pb.swap(char)
        


        return char
