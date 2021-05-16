from math import gcd


def modinv(a, m): # calculates modulo inverse of a for mod m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


def coprimes(a): # calculates all possible co-prime numbers with a
    return [i for i in range(2,a) if gcd(i,a)== 1]


def encrypt_block(m): # encrypts a single block
    c = m ** e % n
    return c


def decrypt_block(c): # decrypts a single block
    m = c ** d % n
    return m

def encrypt_string(s): # applies encryption
    return ''.join([chr(encrypt_block(ord(x))) for x in list(s)])


def decrypt_string(s): # applies decryption
    return ''.join([chr(decrypt_block(ord(x))) for x in list(s)])


p = int(input('Enter prime p: '))
q = int(input('Enter prime q: '))

print("Choosen primes:\np=" + str(p) + ", q=" + str(q) + "\n")

n = p * q
print("n = p * q = " + str(n) + "\n")

phi = (p - 1) * (q - 1)
print("Euler's function (totient) [phi(n)]: " + str(phi) + "\n")

print("Choose an e from a below coprimes array:\n")
print(str(coprimes(phi)) + "\n")
e = int(input())

d = modinv(e, phi) # calculates the decryption key d

print("\nYour public key is a pair of numbers (e=" + str(e) + ", n=" + str(n) + ").\n")
print("Your private key is a pair of numbers (d=" + str(d) + ", n=" + str(n) + ").\n")

s = input("Enter a message to encrypt: ")
print("\nPlain message: " + s + "\n")
enc = encrypt_string(s)
print("Encrypted message: ", enc, "\n")
dec = decrypt_string(enc)
print("Decrypted message: " + dec + "\n")












































"""


################OUTPUT#######################################
python RSA.py
Enter prime p: 13
Enter prime q: 17
Choosen primes:
p=13, q=17

n = p * q = 221

Euler's function (totient) [phi(n)]: 192

Choose an e from a below coprimes array:

[5, 7, 11, 13, 17, 19, 23, 25, 29, 35, 37, 41, 43, 47, 49, 53, 55, 59, 61, 67, 71, 73, 77, 79, 83, 85, 89, 91, 97, 101, 103, 107, 109, 113, 115, 119, 121, 125, 131, 133, 137, 139, 143, 145, 149, 151, 155, 157, 163, 167, 169, 173, 175, 179, 181, 185, 187]

85

Your public key is a pair of numbers (e=85, n=221).

Your private key is a pair of numbers (d=61, n=221).

Enter a message to encrypt: "1010110"

Plain message: 1010110

('Encrypted message: ', '$\xa5$\xa5$$\xa5', '\n')
Decrypted message: 1010110"""
