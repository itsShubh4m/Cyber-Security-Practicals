from tkinter import *

def encrypt():
    msg = text.get()
    key = int(k.get())
    ans = ""
    for ch in msg.upper():
        if ch.isalpha():
            ans += chr((ord(ch)-65+key)%26+65)
        else:
            ans += ch
    result.config(text="Encrypted : "+ans)

def decrypt():
    msg = text.get()
    key = int(k.get())
    ans = ""
    for ch in msg.upper():
        if ch.isalpha():
            ans += chr((ord(ch)-65-key)%26+65)
        else:
            ans += ch
    result.config(text="Decrypted : "+ans)

root = Tk()
root.title("Caesar Cipher")
root.state("zoomed")
root.configure(bg="black")

Label(root,text="CAESAR CIPHER",font=("Arial",24,"bold"),
      bg="black",fg="cyan").pack(pady=20)

Label(root,text="Message",bg="black",fg="white").pack()
text = Entry(root,width=40,font=15)
text.pack()

Label(root,text="Key",bg="black",fg="white").pack()
k = Entry(root,width=10,font=15)
k.pack()

Button(root,text="Encrypt",bg="cyan",fg="black",
       command=encrypt,width=15).pack(pady=10)

Button(root,text="Decrypt",bg="cyan",fg="black",
       command=decrypt,width=15).pack()

result = Label(root,text="",font=("Arial",16),
               bg="black",fg="lime")
result.pack(pady=20)

Button(root,text="Exit",command=root.destroy,
       bg="red",fg="white",width=10).pack()

root.mainloop()
