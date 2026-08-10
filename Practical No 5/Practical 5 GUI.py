import tkinter as tk
from tkinter import messagebox


# Diffie-Hellman Calculation
def calculate():
    try:
        p = int(p_entry.get())
        g = int(g_entry.get())
        a = int(alice_entry.get())
        b = int(bob_entry.get())

        if p <= 1 or a <= 0 or b <= 0:
            raise ValueError

        # Public keys
        A = pow(g, a, p)
        B = pow(g, b, p)

        # Shared secret keys
        alice_secret = pow(B, a, p)
        bob_secret = pow(A, b, p)

        # Display results
        alice_public.config(text=str(A))
        bob_public.config(text=str(B))
        alice_secret_label.config(text=str(alice_secret))
        bob_secret_label.config(text=str(bob_secret))

        if alice_secret == bob_secret:
            result.config(
                text="✓ KEY EXCHANGE SUCCESSFUL",
                fg="#00ffcc"
            )
        else:
            result.config(
                text="✗ KEY EXCHANGE FAILED",
                fg="red"
            )

    except ValueError:
        messagebox.showerror(
            "Error",
            "Please enter valid positive numbers."
        )


# Clear function
def clear():
    p_entry.delete(0, tk.END)
    g_entry.delete(0, tk.END)
    alice_entry.delete(0, tk.END)
    bob_entry.delete(0, tk.END)

    alice_public.config(text="-")
    bob_public.config(text="-")
    alice_secret_label.config(text="-")
    bob_secret_label.config(text="-")
    result.config(text="READY", fg="#00ffcc")


# Fullscreen toggle
def fullscreen(event=None):
    root.attributes("-fullscreen", not root.attributes("-fullscreen"))


# Exit fullscreen
def exit_fullscreen(event=None):
    root.attributes("-fullscreen", False)


# ---------------- GUI ----------------

root = tk.Tk()
root.title("Diffie-Hellman Key Exchange")

# Full screen
root.attributes("-fullscreen", True)

root.configure(bg="#050505")

# Press F11 to toggle fullscreen
root.bind("<F11>", fullscreen)

# Press Escape to exit fullscreen
root.bind("<Escape>", exit_fullscreen)


# Title
tk.Label(
    root,
    text="DIFFIE-HELLMAN KEY EXCHANGE",
    font=("Arial", 28, "bold"),
    bg="#050505",
    fg="#00ffcc"
).pack(pady=30)


# Public Parameters
tk.Label(
    root,
    text="Public Parameters",
    font=("Arial", 18, "bold"),
    bg="#050505",
    fg="white"
).pack(pady=10)


# Prime number
tk.Label(
    root,
    text="Prime Number (p)",
    font=("Arial", 13),
    bg="#050505",
    fg="white"
).pack()

p_entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=20,
    bg="#111111",
    fg="#00ffcc",
    insertbackground="#00ffcc"
)
p_entry.pack(pady=5)
p_entry.insert(0, "23")


# Primitive root
tk.Label(
    root,
    text="Primitive Root (g)",
    font=("Arial", 13),
    bg="#050505",
    fg="white"
).pack()

g_entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=20,
    bg="#111111",
    fg="#00ffcc",
    insertbackground="#00ffcc"
)
g_entry.pack(pady=5)
g_entry.insert(0, "5")


# Alice and Bob
people = tk.Frame(root, bg="#050505")
people.pack(pady=25)


# Alice
alice_frame = tk.Frame(
    people,
    bg="#111111",
    padx=30,
    pady=20
)
alice_frame.pack(side="left", padx=30)

tk.Label(
    alice_frame,
    text="ALICE",
    font=("Arial", 20, "bold"),
    bg="#111111",
    fg="#00ccff"
).pack(pady=10)

tk.Label(
    alice_frame,
    text="Private Key (a)",
    bg="#111111",
    fg="white",
    font=("Arial", 12)
).pack()

alice_entry = tk.Entry(
    alice_frame,
    font=("Arial", 14),
    width=15,
    bg="#222222",
    fg="white",
    insertbackground="white"
)
alice_entry.pack(pady=5)
alice_entry.insert(0, "6")

tk.Label(
    alice_frame,
    text="Public Key (A)",
    bg="#111111",
    fg="white"
).pack(pady=(10, 0))

alice_public = tk.Label(
    alice_frame,
    text="-",
    font=("Arial", 18, "bold"),
    bg="#111111",
    fg="#00ccff"
)
alice_public.pack()

tk.Label(
    alice_frame,
    text="Shared Secret",
    bg="#111111",
    fg="white"
).pack(pady=(10, 0))

alice_secret_label = tk.Label(
    alice_frame,
    text="-",
    font=("Arial", 18, "bold"),
    bg="#111111",
    fg="#00ffcc"
)
alice_secret_label.pack()


# Bob
bob_frame = tk.Frame(
    people,
    bg="#111111",
    padx=30,
    pady=20
)
bob_frame.pack(side="left", padx=30)

tk.Label(
    bob_frame,
    text="BOB",
    font=("Arial", 20, "bold"),
    bg="#111111",
    fg="#cc66ff"
).pack(pady=10)

tk.Label(
    bob_frame,
    text="Private Key (b)",
    bg="#111111",
    fg="white",
    font=("Arial", 12)
).pack()

bob_entry = tk.Entry(
    bob_frame,
    font=("Arial", 14),
    width=15,
    bg="#222222",
    fg="white",
    insertbackground="white"
)
bob_entry.pack(pady=5)
bob_entry.insert(0, "15")

tk.Label(
    bob_frame,
    text="Public Key (B)",
    bg="#111111",
    fg="white"
).pack(pady=(10, 0))

bob_public = tk.Label(
    bob_frame,
    text="-",
    font=("Arial", 18, "bold"),
    bg="#111111",
    fg="#cc66ff"
)
bob_public.pack()

tk.Label(
    bob_frame,
    text="Shared Secret",
    bg="#111111",
    fg="white"
).pack(pady=(10, 0))

bob_secret_label = tk.Label(
    bob_frame,
    text="-",
    font=("Arial", 18, "bold"),
    bg="#111111",
    fg="#00ffcc"
)
bob_secret_label.pack()


# Buttons
buttons = tk.Frame(root, bg="#050505")
buttons.pack(pady=15)

tk.Button(
    buttons,
    text="EXCHANGE KEYS",
    command=calculate,
    font=("Arial", 13, "bold"),
    bg="#006666",
    fg="white",
    activebackground="#00aaaa",
    padx=30,
    pady=10
).pack(side="left", padx=10)

tk.Button(
    buttons,
    text="CLEAR",
    command=clear,
    font=("Arial", 13, "bold"),
    bg="#333333",
    fg="white",
    padx=30,
    pady=10
).pack(side="left", padx=10)


# Result
result = tk.Label(
    root,
    text="READY",
    font=("Arial", 20, "bold"),
    bg="#050505",
    fg="#00ffcc"
)
result.pack(pady=15)


# Run
root.mainloop()
