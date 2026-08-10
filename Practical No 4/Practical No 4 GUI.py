import tkinter as tk
import hashlib

n = 3233
e = 17
d = 2753


def sign():
    message = msg.get("1.0", tk.END).strip()

    h = int(hashlib.sha256(message.encode()).hexdigest(), 16)
    signature = pow(h, d, n)

    sig.delete("1.0", tk.END)
    sig.insert("1.0", str(signature))


def verify():
    message = msg.get("1.0", tk.END).strip()
    signature = int(sig.get("1.0", tk.END).strip())

    h = int(hashlib.sha256(message.encode()).hexdigest(), 16)
    check = pow(signature, e, n)

    if check == h % n:
        result.config(text="✓ Signature Valid", fg="#00ffff")
    else:
        result.config(text="✗ Signature Invalid", fg="red")


# Window
root = tk.Tk()
root.title("RSA Digital Signature")
root.attributes("-fullscreen", True)
root.configure(bg="black")

# Title
tk.Label(
    root,
    text="RSA DIGITAL SIGNATURE",
    font=("Arial", 28, "bold"),
    fg="#00ffff",
    bg="black"
).pack(pady=40)

# Message
tk.Label(
    root,
    text="Enter Message",
    font=("Arial", 16),
    fg="#00ffff",
    bg="black"
).pack()

msg = tk.Text(
    root,
    height=6,
    width=80,
    bg="#111111",
    fg="#00ffff",
    insertbackground="#00ffff",
    font=("Arial", 14)
)
msg.pack(pady=15)

# Signature
tk.Label(
    root,
    text="Digital Signature",
    font=("Arial", 16),
    fg="#00ffff",
    bg="black"
).pack()

sig = tk.Text(
    root,
    height=3,
    width=80,
    bg="#111111",
    fg="#00ffff",
    insertbackground="#00ffff",
    font=("Arial", 14)
)
sig.pack(pady=15)

# Buttons
tk.Button(
    root,
    text="SIGN",
    command=sign,
    width=15,
    bg="#00ffff",
    fg="black",
    font=("Arial", 12, "bold")
).pack(pady=10)

tk.Button(
    root,
    text="VERIFY",
    command=verify,
    width=15,
    bg="#00ffff",
    fg="black",
    font=("Arial", 12, "bold")
).pack(pady=10)

# Result
result = tk.Label(
    root,
    text="",
    font=("Arial", 18, "bold"),
    bg="black"
)
result.pack(pady=20)

root.mainloop()
