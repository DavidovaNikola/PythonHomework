import os

def save_decrypted_output(text, key, sample_id, length, output_dir="output"):
    """
    Save decrypted text and corresponding key to separate files.
    
    Args:
        text (str): The decrypted plaintext to save
        key (str): The encryption key to save
        sample_id (int/str): Sample identifier for the filename
        length (int/str): Length identifier for the filename
        output_dir (str): Directory to save files in (default: "output")
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate filenames
    text_filename = f"text_{length}_sample_{sample_id}_plaintext.txt"
    key_filename = f"text_{length}_sample_{sample_id}_key.txt"
    
    # Full file paths
    text_path = os.path.join(output_dir, text_filename)
    key_path = os.path.join(output_dir, key_filename)
    
    # Save the decrypted text
    with open(text_path, 'w', encoding='utf-8') as f:
        f.write(text)
    
    # Save the key
    with open(key_path, 'w', encoding='utf-8') as f:
        f.write(str(key))
    
    print(f"Saved decrypted text to: {text_path}")
    print(f"Saved key to: {key_path}")