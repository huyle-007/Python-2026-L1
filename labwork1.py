#1
r = int(input("Enter the radius: "))
C = float(r * r * 3.14)
print("The circle area is " + str(C))

#2
C = int(input("Enter the temp in Celsius: "))
F = float((C * 9/5) + 32)
print("The temp in Fahrenheit is " + str(F))

#3
n = int(input("Enter a number: "))
if n < 2: print( str(n) + " is not a prime number ")
elif n == 2: print(str(n) + " is a prime number ")
else:
    for i in range(2, n):
        if n % i == 0:
            print(str(n) + " is not a prime number ")
            break
        else: print(str(n) + " is a prime number ")
        break

#4
n = int(input("Enter a number: "))
def number(n):
    numb = []
    for i in range(1, n):
      if n % i == 0:
        numb.append(i)
    return numb


total = sum(number(n))
if total == n:
  print(str(n) + " is a perfect number ")
else: print(str(n) + " is not a perfect number ")


#5
Color = ['Blue', 'Yellow', 'Red', 'Orange', 'Purple']
C_name = str(input("Enter the color name: "))
if C_name in Color: print(str(C_name) + " is in the list ")
else: print(str(C_name) + " Sorry, I could not find your color" )
for i in range (len(Color)):
  if C_name == Color[i]:
    print(str(C_name) + " is at index " + str(i+1) + " in my list ")
    break



#6
range1 = list(range(0, 7))    # = print([ i for i in range1])
range2 = list(range(1, 11, 3))
range3 = list(range(5, 0, -1))
range4 = list(range(6, -3, -2))

print("range1:", range1)
print("range2:", range2)
print("range3:", range3)
print("range4:", range4)

#7
def remove_dollar_sign(s):
  new_str = ""                       # return "".join[c for c in s if c != ]
  for char in s:
    if char != "$":
      new_str += char
  return new_str
input_str = input("Enter a string: ")
result = remove_dollar_sign(input_str)
print(result)

#8
def extract_even():
  list1 = [1,4,5,-1,10]
  new_list = []
  for i in list1:
    if i % 2 == 0:
      new_list.append(i) # =       new.list += [i]
  return new_list
result = extract_even()
print(result)

#9
n = int(input("Enter a number: "))
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)
print(factorial(n))

#10
n = int(input("Enter a number: "))
def divisor_numb(n):
  divisor_list = []
  for i in range(1, n+1):
    if n % i == 0:
      divisor_list.append(i)
  return divisor_list
print(divisor_numb(n))


#11
import math

def dist_2_p(x, y, a, b):
  distance =  math.sqrt((a-x)**2 + (b-y)**2)
  return distance
x = int(input("Enter x1: "))
y = int(input("Enter y1: "))
a = int(input("Enter x2: "))
b = int(input("Enter y2: "))
print(dist_2_p(x, y, a, b))

#12
def print_rectangle(m, n):
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m-1 or j == 0 or j == n-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
print_rectangle(4, 5)

