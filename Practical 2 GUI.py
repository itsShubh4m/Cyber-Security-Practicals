import tkinter as tk
from math import gcd

#RSA Functions

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (d * e) % phi == 1:
            return d
    return None

# Functions

def generate():
    global n, e, d

    p = int(ep.get())
    q = int(eq.get())
    e = int(ee.get())

    if not is_prime(p) or not is_prime(q):
        pub.config(text="Invalid Prime Numbers")
        return

    n = p * q
    phi = (p - 1) * (q - 1)

    if gcd(e, phi) != 1:
        pub.config(text="Invalid e")
        return

    d = mod_inverse(e, phi)

    pub.config(text=f"Public Key : ({e}, {n})")
    pri.config(text=f"Private Key : ({d}, {n})")

def encrypt():
    m = int(em.get())
    c = pow(m, e, n)
    cipher.config(text=f"Cipher : {c}")

def decrypt():
    c = int(ec.get())
    m = pow(c, d, n)
    plain.config(text=f"Message : {m}")

def clear():
    ep.delete(0, tk.END)
    eq.delete(0, tk.END)
    ee.delete(0, tk.END)
    em.delete(0, tk.END)
    ec.delete(0, tk.END)

    pub.config(text="")
    pri.config(text="")
    cipher.config(text="")
    plain.config(text="")

#Window
    
root = tk.Tk()
root.title("RSA Algorithm")
root.state("zoomed")
root.configure(bg="black")

root.bind("<Escape>", lambda e: root.state("normal"))

frame = tk.Frame(root, bg="black")
frame.place(relx=0.5, rely=0.5, anchor="center")

title = tk.Label(
    frame,
    text="RSA ENCRYPTION",
    font=("Arial", 24, "bold"),
    bg="black",
    fg="cyan"
)
title.grid(row=0, column=0, columnspan=2, pady=20)

#Inputs

labels = ["Prime p", "Prime q", "Public e", "Message", "Cipher"]

entries = []

for i, text in enumerate(labels):
    tk.Label(frame,
             text=text,
             bg="black",
             fg="cyan",
             font=("Arial", 12)).grid(row=i+1, column=0, pady=8)

    entry = tk.Entry(frame,
                     width=25,
                     bg="#111111",
                     fg="cyan",
                     insertbackground="cyan")
    entry.grid(row=i+1, column=1, pady=8)
    entries.append(entry)

ep, eq, ee, em, ec = entries

#Buttons

tk.Button(frame, text="Generate Keys",
          command=generate,
          bg="cyan").grid(row=6, column=0, pady=15)

tk.Button(frame, text="Encrypt",
          command=encrypt,
          bg="cyan").grid(row=6, column=1)

tk.Button(frame, text="Decrypt",
          command=decrypt,
          bg="cyan").grid(row=7, column=0)

tk.Button(frame, text="Clear",
          command=clear,
          bg="cyan").grid(row=7, column=1)

#Outputs

pub = tk.Label(frame, text="", bg="black", fg="cyan", font=("Arial", 12))
pub.grid(row=8, column=0, columnspan=2, pady=5)

pri = tk.Label(frame, text="", bg="black", fg="cyan", font=("Arial", 12))
pri.grid(row=9, column=0, columnspan=2, pady=5)

cipher = tk.Label(frame, text="", bg="black", fg="cyan", font=("Arial", 12))
cipher.grid(row=10, column=0, columnspan=2, pady=5)

plain = tk.Label(frame, text="", bg="black", fg="cyan", font=("Arial", 12))
plain.grid(row=11, column=0, columnspan=2, pady=5)

root.mainloop()
