# Import required libraries
import sys
sys.path.append('..')

from src.channel import *
from src.huffman import *
from src.matrix import *
from src.poly_ops import *

module_path = os.path.abspath(os.path.join('.'))
if module_path not in sys.path:
    sys.path.append(module_path)


# Global variables
# Parameters
n = 14  # codeword length
k = 10   # source word length

# Proposed parity matrix
P = np.matrix([[1, 1, 0, 0],
     [0, 1, 1, 0],
     [0, 0, 1, 1],
     [1, 0, 0, 1],
     [1, 1, 1, 0],
     [0, 1, 1, 1],
     [1, 0, 1, 1],
     [1, 1, 0, 1],
     [1, 1, 1, 1],
     [1, 0, 1, 0]], dtype=np.int64)
G = np.hstack((np.eye(k), P))
H = np.hstack((P.T, np.eye(n-k)))
tc = 1
td = 2
dmin = 3

# Choose power of extended source S^x
x = 2
max_retransmissions = 100 # Set to prevent infinite loops


print("Notebook own setup done.") 