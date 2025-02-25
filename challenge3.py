"""  x = True
y = True

def GCF(): 
    factors = []
    for 1 in range (1, num +1) 
        x = % 1 == 0  
        y = true 
number = int(input("Enter a number to find its factors: "))  """

""" def vote(age,id):
    if age <18 or id == False:
        print("cannot vote")
    elif age >18 and id == True:
        print("vote") 

def skins2(money, cost, isAvailable): 
    if isAvaliable == True:
        if money > 10  or cost == 0: 
            print("Yuuuuuuuup")
        else:
            print("Bruh get out!") """

def GCF(num):
    factors = []  # List to store the factors
    for i in range(1, num + 1):  # Loop through numbers from 1 to num
        x = num % i == 0  # Check if i is a factor of num (no remainder)
        y = True  # y is always True (as per your format)

        if x == True and y == True:  # If both conditions are true, i is a factor
            factors.append(i)

    return factors

# Accept user input
number = int(input("Enter a number to find its factors: "))  # Input the number

# Call the function and print the result
factors = GCF(number)
print(f"The factors of {number} are: {factors}")
