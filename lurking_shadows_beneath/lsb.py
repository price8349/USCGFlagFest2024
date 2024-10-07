import socket


conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(('0.cloud.chals.io', 19108))
data = conn.recv(1024).strip().decode()
lines = data.split("\n")


n = 0
e = 0
c = 0

for line in lines:
    if line.startswith("Public Key: "):
        e = 65537 # default
        n = int(line[15:].split(", ")[0]) 
    elif line.startswith("Ciphertext: "):
        c = int(line[12:])
    

def oracle(c):
     conn.send((str(c)+ "\n").encode("ascii"))
     data = conn.recv(1024).decode()
     return int(data[0])   

def attack(N, e, c, oracle):
    """
    Recovers the plaintext from the ciphertext using the LSB oracle (parity oracle) attack.
    :param N: the modulus
    :param e: the public exponent
    :param c: the encrypted message
    :param oracle: a function which returns the last bit of a plaintext for a given ciphertext
    :return: the plaintext
    """
    left = 0
    right = N
    while right - left > 1:
        print(right, left)
        c = (c * pow(2, e, N)) % N
        if oracle(c) == 0:
            right = (right + left) // 2
        else:
            left = (right + left) // 2

    return int(right)

print(hex(attack(n,e,c,oracle)))
