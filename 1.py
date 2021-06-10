import math

D = input("Enter the values in comma-separated manner:")
C = 50
H = 30
new_list = []
for i in D.split(','):
    Q = math.sqrt((2 * C * int(i))/ H)
    new_list.append(Q)
    
print(new_list)