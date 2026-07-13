from tkinter import *
from tkinter import messagebox

# Rail Fence
def rail_encrypt(t):
    return t[::2] + t[1::2]

def rail_decrypt(t):
    m = (len(t)+1)//2
    a, b = t[:m], t[m:]
    r = ""
    for i in range(len(b)):
        r += a[i] + b[i]
    if len(a) > len(b):
        r += a[-1]
    return r

# Columnar
def column_encrypt(t, k):
    while len(t) % k != 0:
        t += "X"
    return "".join(t[i::k] for i in range(k))

def column_decrypt(t, k):
    rows = len(t)//k
    col = [t[i*rows:(i+1)*rows] for i in range(k)]
    return "".join(col[c][r] for r in range(rows) for c in range(k))

# Process
def run():
    msg = e1.get()

    if cipher.get() == "Rail":
        ans = rail_encrypt(msg) if op.get() == "Encrypt" else rail_decrypt(msg)
    else:
        try:
            key = int(e2.get())
            ans = column_encrypt(msg, key) if op.get() == "Encrypt" else column_decrypt(msg, key)
        except:
            messagebox.showerror("Error", "Enter Key")
            return

    out.config(text=ans)

# GUI
root = Tk()
root.title("Transposition Cipher")
root.geometry("400x350")

cipher = StringVar(value="Rail")
op = StringVar(value="Encrypt")

Label(root, text="Cipher").pack()
OptionMenu(root, cipher, "Rail", "Columnar").pack()

Label(root, text="Operation").pack()
OptionMenu(root, op, "Encrypt", "Decrypt").pack()

Label(root, text="Message").pack()
e1 = Entry(root, width=30)
e1.pack()

Label(root, text="Key (Columnar)").pack()
e2 = Entry(root, width=10)
e2.pack()

Button(root, text="Run", command=run).pack(pady=10)

out = Label(root, text="", font=("Arial", 12))
out.pack()

root.mainloop()
