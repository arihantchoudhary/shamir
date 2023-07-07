def reconstruct(y_values, x):
    """
    y_values: parts of secret s
    x: the point at which to evaluate the reconstructed polynomial. By default, the secret is stored at x = 0;
    """
    n = len(y_values)
    result = 0.0

    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if i != j:
                term *= (x - j) / (i - j)
        result += term

    return result

# Example usage
# Suppose we have 4 points: (1, 2), (2, 3), (3, 5), (4, 9)
x_values = [1, 2, 3, 4]
y_values = [2, 3, 5, 9]
# find f(0)
result = reconstruct(y_values, 0)
print("f(0) =", result)

from pyfinite import ffield

    
    
        

    
    
    
    
    


