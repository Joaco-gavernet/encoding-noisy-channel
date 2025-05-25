import numpy as np

# Perform polynomial division in GF(2)
def polynomial_division(dividend, divisor):
    # Convert to numpy arrays if not already
    dividend = np.array(dividend, dtype=int)
    divisor = np.array(divisor, dtype=int)
    
    # Initialize remainder as dividend
    remainder = dividend.copy()
    
    # Get the degree of divisor
    divisor_degree = len(divisor) - 1
    
    # Perform division
    for i in range(len(dividend) - divisor_degree):
        if remainder[i] == 1:
            remainder[i:i + len(divisor)] ^= divisor
    
    # Return the remainder (last divisor_degree elements)
    return remainder[-divisor_degree:]

# Perform polynomial multiplication in GF(2)
def multiply_gf2(poly1, poly2):
    result_degree = len(poly1) + len(poly2) - 1
    result = np.zeros(result_degree, dtype=int)
    
    for i, coeff1 in enumerate(poly1):
        if coeff1 == 1:  # Only multiply if coefficient is 1
            for j, coeff2 in enumerate(poly2):
                if coeff2 == 1:  # Only multiply if coefficient is 1
                    result[i + j] ^= 1  # XOR with 1 is equivalent to flipping the bit
    
    return result