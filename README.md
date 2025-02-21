# Shamir's Secret Sharing in Python

This repository demonstrates a simple implementation of **Shamir’s Secret Sharing** (SSS) using the [**galois** Python library](https://github.com/mhostetter/galois). You can generate shares for a secret and then reconstruct the secret from those shares using polynomial interpolation over a finite field.

## Table of Contents
- [Overview](#overview)
- [Key Components](#key-components)
- [Setup and Installation](#setup-and-installation)
- [How to Run](#how-to-run)
- [Usage Examples](#usage-examples)
- [Explanation of Core Functions](#explanation-of-core-functions)
- [License](#license)

---

## Overview

1. **Shamir's Secret Sharing** divides a secret \( s \) into \( n \) parts (shares).  
2. Only \( k \) of those shares are required to reconstruct the original secret.  
3. This approach uses polynomial interpolation in a finite field of size \( p \) (where \( p \) is prime).  

In this repo:
- **`share(n, k, s)`**: Generates \( n \) shares (each share is a point \((x_i, y_i)\)) from a secret \( s \) such that any \( k \) of these shares can reconstruct the secret.
- **`reconstruct(points, k, n, field)`**: Given \( k \) shares, performs Lagrange interpolation at \( x = 0 \) to recover the secret \( s \).

---

## Key Components

- **`shamir.py`** (or `secret.py`, depending on how you organize): Contains the main logic for:
  - Generating shares (`share` function).
  - Checking or finding prime fields (optional).
  - Helper utilities (e.g., next prime, replacing polynomial coefficients).
- **`reconstruct` functions**: Illustrate how to rebuild the secret from \( k \) points using [Lagrange interpolation](https://en.wikipedia.org/wiki/Lagrange_polynomial).

---

## Setup and Installation

1. **Clone** the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   cd YOUR_REPO_NAME
   ```
2. **Install Python 3.8+** (recommended).
3. **Install dependencies**:
   ```bash
   pip install galois
   ```
   Or, if you have a `requirements.txt`, then:
   ```bash
   pip install -r requirements.txt
   ```

---

## How to Run

1. **Run the Shamir demo** from the command line:
   ```bash
   python shamir.py
   ```
   This will print out:
   - The random polynomial constructed.
   - The shares distributed \((x_i, y_i)\).
   - A reconstructed secret example (if provided in the script).

2. **Or use the `secret.py` reconstruction** from your own script:
   ```bash
   python secret.py
   ```
   - It demonstrates how to manually call `reconstruct(...)` with a set of shares.

---

## Usage Examples

### 1) Generate and Reconstruct

In `shamir.py` (or wherever you place the code):

```python
from shamir import share, reconstruct

# Generate shares for secret = 42
n = 5   # total parts
k = 3   # threshold needed to reconstruct
s = 42  # secret

y_values, k, n, field = share(n, k, s)
# y_values are [(x1,y1), (x2,y2), ..., (xn,yn)]

# Reconstruct using first k shares
points = y_values[:k]  # e.g., just take the first 3 shares
secret = reconstruct(points, k, n, field)
print("Reconstructed secret:", secret)  # should print 42
```

### 2) Using `secret.py` Directly

```bash
python secret.py
```
- The script runs an example with hardcoded points/shares, calls `reconstruct()`, and prints `f(0)` (the secret).

---

## Explanation of Core Functions

### `share(n, k, s)`
1. **Parameters**:
   - `n` (int): total number of parts (shares).
   - `k` (int): threshold number of parts needed to reconstruct.
   - `s` (int): the secret to be shared.
2. **Process**:
   - Validates `n >= k`.
   - Picks a prime field \( p \) (e.g., 1009) and creates a Galois Field `GF(p)`.
   - Creates a random polynomial of degree \( k - 1 \) in that field.
   - Adjusts polynomial so that `f(0) = s`.
   - Computes \( f(1), f(2), \ldots, f(n) \), returning all \((x_i, y_i)\) pairs.
3. **Returns**:
   - `y_values`: The list of \((x_i, y_i)\) shares.
   - `k, n, field`: For convenience in reconstruction.

### `reconstruct(points, k, n, field)`
1. **Parameters**:
   - `points` (list of tuples): The \((x, y)\) shares.
   - `k, n, field`: Threshold, total parts, and prime field.
2. **Process**:
   - Ensures we only use the first `k` points.
   - Performs **Lagrange interpolation** at `x=0`:
     \[
        s = \sum_{i=1}^{k} \left( y_i \times \prod_{j=1, j\neq i}^{k} \frac{x - x_j}{x_i - x_j} \right) \bmod p
     \]
     where \( x = 0 \).
   - The result is the secret `s`.
3. **Returns**: The **reconstructed secret** as an integer in `[0, p-1]`.

---

## License

(Choose a license—e.g., [MIT License](https://opensource.org/licenses/MIT)—and include its text if you wish. Below is an example MIT snippet.)

```
MIT License

Copyright (c) 2025 ...

Permission is hereby granted, free of charge, to any person obtaining a copy
...
```

---

Feel free to extend this Shamir’s Secret Sharing implementation for multi-party protocols, threshold cryptography, or secret distribution in production systems. For any questions, open an issue or create a pull request! 

Enjoy experimenting with **Shamir’s Secret Sharing**!
