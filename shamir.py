import galois
import re 
def reconstruct(val):
    """
    y_values: parts of secret s
    """
    #Printing Points for reference:
    # print(points)
    points, k, n, field = val
    #Keep only first k points and remove extra points
    if(len(points) > k):
        points = points[0:k]
    print("Parts of the secret: ", points)
    
    
    #Creating a field 
    GF = galois.GF(field)
    # print(GF.characteristic)
    field = GF.characteristic
    # points = [galois.Poly(i, field=GF) for i in points]
    
    #storing all (x,y) values separately as field elements
    x_values = [(i[0])%field for i in points]
    y_values = [(i[1])%field for i in points]
    # print("X ", (x_values))
    # print("Y ", (y_values))

    #Result variable will store the reconstructed secret
    result = 0 % field
    x = (0) % field

    for i in range(len(x_values)):
        y = (y_values[i])%field
        term = 1 % field

        for j in range(len(x_values)):
            if i != j:
                numerator = (x - x_values[j]) % field
                #finding the multiplicative inverse of d and storing denominator
                d = (x_values[i] - x_values[j]) % field
                _ , denominator, _ = galois.egcd(d, field) 
                #check
                # print(numerator, d, denominator)
                #formula = (x-xj)/(xi-xj)
                term *= (numerator * (denominator % field)) % field
        
        #formula = sum(y*terms)          
        result = (result + ((y*term) % field)) % field

    return result
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
    field = 1009    
    # n = next_prime(n)  # function to set n to the first prime greater than n
    GF = galois.GF(field)  # GF is a field of size n
    print("Prime Field: ", field)

    # creating a polynomial of size (k-1)
    equation = galois.Poly.Random((k-1), field=GF)
    # print("Before:", str(equation))
    #removing x = 0 from the equation
    equation = equation - equation(0) + GF(s);

    # add secret to equation
    # replaced_eq = replace_coefficient(str(equation), s)
    # equation = galois.Poly.Str(replaced_eq, field=GF)
    # print("After:", str(equation))
    
    
   
    # Computing {y1, y2, ... yn} 
    y_values = []
    for i in range(1, n+1):
        temp = int(equation(i))
        y_values.append([i, temp])

    # print("Y values given out", y_values)
    return y_values, k, n, field



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
    next_num = n*100 + 1
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

# # Example usage
# y_values =  [[1, 993], [2, 422], [3, 686], [4, 1], [5, 476], [6, 41], [7, 519], [8, 563], [9, 701], [10, 309]]
# result = reconstruct(y_values, 5, 10, 1009)
# print("f(0) =", result) 
print("Reconstructed Secret: ", reconstruct(share(10, 5, 4)))
print("Reconstructed Secret: ", reconstruct(share(11, 6, 69)))