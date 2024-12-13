from sympy import mod_inverse
from shor_algorithim import ShorAlgorithm

def read_custom_rsa_public_key(file_path):
    try:
        with open(file_path, 'rb') as file:
            public_key_data = file.read()
        n_length = len(public_key_data) // 2
        n = int.from_bytes(public_key_data[:n_length], 'big')
        e = int.from_bytes(public_key_data[n_length:], 'big')
        return {"modulus": n, "exponent": e}
    except Exception as ex:
        print(f"Erro ao ler a chave pública: {ex}")
        return None

def decrypt_rsa_key(encrypted_aes_key_file, n, d):
    try:
        with open(encrypted_aes_key_file, 'rb') as file:
            encrypted_aes_key = file.read()
        c = int.from_bytes(encrypted_aes_key, 'big')
        m = pow(c, d, n)
        aes_key = m.to_bytes((m.bit_length() + 7) // 8, 'big')
        return aes_key.rjust(16, b'\0')  # Garante que a chave tenha 16 bytes
    except Exception as ex:
        print(f"Erro ao descriptografar a chave AES: {ex}")
        return None

def decrypt_message(cipher_file, aes_key, iv_file):
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import unpad
    try:
        with open(cipher_file, 'rb') as file:
            ciphertext = file.read()
        with open(iv_file, 'rb') as file:
            iv = file.read()
        cipher = AES.new(aes_key, AES.MODE_CBC, iv)
        decrypted = cipher.decrypt(ciphertext)
        return unpad(decrypted, AES.block_size).decode('utf-8', errors='ignore')
    except Exception as ex:
        print(f"Erro ao descriptografar a mensagem: {ex}")
        return None

def main():
    rsa_public_key_path = "public/public_key.bin"
    encrypted_aes_key_path = "public/encrypted_aes_key.bin"
    cipher_file_path = "public/encrypted_message.bin"
    iv_file_path = "public/iv.bin"

    # Passo 1: Ler a chave pública RSA
    rsa_key = read_custom_rsa_public_key(rsa_public_key_path)
    if not rsa_key:
        return
    n, e = rsa_key['modulus'], rsa_key['exponent']
    print(f"Modulus (n): {n}, Exponent (e): {e}")

    # Passo 2: Fatorar n e calcular a chave privada
    shor = ShorAlgorithm(n)
    p, q = shor.factorize()
    print(f"Fatores primos: p={p}, q={q}")

    phi_n = (p - 1) * (q - 1)
    d = mod_inverse(e, phi_n)
    print(f"Chave privada (d): {d}")

    # Passo 3: Descriptografar a chave AES
    aes_key = decrypt_rsa_key(encrypted_aes_key_path, n, d)
    if not aes_key:
        return
    print(f"Chave AES descriptografada: {aes_key.hex()}")

    # Passo 4: Descriptografar a mensagem usando AES
    plaintext = decrypt_message(cipher_file_path, aes_key, iv_file_path)
    if plaintext:
        print("Mensagem descriptografada:")
        print(plaintext)
    else:
        print("Falha ao descriptografar a mensagem.")

if __name__ == "__main__":
    main()