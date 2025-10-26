import hmac
import hashlib

# 1. Define the secret key, the message, and the hash algorithm
secret_key = b'my_super_secret_key' 
message = b'This is the data to be authenticated.'
# SHA-256 is a common and strong choice
hash_algorithm = hashlib.sha256 

# 2. HMAC Generation (The Sender's Side)

# Create an HMAC object
# hmac.new(key, msg=None, digestmod)
hmac_generator = hmac.new(
    key=secret_key, 
    msg=message, 
    digestmod=hash_algorithm
)

# Generate the MAC (Message Authentication Code)
# .hexdigest() returns the MAC as a hexadecimal string
generated_mac = hmac_generator.hexdigest()

print(f"--- HMAC Generation ---")
print(f"Key used: {secret_key.decode()}")
print(f"Message: {message.decode()}")
print(f"Algorithm: {hash_algorithm.__name__.upper()}")
print(f"Generated HMAC (MAC): {generated_mac}")

print("-" * 35)

# 3. HMAC Verification (The Receiver's Side)

# a) Calculate the MAC for the received message
# In a real scenario, 'message' would be the received data, and 'secret_key' 
# would be known only to the sender/receiver.
hmac_verifier = hmac.new(
    key=secret_key, 
    msg=message, # Use the *received* message
    digestmod=hash_algorithm
)
calculated_mac = hmac_verifier.hexdigest()

print(f"--- HMAC Verification ---")
print(f"Calculated MAC (Receiver): {calculated_mac}")
print(f"Received MAC (Sender):     {generated_mac}")

# b) Compare the two MACs securely using hmac.compare_digest()
# This function is used to prevent **timing attacks**
is_verified = hmac.compare_digest(generated_mac, calculated_mac)

print(f"\nVerification Result: {'SUCCESS' if is_verified else 'FAILURE'}")

print("-" * 35)

# 4. Demonstration of Tampering (Verification Fails)

print(f"--- Demonstration of Tampering ---")
tampered_message = b'This is the data to be authenticated. (TAMPERED)'

# Calculate the MAC for the tampered message
hmac_tampered = hmac.new(
    key=secret_key, 
    msg=tampered_message, 
    digestmod=hash_algorithm
)
tampered_calculated_mac = hmac_tampered.hexdigest()

# Compare the original MAC with the MAC of the tampered message
is_tampered_verified = hmac.compare_digest(generated_mac, tampered_calculated_mac)

print(f"Tampered Message MAC:  {tampered_calculated_mac}")
print(f"Original Sent MAC:     {generated_mac}")
print(f"\nVerification Result with Tampered Message: {'SUCCESS' if is_tampered_verified else 'FAILURE'}")
