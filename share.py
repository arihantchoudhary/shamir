# import galois
# def share(n, k, s):
#     '''
#     n: Total number of parties
#     k: number of parts needed to reconstruct the k-1 degree polynomial
#     s: secret to be shared
#     '''
    
#     #defining a field of size n+1
#     field = galois.G7(k-1)
#     #equation => y = s + f1(x) + f2(x)^2 + f3^x^3 ... fk-1 * x^k-1
#     #Computing {y1, y2, ... yn}
#     y_values = []
#     for i in range(n):
#         temp = s
#         for j in range(k-1):
#              temp += field.Add(f_vals[j], i ** j)
#         y_values.append[temp]
    
#     return y_values
