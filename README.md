# Noisy Channel Simulation

This project simulates transmission through a noisy channel using BPSK modulation. It provides tools for analyzing channel performance and error rates under different signal-to-noise ratio conditions.

## Project Structure

```
.
├── src/                    # Source code directory
│   └── channel.py         # Channel simulation module
├── notebooks/             # Jupyter notebooks
│   └── channel_simulation.ipynb  # Example usage and analysis
└── README.md             # This file
```

## Setup

1. Make sure you have Python 3.x installed
2. Install required packages:
   ```bash
   pip install numpy jupyter
   ```

## Usage

1. Open the Jupyter notebook:
   ```bash
   jupyter notebook notebooks/channel_simulation.ipynb
   ```

2. The notebook contains examples of:
   - Basic channel simulation
   - Error rate analysis with different SNR values

## Module Documentation

The main functionality is in `src/channel.py`, which provides the `noisy_channel()` function for simulating BPSK transmission through a noisy channel.

### Parameters:
- `v`: Input codeword (row vector)
- `A`: BPSK signal amplitude (default: 1)
- `n`: Codeword length (default: 10)
- `k`: Source word length (default: 5)
- `EbfN0`: Desired source bit energy to noise spectral density ratio (default: 10)

### Returns:
- `vr`: Demodulated codeword (hard detection) 