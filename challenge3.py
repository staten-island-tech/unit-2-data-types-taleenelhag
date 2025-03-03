def find_factor(num):
    factors = []
    for i in range(1, min(num) + 1): 
        if num % i == 0:
            factors.append(i)
    return factors 

number = 20
print(f"factprs {number} are: {find_factor(number)}")
