import hmac
import hashlib

# User enters the secret key
secret_key = input("Enter Secret Key: ").encode()

# User enters the message
message = input("Enter Message: ").encode()

# Generate MAC
mac = hmac.new(secret_key, message, hashlib.sha256).hexdigest()

print("\nGenerated MAC:", mac)

# ---------------- Verification ----------------

print("\n----- Verify Message -----")

received_message = input("Enter Received Message: ").encode()
received_mac = input("Enter Received MAC: ")

# Generate MAC again
new_mac = hmac.new(secret_key, received_message, hashlib.sha256).hexdigest()

# Verify MAC
if hmac.compare_digest(received_mac, new_mac):
    print("\n MAC Verification Successful!")
    print("Message is Authentic and Integrity is Maintained.")
else:
    print("\n MAC Verification Failed!")
    print("Message has been Modified or Authentication Failed.")
