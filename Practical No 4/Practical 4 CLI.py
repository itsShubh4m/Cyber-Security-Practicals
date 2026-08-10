import hashlib

# RSA values
n = 3233
e = 17
d = 2753

while True:
    print("\n===== DIGITAL SIGNATURE =====")
    print("1. Sign Message")
    print("2. Verify Message")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        message = input("Enter message: ")

        # Hash message
        h = int(hashlib.sha256(message.encode()).hexdigest(), 16)

        # Generate signature
        signature = pow(h, d, n)

        print("Digital Signature:", signature)

    elif choice == "2":
        message = input("Enter message: ")
        signature = int(input("Enter digital signature: "))

        # Hash message
        h = int(hashlib.sha256(message.encode()).hexdigest(), 16)

        # Verify signature
        check = pow(signature, e, n)

        if check == h % n:
            print("Signature is VALID")
            print("Message is authentic.")
        else:
            print("Signature is INVALID")
            print("Message may have been changed.")

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
