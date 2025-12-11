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
    secret = input("Enter the Password: \n").strip()
    
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
    print("Starting brute-force attack ...")
    
    for guess in generate_guesses(charset, max_length):
        if guess == secret:
            print(f"Password guessed successfully: {guess}")
            break
    else:
        print("Password not found within the given length limit.")

if __name__ == "__main__":
    main()

################################################
# Example usage:
#Enter the password to guess for: he
#
#Trying guesses (this may take some time for longer secrets):
#
#a b c d e f g h i j k l m n o p q r s t u v w x y z aa ab ac ad ae af ag ah ai aj ak al am an ao ap aq ar as at au av aw ax ay az ba bb bc bd be bf bg bh bi bj bk bl bm bn bo bp bq br bs bt bu bv bw bx by bz ca cb cc cd ce cf cg ch ci cj ck cl cm cn co cp cq cr cs ct cu cv cw cx cy cz da db dc dd de df dg dh di dj dk dl dm dn do dp dq dr ds dt du dv dw dx dy dz ea eb ec ed ee ef eg eh ei ej ek el em en eo ep eq er es et eu ev ew ex ey ez fa fb fc fd fe ff fg fh fi fj fk fl fm fn fo fp fq fr fs ft fu fv fw fx fy fz ga gb gc gd ge gf gg gh gi gj gk gl gm gn go gp gq gr gs gt gu gv gw gx gy gz ha hb hc hd he
#
#
#Password found: he
################################################