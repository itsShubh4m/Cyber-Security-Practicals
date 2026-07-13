# Rail Fence Cipher
def rail_encrypt(text):
    odd = text[::2]
    even = text[1::2]
    return odd + even

def rail_decrypt(text):
    mid = (len(text)+1)//2
    odd = text[:mid]
    even = text[mid:]
    result = ""
    for i in range(len(even)):
        result += odd[i] + even[i]
    if len(odd) > len(even):
        result += odd[-1]
    return result


# Columnar Transposition Cipher
def column_encrypt(text, key):
    while len(text) % key != 0:
        text += "X"
    result = ""
    for i in range(key):
        result += text[i::key]
    return result

def column_decrypt(text, key):
    rows = len(text) // key
    cols = []
    for i in range(key):
        cols.append(text[i*rows:(i+1)*rows])
    result = ""
    for r in range(rows):
        for c in range(key):
            result += cols[c][r]
    return result


# Main Menu
while True:
    print("\n===== Transposition Cipher =====")
    print("1. Rail Fence")
    print("2. Columnar")
    print("3. Exit")

    ch = input("Enter Choice: ")

    if ch == "1":
        print("\n1. Encrypt")
        print("2. Decrypt")
        op = input("Enter Choice: ")

        msg = input("Enter Message: ")

        if op == "1":
            print("Encrypted:", rail_encrypt(msg))
        elif op == "2":
            print("Decrypted:", rail_decrypt(msg))

    elif ch == "2":
        print("\n1. Encrypt")
        print("2. Decrypt")
        op = input("Enter Choice: ")

        msg = input("Enter Message: ")
        key = int(input("Enter Key: "))

        if op == "1":
            print("Encrypted:", column_encrypt(msg, key))
        elif op == "2":
            print("Decrypted:", column_decrypt(msg, key))

    elif ch == "3":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
