from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflector
from enigma import Enigma

# Rotores
i   = Rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'Q')
ii  = Rotor('AJDKSIRUXBLHWTMCQGZNPYFVOE', 'E')
iii = Rotor('BDFHJLCPRTXVZNYEIWGAKMUSQO', 'V')
iv  = Rotor('ESOVPZJAYQUIRHXLNFTGKDCMWB', 'J')
v   = Rotor('VZBRGITYUPSDNHLXAWMJQOFECK', 'Z')

# Refletores:
B = Reflector('YRUHQSLDPXNGOKMIEBFZCWVJAT')
C = Reflector('FVPJIAOYEDRZXWGCTKUQSBNMHL')

# Plugboard
pb = Plugboard('AR GK OX')

# Enigma
enigma = Enigma(C, iii, ii, i, pb)
enigma.set_rotors([0, 0, 0])

original = 'TESTANDO'
print(original)
criptografado = ''
for c in original:
   criptografado += enigma.encipher(c)
print(criptografado)