import hmac
import hashlib

# 1. Define the secret key and message as inputs, encode them to bytes
secret_key_input = input("Enter the secret key: ")
message_input = input("Enter the message: ")

secret_key = secret_key_input.encode()
message = message_input.encode()

# SHA-256 is a common and strong choice
hash_algorithm = hashlib.sha256

# 2. HMAC Generation (The Sender's Side)

# Create an HMAC object
hmac_generator = hmac.new(
    key=secret_key,
    msg=message,
    digestmod=hash_algorithm
)

# Generate the MAC (Message Authentication Code)
generated_mac = hmac_generator.hexdigest()

print(f"--- HMAC Generation ---")
print(f"Key used: {secret_key.decode()}")
print(f"Message: {message.decode()}")
print(f"Algorithm: {hash_algorithm.__name__.upper()}")
print(f"Generated HMAC (MAC): {generated_mac}")

print("-" * 35)

# 3. HMAC Verification (The Receiver's Side)

# a) Calculate the MAC for the received message
hmac_verifier = hmac.new(
    key=secret_key,
    msg=message,
    digestmod=hash_algorithm
)
calculated_mac = hmac_verifier.hexdigest()

print(f"--- HMAC Verification ---")
print(f"Calculated MAC (Receiver): {calculated_mac}")
print(f"Received MAC (Sender):     {generated_mac}")

# b) Compare the two MACs securely
is_verified = hmac.compare_digest(generated_mac, calculated_mac)

print(f"\nVerification Result: {'SUCCESS' if is_verified else 'FAILURE'}")

print("-" * 35)

# 4. Demonstration of Tampering (Verification Fails)

print(f"--- Demonstration of Tampering ---")
tampered_message_str = input("Enter a tampered message: ")
tampered_message = tampered_message_str.encode()

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

#################################################
#Example Usage:
#Enter the secret key: ello
#Enter the message: hui
#--- HMAC Generation ---
#Key used: ello
#Message: hui
#Algorithm: OPENSSL_SHA256
#Generated HMAC (MAC): 8e6de3af27da1d2c900973ae32a7cf0dc7f84075fa59f8066bd92d853d8ff9aa
#-----------------------------------
#--- HMAC Verification ---
#Calculated MAC (Receiver): 8e6de3af27da1d2c900973ae32a7cf0dc7f84075fa59f8066bd92d853d8ff9aa
#Received MAC (Sender):     8e6de3af27da1d2c900973ae32a7cf0dc7f84075fa59f8066bd92d853d8ff9aa
#
#Verification Result: SUCCESS
#-----------------------------------
#--- Demonstration of Tampering ---
#Enter a tampered message: hui
#Tampered Message MAC:  8e6de3af27da1d2c900973ae32a7cf0dc7f84075fa59f8066bd92d853d8ff9aa
#Original Sent MAC:     8e6de3af27da1d2c900973ae32a7cf0dc7f84075fa59f8066bd92d853d8ff9aa
#
#Verification Result with Tampered Message: SUCCESS
#################################################
