x = 45
y = 18
print("Swapping useing XOR")
print("Before Swapping : ")
print("x = ",x)
print("y = ",y)
x = x ^ y
y = x ^ y
x = x ^ y
print("After Swapping")
print("x = ",x)
print("y = ",y)

number = 3
print("Orginal = ",number)
print(number, "<< 1 = ",number << 1)
print(number, "<< 2 = ",number << 2)
print(number, ">> 3 = ",number >> 3)
print(number, ">> 4 = ",number >> 4)
print("Each left shift multiplies the number by 2 and , right shift divides the number by 2.")


num1 = -10
num = 5
print("num1 = ",num1)
print("num = ",num)
if (num1 < 0) ^ (num<0):
    print("The numbers have different signs.")
else:
    print("THe numbers have the same sign.")