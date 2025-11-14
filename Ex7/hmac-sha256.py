import hmac, hashlib

def generate_hmac(key, msg):
    return hmac.new(key.encode(), msg.encode(), hashlib.sha256).hexdigest()

key = input("Secret key: ")
msg = input("Message: ")
mac = generate_hmac(key, msg)

print("\n--- HMAC Generation ---")
print(f"Key: {key}\nMessage: {msg}\nHMAC: {mac}\n" + "-"*35)

print("--- HMAC Verification ---")
verified_mac = generate_hmac(key, msg)
print(f"Verified MAC: {verified_mac}\nMatch: {'SUCCESS' if hmac.compare_digest(mac, verified_mac) else 'FAILURE'}\n" + "-"*35)

tampered_msg = input("Tampered message: ")
tampered_mac = generate_hmac(key, tampered_msg)

print("--- Tampering Check ---")
print(f"Tampered MAC: {tampered_mac}\nMatch: {'SUCCESS' if hmac.compare_digest(mac, tampered_mac) else 'FAILURE'}")
###############################################
# Example Output:
#Secret key: hui
#Message: hello
#
#--- HMAC Generation ---
#Key: hui
#Message: hello
#HMAC: 0e5f5ad5768152f90569807b24b3e3522a24104b53e3b087cc9705448117f1e0
#-----------------------------------
#--- HMAC Verification ---
#Verified MAC: 0e5f5ad5768152f90569807b24b3e3522a24104b53e3b087cc9705448117f1e0
#Match: SUCCESS
#-----------------------------------
#Tampered message: hello
#--- Tampering Check ---
#Tampered MAC: 0e5f5ad5768152f90569807b24b3e3522a24104b53e3b087cc9705448117f1e0
#Match: SUCCESS
#############################################