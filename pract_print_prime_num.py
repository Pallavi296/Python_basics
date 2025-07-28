# The Following code checks if the user-provided number is prime or not

# Defining the function
# Logic : A number is not prime if :
# 		1. it is less than equal to 1 and
# 		2. it is divisible by any number except 1 and itself

def is_prime(num):
    if num>1:

        for i in range(2,num):
            if num%i==0:
                return False
        return True
    else:
            return True
num = int(input ("Enter num:"))

#Condition check
if is_prime(num):
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")

   