#!/usr/bin/env python3
"""
Caesar Cipher Lab
-----------------
This script implements the classical Caesar cipher for educational purposes.

Note:
- This is an improved version with documentation and additional features.
Features:
- Encrypt and decrypt text using a given key
- Handles uppercase, lowercase, and non-alphabet characters
- Command-line interface with argparse
"""

import argparse

def encrypt(text: str, key: int) -> str:
    """
    Encrypts text using Caesar cipher with the given key.
    
    Parameters:
        text (str): The input plaintext
        key (int): Shift key (number of positions)
    
    Returns:
        str: Encrypted ciphertext
    """
    result = []
    for char in text:
        if char.isupper():
            result.append(chr((ord(char) - 65 + key) % 26 + 65))
        elif char.islower():
            result.append(chr((ord(char) - 97 + key) % 26 + 97))
        else:
            result.append(char)
    return ''.join(result)

def decrypt(cipher: str, key: int) -> str:
    """
    Decrypts text using Caesar cipher with the given key.
    
    Parameters:
        cipher (str): The encrypted ciphertext
        key (int): Shift key (number of positions)
    
    Returns:
        str: Decrypted plaintext
    """
    return encrypt(cipher, -key)

def main():
    parser = argparse.ArgumentParser(description="Caesar Cipher Lab Exercise")
    parser.add_argument("mode", choices=["encrypt", "decrypt"], help="Mode: encrypt or decrypt")
    parser.add_argument("text", help="Text to encrypt/decrypt (use quotes for spaces)")
    parser.add_argument("key", type=int, help="Shift key (integer)")

    args = parser.parse_args()

    if args.mode == "encrypt":
        result = encrypt(args.text, args.key)
        print(f"Encrypted Text: {result}")
    else:
        result = decrypt(args.text, args.key)
        print(f"Decrypted Text: {result}")

if __name__ == "__main__":
    main()
####################################
# Example usage:
# To encrypt: python Caesar_Improved.py encrypt "Hello, World!" 3
# Output: "Khoor, Zruog!"
# To decrypt: python Caesar_Improved.py decrypt "Khoor, Zruog!" 3
# Output: "Hello, World!"
####################################
