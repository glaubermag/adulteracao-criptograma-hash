from pwn import *

# Mensagem original (m)
m = b"Esta e a mensagem original"

# Mensagem adulterada (n)
n = b"Esta e a mensagem adulterada"

# Chave secreta (k) - deve ser a mesma usada para criptografar a mensagem original
k = b"chave_secreta"

def xor_strings(s1, s2):
    # Repete a chave s2 até que ela tenha o mesmo tamanho de s1
    s2 = (s2 * (len(s1) // len(s2) + 1))[:len(s1)]
    return bytes([a ^ b for a, b in zip(s1, s2)])

# Criptografar a mensagem original (c = m xor k)
c = xor_strings(m, k)

# Calcular a adulteração maliciosa (x = m xor n)
x = xor_strings(m, n)

# Calcular o criptograma adulterado (y = c xor x)
y = xor_strings(c, x)

# Descriptografar o criptograma adulterado (y xor k)
mensagem_recuperada = xor_strings(y, k)

# Imprimir os resultados
print(f"Mensagem original (m): {m.decode()}")
print(f"Mensagem adulterada (n): {n.decode()}")
print(f"Criptograma original (c): {c.hex()}")
print(f"Adulteração maliciosa (x): {x.hex()}")
print(f"Criptograma adulterado (y): {y.hex()}")
print(f"Mensagem recuperada: {mensagem_recuperada.decode()}")