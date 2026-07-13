# Caesar Cipher
def caesar(text, key):
    ans = ""
    for ch in text.upper():
        if ch.isalpha():
            ans += chr((ord(ch)-65+key)%26+65)
        else:
            ans += ch
    return ans

# Playfair Cipher
def playfair(text, key, mode):
    alpha = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key = (key.upper()+alpha).replace("J","I")
    mat = []
    for ch in key:
        if ch not in mat and ch.isalpha():
            mat.append(ch)

    text = text.upper().replace(" ","").replace("J","I")
    if len(text)%2:
        text += "X"

    ans = ""
    for i in range(0,len(text),2):
        a,b = text[i],text[i+1]
        r1=c1=r2=c2=0

        for r in range(5):
            for c in range(5):
                if mat[r*5+c]==a:
                    r1,c1=r,c
                if mat[r*5+c]==b:
                    r2,c2=r,c

        if r1==r2:
            ans += mat[r1*5+(c1+mode)%5]
            ans += mat[r2*5+(c2+mode)%5]
        elif c1==c2:
            ans += mat[((r1+mode)%5)*5+c1]
            ans += mat[((r2+mode)%5)*5+c2]
        else:
            ans += mat[r1*5+c2]
            ans += mat[r2*5+c1]
    return ans

# Menu
while True:
    print("\n1.Caesar\n2.Playfair\n3.Exit")
    ch = input("Choice: ")

    if ch=="1":
        print("1.Encrypt\n2.Decrypt")
        op = input("Choice: ")
        msg = input("Message: ")
        key = int(input("Key: "))
        if op=="1":
            print("Encrypted:", caesar(msg,key))
        else:
            print("Decrypted:", caesar(msg,-key))

    elif ch=="2":
        print("1.Encrypt\n2.Decrypt")
        op = input("Choice: ")
        msg = input("Message: ")
        key = input("Keyword: ")
        if op=="1":
            print("Encrypted:", playfair(msg,key,1))
        else:
            print("Decrypted:", playfair(msg,key,-1))

    elif ch=="3":
        print("Thank You")
        break

    else:
        print("Invalid Choice")
