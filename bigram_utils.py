"""
Bigram analysis utilities for text processing.

This module provides functions for extracting bigrams from text,
creating transition matrices, and calculating text plausibility
based on bigram frequencies.
"""

import math
from collections import defaultdict, Counter
from typing import List, Dict, Tuple


def get_bigrams(text: str) -> List[str]:
    """
    Returns a list of all consecutive 2-character sequences (bigrams) in the text.
    
    Args:
        text (str): Input text to extract bigrams from
        
    Returns:
        List[str]: List of bigram strings
        
    Example:
        >>> get_bigrams("HELLO")
        ['HE', 'EL', 'LL', 'LO']
    """
    if len(text) < 2:
        return []
    
    bigrams = []
    for i in range(len(text) - 1):
        bigrams.append(text[i:i+2])
    
    return bigrams


def transition_matrix(bigrams: List[str]) -> Dict[str, Dict[str, float]]:
    """
    Creates a relative bigram frequency matrix using the alphabet 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_'.
    
    Args:
        bigrams (List[str]): List of bigram strings
        
    Returns:
        Dict[str, Dict[str, float]]: Nested dictionary representing transition matrix
                                   where TM[first_char][second_char] = relative_frequency
                                   
    Example:
        >>> bigrams = ['AB', 'BC', 'AB']
        >>> tm = transition_matrix(bigrams)
        >>> tm['A']['B']  # Relative frequency of 'B' following 'A'
        1.0
    """
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_'
    
    # Initialize transition matrix with zeros
    TM = {}
    for char1 in alphabet:
        TM[char1] = {}
        for char2 in alphabet:
            TM[char1][char2] = 0.0
    
    # Count bigram occurrences
    bigram_counts = Counter(bigrams)
    
    # Count occurrences of each first character
    first_char_counts = defaultdict(int)
    for bigram in bigrams:
        if len(bigram) >= 2:
            first_char = bigram[0]
            if first_char in alphabet:
                first_char_counts[first_char] += 1
    
    # Calculate relative frequencies
    for bigram, count in bigram_counts.items():
        if len(bigram) >= 2:
            first_char, second_char = bigram[0], bigram[1]
            if first_char in alphabet and second_char in alphabet:
                if first_char_counts[first_char] > 0:
                    TM[first_char][second_char] = count / first_char_counts[first_char]
    
    return TM


def plausibility(text: str, TM_ref: Dict[str, Dict[str, float]]) -> float:
    """
    Calculates the log-likelihood of a text using a reference bigram matrix TM_ref.
    
    Args:
        text (str): Input text to analyze
        TM_ref (Dict[str, Dict[str, float]]): Reference transition matrix
        
    Returns:
        float: Log-likelihood of the text based on bigram probabilities
               Returns negative infinity if any bigram has zero probability
               
    Example:
        >>> text = "HELLO"
        >>> log_likelihood = plausibility(text, reference_matrix)
        >>> print(log_likelihood)
        -5.298317366548036
    """
    if len(text) < 2:
        return 0.0
    
    log_likelihood = 0.0
    bigrams = get_bigrams(text)
    
    for bigram in bigrams:
        if len(bigram) >= 2:
            first_char, second_char = bigram[0], bigram[1]
            
            # Check if characters are in the reference matrix
            if first_char in TM_ref and second_char in TM_ref[first_char]:
                probability = TM_ref[first_char][second_char]
                
                if probability > 0:
                    log_likelihood += math.log(probability)
                else:
                    # Zero probability means this bigram is impossible
                    return float('-inf')
            else:
                # Character not in reference matrix
                return float('-inf')
    
    return log_likelihood


# Example usage and testing functions (optional)
if __name__ == "__main__":
    # Example usage
    sample_text = "HELLO_WORLD"
    
    # Get bigrams
    bigrams = get_bigrams(sample_text)
    print(f"Bigrams from '{sample_text}': {bigrams}")
    
    # Create transition matrix
    tm = transition_matrix(bigrams)
    print(f"\nTransition matrix created with {len(tm)} first characters")
    
    # Calculate plausibility
    plaus = plausibility(sample_text, tm)
    print(f"Plausibility of '{sample_text}': {plaus}")