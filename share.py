import galois
import re

def share(n, k, s):
    '''
    Share a secret using Shamir's Secret Sharing scheme.
    
    n: Total number of parties
    k: Number of parts needed to reconstruct the k-1 degree polynomial
    s: Secret to be shared
    '''
    # n needs to be greater than or equal to k for this to work
    assert n >= k

    print("Secret:", s)
    print("Number of Parties:", n)
    print("Number of k shares needed to rebuild:", k)

    # n needs to be a prime number to be a field
    copy = n
    n = next_prime(n)  # function to set n to the first prime greater than n
    GF = galois.GF(n)  # GF is a field of size n
    print("Prime Field: ", n)

    # creating a polynomial of size (k-1)
    equation = galois.Poly.Random((k-1), field=GF)
    print("Before:", str(equation))
    equation = equation - equation(0) + GF(s);

    # add secret to equation
    # replaced_eq = replace_coefficient(str(equation), s)
    # equation = galois.Poly.Str(replaced_eq, field=GF)
    print("After:", str(equation))
   
    # Computing {y1, y2, ... yn} 
    y_values = []
    for i in range(copy):
        temp = equation(i)
        y_values.append(temp)

    print("Y values given out", y_values)
    return y_values

def is_prime(num):
    '''
    Checks if a number is prime.
    '''
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def next_prime(n):
    '''
    Finds the next prime number greater than n.
    '''
    next_num = n + 1
    while True:
        if is_prime(next_num):
            return next_num
        next_num += 1
        
def replace_coefficient(string, s):
    terms = re.split(r'\+|\-', string)
    new_terms = []
    for term in terms:
        term = term.strip()
        if 'x' in term:
            new_terms.append(term)
    
    new_terms.append(str(s))
    
    return ' + '.join(new_terms)


# Example usage
share(10, 5, 4)