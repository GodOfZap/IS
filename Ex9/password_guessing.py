import itertools
import string

def generate_guesses(charset, max_length):
    """
    Generate all possible strings using the given charset,
    starting from length 1 up to max_length.
    """
    for length in range(1, max_length + 1):
        for combo in itertools.product(charset, repeat=length):
            yield "".join(combo)

def main():
    secret = input("Enter the password to guess through brute-force: ").strip()
    
    if not secret:
        print("Password cannot be empty. Please try again.")
        return
    
    # Define the character set (you can expand this if needed)
    charset = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
    
    # Validate that the secret only uses allowed characters
    if any(ch not in charset for ch in secret):
        print(f"Error: Your password contains unsupported characters.")
        print(f"Allowed characters are: {charset}")
        return

    max_length = len(secret)
    print(f"\nStarting guesses (this may take time for longer passwords)...\n")
    
    for guess in generate_guesses(charset, max_length):
        print(guess, end=" ", flush=True)  # flush ensures smooth printing
        
        if guess == secret:
            print(f"\n\nPassword found: {guess}")
            break
    else:
        print("\n\nPassword not found within the given length limit.")

if __name__ == "__main__":
    main()
