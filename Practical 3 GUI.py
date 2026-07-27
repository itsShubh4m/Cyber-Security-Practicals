import tkinter as tk
from tkinter import messagebox
import hmac
import hashlib

# ---------------- Generate MAC ----------------
def generate_mac():
    key = entry_key.get().encode()
    message = text_message.get("1.0", tk.END).strip().encode()

    if not key or not message:
        messagebox.showerror("Error", "Please enter both Secret Key and Message.")
        return

    mac = hmac.new(key, message, hashlib.sha256).hexdigest()

    entry_generated_mac.config(state="normal")
    entry_generated_mac.delete(0, tk.END)
    entry_generated_mac.insert(0, mac)
    entry_generated_mac.config(state="readonly")


# ---------------- Verify MAC ----------------
def verify_mac():
    key = entry_key.get().encode()
    received_message = text_verify_message.get("1.0", tk.END).strip().encode()
    received_mac = entry_verify_mac.get()

    if not key or not received_message or not received_mac:
        messagebox.showerror("Error", "Please fill all verification fields.")
        return

    new_mac = hmac.new(key, received_message, hashlib.sha256).hexdigest()

    if hmac.compare_digest(received_mac, new_mac):
        result_label.config(
            text="✔ MAC Verification Successful!\nMessage is Authentic.",
            fg="green"
        )
    else:
        result_label.config(
            text="✘ MAC Verification Failed!\nMessage has been Modified.",
            fg="red"
        )


# ---------------- GUI ----------------
root = tk.Tk()
root.title("Message Authentication Code (MAC)")
root.geometry("650x600")
root.configure(bg="black")

title = tk.Label(
    root,
    text="MAC Generator & Verifier",
    font=("Arial", 18, "bold"),
    bg="black",
    fg="cyan"
)
title.pack(pady=10)

# Secret Key
tk.Label(root, text="Secret Key", bg="black", fg="cyan",
         font=("Arial", 11)).pack()

entry_key = tk.Entry(root, width=50, bg="#1a1a1a",
                     fg="white", insertbackground="white")
entry_key.pack(pady=5)

# Message
tk.Label(root, text="Message", bg="black", fg="cyan",
         font=("Arial", 11)).pack()

text_message = tk.Text(root, height=4, width=55,
                       bg="#1a1a1a", fg="white",
                       insertbackground="white")
text_message.pack(pady=5)

# Generate Button
tk.Button(root,
          text="Generate MAC",
          command=generate_mac,
          bg="cyan",
          fg="black",
          font=("Arial", 11, "bold")).pack(pady=10)

# Generated MAC
tk.Label(root, text="Generated MAC", bg="black",
         fg="cyan", font=("Arial", 11)).pack()

entry_generated_mac = tk.Entry(root, width=70, state="readonly",
                               bg="#1a1a1a", fg="yellow",
                               readonlybackground="#1a1a1a")
entry_generated_mac.pack(pady=5)

# Verification Section
tk.Label(root,
         text="Verification",
         font=("Arial", 15, "bold"),
         bg="black",
         fg="cyan").pack(pady=15)

tk.Label(root, text="Received Message", bg="black",
         fg="cyan").pack()

text_verify_message = tk.Text(root, height=4, width=55,
                              bg="#1a1a1a",
                              fg="white",
                              insertbackground="white")
text_verify_message.pack(pady=5)

tk.Label(root, text="Received MAC", bg="black",
         fg="cyan").pack()

entry_verify_mac = tk.Entry(root, width=70,
                            bg="#1a1a1a",
                            fg="white",
                            insertbackground="white")
entry_verify_mac.pack(pady=5)

# Verify Button
tk.Button(root,
          text="Verify MAC",
          command=verify_mac,
          bg="cyan",
          fg="black",
          font=("Arial", 11, "bold")).pack(pady=10)

# Result Label
result_label = tk.Label(root,
                        text="",
                        font=("Arial", 12, "bold"),
                        bg="black")
result_label.pack(pady=10)

root.mainloop()
