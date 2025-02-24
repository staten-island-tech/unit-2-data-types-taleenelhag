""" values = [2,4,8,10]
print(values)
for i in values:
    print(i)
if values == "2,4,8,10":
    print("even")
else:
    print("odd")
 """
def odd_even(number): 
    if number % 2 == 0:
        print(f"{number} is even.")
    else: 
        print(f"{number} is odd.")
user_number = int(input("Enter a number:"))
odd_even(user_number)