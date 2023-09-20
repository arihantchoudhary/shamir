import galois
def reconstruct(points, k, n, field):
    """
    y_values: parts of secret s
    """
    #Printing Points for reference:
    # print(points)
    
    #Keep only first k points and remove extra points
    if(len(points) > k):
        points = points[0:k]
    # print("Updated: ", points)
    
    
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


# Example usage
y_values =  [[1, 993], [2, 422], [3, 686], [4, 1], [5, 476], [6, 41], [7, 519], [8, 563], [9, 701], [10, 309]]
result = reconstruct(y_values, 5, 10, 1009)
print("f(0) =", result) 


# #Input 1
# y_values =  [[1, 3], [4, 8], [8, 9], [9, 5], [10, 2]]
# result = reconstruct(y_values)
# print("f(0) =", result)


# # Suppose we have 4 points: (1, 2), (2, 3), (3, 5), (4, 9)
# x_values = [1, 2, 3, 4]
# y_values = [2, 3, 5, 9]
# # find f(0)
# result = reconstruct(y_values)
# print("f(0) =", result)

# #Input 2
# y_values = [4, 6, 7, 10, 0, 10, 0, 0, 0, 5]
# result = reconstruct(y_values)
# print("f(0) =", result)


# #Input 2
# y_values = [6, 7, 10, 0, 10]
# result = reconstruct(y_values)
# print("f(0) =", result)

# result = reconstruct([galois.GF(4, order=11), GF(4, order=11), GF(9, order=11),
#                       GF(4, order=11), GF(3, order=11), GF(5, order=11), 
#                       GF(5, order=11), GF(5, order=11), GF(3, order=11), 
#                       GF(4, order=11)])



    
    
        

    
    
    
    
    



# Example usage
y_values =  [[1, 993], [2, 422], [3, 686], [4, 1], [5, 476], [6, 41], [7, 519], [8, 563], [9, 701], [10, 309]]
result = reconstruct(y_values, 5, 10, 1009)
print("f(0) =", result) 


# #Input 1
# y_values =  [[1, 3], [4, 8], [8, 9], [9, 5], [10, 2]]
# result = reconstruct(y_values)
# print("f(0) =", result)


# # Suppose we have 4 points: (1, 2), (2, 3), (3, 5), (4, 9)
# x_values = [1, 2, 3, 4]
# y_values = [2, 3, 5, 9]
# # find f(0)
# result = reconstruct(y_values)
# print("f(0) =", result)

# #Input 2
# y_values = [4, 6, 7, 10, 0, 10, 0, 0, 0, 5]
# result = reconstruct(y_values)
# print("f(0) =", result)


# #Input 2
# y_values = [6, 7, 10, 0, 10]
# result = reconstruct(y_values)
# print("f(0) =", result)

# result = reconstruct([galois.GF(4, order=11), GF(4, order=11), GF(9, order=11),
#                       GF(4, order=11), GF(3, order=11), GF(5, order=11), 
#                       GF(5, order=11), GF(5, order=11), GF(3, order=11), 
#                       GF(4, order=11)])



    
    
        

    
    
    
    
    


