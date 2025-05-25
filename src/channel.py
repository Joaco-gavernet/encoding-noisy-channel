import numpy as np
from itertools import combinations

def noisy_channel(v, A=1, n=14, k=10, EbfN0=10):
    Es = A**2
    Ebf = Es*n/k
    s = (2*v - 1)*A
    N0 = Ebf/EbfN0
    noise = np.sqrt(N0/2) * (np.random.randn(1, n) + 1j * np.random.randn(1, n))
    r = s + noise
    vr = 1 * (np.real(r) > 0)
    return vr 

def generate_error_patterns(max_weight, n):
    patterns = []
    for weight in range(1, max_weight + 1):
        for positions in combinations(range(n), weight):
            pattern = np.zeros((1, n), dtype=int)
            pattern[0, list(positions)] = 1
            patterns.append(pattern)
    return patterns

def encode_message(message, G):
    return np.dot(message, G) % 2

def any_error(message, H):
    syndrome = np.dot(message, H.T) % 2
    return np.any(syndrome)

def decode_message(received_codeword, H, n):
    syndrome = np.dot(received_codeword, H.T) % 2
    
    if not np.any(syndrome):
        return received_codeword
    
    # Try to find matching error pattern, convert syndrome to decimal for lookup
    syndrome_decimal = str(syndrome[0].astype(int).tolist())

    # Check if syndrome matches any single-bit error pattern
    for i in range(n):  # Use shape[1] for column length
        error_pattern = np.zeros((1, n), dtype=int)
        error_pattern[0, i] = 1
        error_syndrome = np.dot(error_pattern, H.T) % 2
        error_syndrome_decimal = str(error_syndrome.astype(int).tolist())

        if error_syndrome_decimal == syndrome_decimal:
            # Correct the error by flipping the bit
            corrected_codeword = received_codeword.copy()
            corrected_codeword[0, i] ^= 1
            return corrected_codeword

    # If no matching error pattern found, return original codeword
    return received_codeword