from math import gcd

# Function to check if a number is prime

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to find modular inverse
def mod_inverse(e, phi):
    for d in range(1, phi):
        if (d * e) % phi == 1:
            return d
    return None

# User Input

p = int(input("Enter first prime number (p): "))
q = int(input("Enter second prime number (q): "))

# Check if inputs are prime

if not is_prime(p) or not is_prime(q):
    print("Error: Both numbers must be prime.")
    exit()

# Calculate n and phi

n = p * q
phi = (p - 1) * (q - 1)

# Input e

e = int(input(f"Enter public exponent e :"))

if gcd(e, phi) != 1:
    print("Error: e must be coprime with phi.")
    exit()

# Find private key d

d = mod_inverse(e, phi)

if d is None:
    print("Error: Modular inverse not found.")
    exit()

# Input message

message = int(input(f"Enter numeric message (< {n}): "))

if message >= n:
    print("Error: Message must be smaller than n.")
    exit()

# Encryption

cipher = pow(message, e, n)
print("\nEncrypted Message:", cipher)

# Decryption

decrypted = pow(cipher, d, n)
print("Decrypted Message:", decrypted)

# Keys

print("\nPublic Key (e, n):", (e, n))
print("Private Key (d, n):", (d, n))
