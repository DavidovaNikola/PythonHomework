import random
import math

def prolom_substitute(text, TM_ref, iter=20000, start_key=None):
    """
    Uses the Metropolis-Hastings algorithm to find the most likely key to decrypt a substitution cipher.
    
    Args:
        text (str): The ciphertext to decrypt
        TM_ref: Reference object containing the plausibility function
        iter (int): Number of iterations to run (default: 20000)
        start_key (str): Starting key for decryption (default: None, uses random key)
    
    Returns:
        tuple: (best_key, decrypted_text) - the best key found and corresponding plaintext
    """
    
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_'
    
    # Initialize the key
    if start_key is None:
        # Create a random permutation of the alphabet as starting key
        key_list = list(alphabet)
        random.shuffle(key_list)
        current_key = ''.join(key_list)
    else:
        current_key = start_key
    
    # Decrypt text with current key
    def decrypt_with_key(ciphertext, key):
        """Decrypt ciphertext using the given substitution key"""
        decryption_map = {}
        for i, char in enumerate(alphabet):
            decryption_map[char] = key[i]
        
        decrypted = ''
        for char in ciphertext:
            if char in decryption_map:
                decrypted += decryption_map[char]
            else:
                decrypted += char  # Keep non-alphabet characters as is
        
        return decrypted
    
    # Get initial decryption and plausibility
    current_decryption = decrypt_with_key(text, current_key)
    current_plausibility = plausibility(current_decryption, TM_ref)
    
    # Keep track of the best solution found
    best_key = current_key
    best_decryption = current_decryption
    best_plausibility = current_plausibility
    
    # Metropolis-Hastings iterations
    for iteration in range(iter):
        # Create a new key by swapping two random characters
        new_key = list(current_key)
        
        # Select two random positions to swap
        pos1 = random.randint(0, len(alphabet) - 1)
        pos2 = random.randint(0, len(alphabet) - 1)
        
        # Ensure we're swapping different positions
        while pos1 == pos2:
            pos2 = random.randint(0, len(alphabet) - 1)
        
        # Swap the characters
        new_key[pos1], new_key[pos2] = new_key[pos2], new_key[pos1]
        new_key_str = ''.join(new_key)
        
        # Decrypt with the new key
        new_decryption = decrypt_with_key(text, new_key_str)
        new_plausibility = plausibility(new_decryption, TM_ref)
        
        # Update best solution if this is better
        if new_plausibility > best_plausibility:
            best_key = new_key_str
            best_decryption = new_decryption
            best_plausibility = new_plausibility
        
        # Metropolis-Hastings acceptance criterion
        # Accept if new solution is better, or with probability based on difference
        if new_plausibility >= current_plausibility:
            # Accept the new solution
            current_key = new_key_str
            current_decryption = new_decryption
            current_plausibility = new_plausibility
        else:
            # Accept with probability based on the difference in plausibility
            # Using a temperature-like parameter to control acceptance
            temperature = 1.0  # You might want to implement cooling schedule
            probability = math.exp((new_plausibility - current_plausibility) / temperature)
            
            if random.random() < probability:
                current_key = new_key_str
                current_decryption = new_decryption
                current_plausibility = new_plausibility
        
        # Optional: Print progress every 1000 iterations
        if (iteration + 1) % 1000 == 0:
            print(f"Iteration {iteration + 1}: Best plausibility = {best_plausibility:.6f}")
    
    return best_key, best_decryption


def plausibility(text, TM_ref):
    """
    Placeholder plausibility function. This should be replaced with your actual implementation.
    
    Args:
        text (str): The text to evaluate
        TM_ref: Reference object for computing plausibility
    
    Returns:
        float: Plausibility score (higher is better)
    """
    # This is a placeholder - replace with your actual plausibility function
    # For now, return a simple score based on common English patterns
    
    # Simple heuristic: count common English patterns
    score = 0.0
    
    # Common English words
    common_words = ['THE', 'AND', 'TO', 'OF', 'A', 'IN', 'IS', 'IT', 'YOU', 'THAT']
    for word in common_words:
        score += text.count(word) * len(word)
    
    # Penalize unusual character sequences
    unusual_pairs = ['QX', 'QZ', 'JX', 'JZ', 'ZX']
    for pair in unusual_pairs:
        score -= text.count(pair) * 5
    
    return score