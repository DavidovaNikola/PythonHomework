"""
Substitution Cipher Library

A Python library for encrypting and decrypting messages using substitution ciphers.
Uses the alphabet: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_' (underscore replaces spaces).
"""

def substitute_encrypt(plaintext, key):
    """
    Encrypt a message using a substitution cipher.
    
    Args:
        plaintext (str): The message to encrypt
        key (str): A 27-character string representing the substitution key.
                  Must contain each character from 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_' exactly once.
    
    Returns:
        str: The encrypted message
        
    Raises:
        ValueError: If the key is invalid (wrong length or missing characters)
    """
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_'
    
    # Validate the key
    if len(key) != 27:
        raise ValueError("Key must be exactly 27 characters long")
    
    if set(key.upper()) != set(alphabet):
        raise ValueError("Key must contain each character from 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_' exactly once")
    
    # Convert key to uppercase for consistency
    key = key.upper()
    
    # Create substitution mapping
    substitution_map = {}
    for i, char in enumerate(alphabet):
        substitution_map[char] = key[i]
    
    # Convert plaintext to uppercase and replace spaces with underscores
    plaintext = plaintext.upper().replace(' ', '_')
    
    # Encrypt the message
    ciphertext = ''
    for char in plaintext:
        if char in substitution_map:
            ciphertext += substitution_map[char]
        else:
            # Keep characters not in our alphabet unchanged (numbers, punctuation, etc.)
            ciphertext += char
    
    return ciphertext


def substitute_decrypt(ciphertext, key):
    """
    Decrypt a message using a substitution cipher.
    
    Args:
        ciphertext (str): The encrypted message to decrypt
        key (str): A 27-character string representing the substitution key.
                  Must contain each character from 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_' exactly once.
    
    Returns:
        str: The decrypted message (with underscores converted back to spaces)
        
    Raises:
        ValueError: If the key is invalid (wrong length or missing characters)
    """
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_'
    
    # Validate the key
    if len(key) != 27:
        raise ValueError("Key must be exactly 27 characters long")
    
    if set(key.upper()) != set(alphabet):
        raise ValueError("Key must contain each character from 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_' exactly once")
    
    # Convert key to uppercase for consistency
    key = key.upper()
    
    # Create reverse substitution mapping (from cipher to plain)
    reverse_map = {}
    for i, char in enumerate(alphabet):
        reverse_map[key[i]] = char
    
    # Convert ciphertext to uppercase
    ciphertext = ciphertext.upper()
    
    # Decrypt the message
    plaintext = ''
    for char in ciphertext:
        if char in reverse_map:
            plaintext += reverse_map[char]
        else:
            # Keep characters not in our alphabet unchanged (numbers, punctuation, etc.)
            plaintext += char
    
    # Convert underscores back to spaces for readability
    plaintext = plaintext.replace('_', ' ')
    
    return plaintext


def generate_random_key():
    """
    Generate a random substitution key by shuffling the alphabet.
    
    Returns:
        str: A random 27-character substitution key
    """
    import random
    
    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ_')
    random.shuffle(alphabet)
    return ''.join(alphabet)


def create_caesar_key(shift=3):
    """
    Create a substitution key based on Caesar cipher shift.
    
    Args:
        shift (int): Number of positions to shift (default: 3)
    
    Returns:
        str: A substitution key representing a Caesar cipher
    """
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_'
    shifted_key = ''
    
    for char in alphabet:
        # Find the position of the character
        pos = alphabet.index(char)
        # Shift by the specified amount (with wraparound)
        new_pos = (pos + shift) % len(alphabet)
        shifted_key += alphabet[new_pos]
    
    return shifted_key


# Example usage and testing
if __name__ == "__main__":
    # Example with a custom key
    custom_key = "ZYXWVUTSRQPONMLKJIHGFEDCBA_"
    message = "HELLO WORLD"
    
    print("Original message:", message)
    print("Encryption key:", custom_key)
    
    # Encrypt
    encrypted = substitute_encrypt(message, custom_key)
    print("Encrypted:", encrypted)
    
    # Decrypt
    decrypted = substitute_decrypt(encrypted, custom_key)
    print("Decrypted:", decrypted)
    
    print("\n" + "="*50 + "\n")
    
    # Example with Caesar cipher key
    caesar_key = create_caesar_key(13)  # ROT13 variant
    message2 = "THE QUICK BROWN FOX"
    
    print("Caesar key (shift 13):", caesar_key)
    print("Original message:", message2)
    
    encrypted2 = substitute_encrypt(message2, caesar_key)
    print("Encrypted:", encrypted2)
    
    decrypted2 = substitute_decrypt(encrypted2, caesar_key)
    print("Decrypted:", decrypted2)