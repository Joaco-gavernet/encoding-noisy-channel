from notebooks.general_utils import *

def generate_error_patterns(max_weight, n):
    patterns = []
    for weight in range(1, max_weight + 1):
        for positions in combinations(range(n), weight):
            pattern = np.zeros((1, n), dtype=int)
            pattern[0, list(positions)] = 1
            patterns.append(pattern)
    return patterns

def noisy_channel(v, A=1, n=14, k=10, EbfN0=10):
    Es = A**2
    Ebf = Es*n/k
    s = (2*v - 1)*A
    N0 = Ebf/EbfN0
    noise = np.sqrt(N0/2) * (np.random.randn(*v.shape) + 1j * np.random.randn(*v.shape))
    r = s + noise
    vr = 1 * (np.real(r) > 0)
    return vr

def encode_message(message, G):
    return np.dot(message, G) % 2

def any_error(message, H):
    syndrome = np.dot(message, H.T) % 2
    return np.any(syndrome)

def decode_message(received_codewords, H, n):
    # Ensure received_codewords is 2D and has the correct shape
    if received_codewords.ndim == 1:
        received_codewords = received_codewords.reshape(1, -1)
    
    # Ensure the shape is correct
    if received_codewords.shape[1] != n:
        received_codewords = received_codewords.reshape(-1, n)
    
    # Calculate syndromes for all codewords at once
    syndromes = np.dot(received_codewords, H.T) % 2
    corrected_codewords = received_codewords.copy()
    
    # For each codeword in the batch
    for i in range(received_codewords.shape[0]):
        syndrome = syndromes[i:i+1]
        
        if not np.any(syndrome):
            continue
            
        # Try to find matching error pattern
        syndrome_decimal = str(syndrome[0].astype(int).tolist())
        
        # Check if syndrome matches any single-bit error pattern
        for j in range(n):
            error_pattern = np.zeros((1, n), dtype=int)
            error_pattern[0, j] = 1
            error_syndrome = np.dot(error_pattern, H.T) % 2
            error_syndrome_decimal = str(error_syndrome.astype(int).tolist())
            
            if error_syndrome_decimal == syndrome_decimal:
                # Correct the error by flipping the bit
                if i < corrected_codewords.shape[0] and j < corrected_codewords.shape[1]:
                    corrected_codewords[i, j] ^= 1
                break
                
    return corrected_codewords

def detect_message(received_codewords, H, n): 
    # Calculate syndromes for all codewords at once
    syndromes = np.dot(received_codewords, H.T) % 2
    corrected_codewords = received_codewords.copy()
    
    # For each codeword in the batch
    for i in range(received_codewords.shape[0]):
        syndrome = syndromes[i:i+1]
        
        if np.any(syndrome):
            corrected_codewords[i] = np.zeros(n, dtype=int)
                
    return corrected_codewords