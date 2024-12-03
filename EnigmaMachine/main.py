from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflector
from enigma import Enigma
import sys

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
enigma = Enigma(C, pb, i, ii, iii, [0, 0, 0])

def main():
   if len(sys.argv) < 2:
      print('Usage: python main.py <text>')
      sys.exit(1)
      
   original = sys.argv[1]
   criptografado = ''
   for c in original:
      criptografado += enigma.encipher(c)
   print(criptografado)

if __name__ == '__main__':
   main()