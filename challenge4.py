def find_factor(num, number_one):
    factors = []
    for i in range(1, min(num, number_one) + 1): 
        if num % i == 0 and number_one % i == 0:  
            factors.append(i)
    return factors 

number = 50
number_one = 200
print(f"The factors of {number} and {number_one} are: {find_factor(number, number_one)}")
