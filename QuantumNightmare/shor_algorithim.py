import sys
import random

class ShorAlgorithm:
    def __init__(self, N):
        if N < 2 or N % 2 == 0:
            raise ValueError("N deve ser um número ímpar maior que 2.")
        self.N = N

    def is_prime(self, n):
        """Testa se um número é primo."""
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def modular_exponentiation(self, base, exponent, mod):
        result = 1
        base = base % mod
        while exponent > 0:
            if (exponent % 2) == 1:
                result = (result * base) % mod
            exponent = exponent >> 1
            base = (base * base) % mod
        return result

    def find_period(self, a):
        r = 1
        while self.modular_exponentiation(a, r, self.N) != 1:
            r += 1
        return r

    def factorize(self):
        if self.is_prime(self.N):
            return [self.N]

        while True:
            a = random.randint(2, self.N - 1)
            print(f"Escolhendo a = {a}")
            
            # Passo 1: Verifica se a e N são coprimos
            d = self.gcd(a, self.N)
            if d > 1:
                return [d, self.N // d]

            # Passo 2: Encontra o período r
            r = self.find_period(a)
            print(f"Período encontrado: r = {r}")

            if r % 2 != 0 or self.modular_exponentiation(a, r // 2, self.N) == self.N - 1:
                print("Período inválido. Tentando novamente...")
                continue

            # Passo 3: Calcula os fatores
            p = self.gcd(self.modular_exponentiation(a, r // 2, self.N) - 1, self.N)
            q = self.gcd(self.modular_exponentiation(a, r // 2, self.N) + 1, self.N)

            if p * q == self.N:
                return [p, q]

if __name__ == "__main__":
    N = int(sys.argv[1])
    shor = ShorAlgorithm(N)
    fatores = shor.factorize()
    print(f"Fatores de {N}: {fatores}")