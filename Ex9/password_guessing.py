import itertools
import string

def generate_guesses(charset, max_length):
    """
    Generate all strings over the given charset
    from length 1 up to max_length.
    """
    for length in range(1, max_length + 1):
        for combo in itertools.product(charset, repeat=length):
            yield "".join(combo)

def main():
    secret = input("Enter the password to guess for: ").strip()
    
    if not secret:
        print("Secret password cannot be empty.")
        return
    
    # Character set to use for guesses.
    # You can change this as needed, e.g.:
    # charset = string.ascii_lowercase + string.digits
    charset = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
    
    # Check that the secret uses only characters from our charset
    for ch in secret:
        if ch not in charset:
            print(f"Error: character '{ch}' in secret is not in the allowed charset.")
            print(f"Allowed characters are: {charset}")
            return

    max_length = len(secret)
    print("\nTrying guesses (this may take some time for longer secrets):\n")
    
    found = False
    for guess in generate_guesses(charset, max_length):
        # Print guesses space-separated
        print(guess, end=" ")
        
        if guess == secret:
            found = True
            print(f"\n\nPassword found: {guess}")
            break

    if not found:
        print("\n\nPassword not found within the given length limit.")

if __name__ == "__main__":
    main()
