numbers = []

a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())

numbers += [a,b,c,d,e]

suma_numbers = a+b+c+d+e

print (f"suma_numbers = {suma_numbers}")

maksimum = numbers[0]
for x in numbers:
    if x > maksimum:
        maksimum = x

print (f"max = {maksimum}")

minimum = numbers[0]
for x in numbers:
    if x < minimum:
        minimum = x

print (f"min = {minimum}")

len (numbers)
print(f"sr. arytmetyczna = {suma_numbers / len(numbers)}")

P=0
for x in numbers:
    if x % 2 == 0:
        P += 1
print (f"l.liczb parzystych = {P}")

duplicates = []
for a in numbers:
    x=0
    for b in numbers:
        if a == b:
            x += 1
    if x > 1 and a not in duplicates:
        duplicates += [a]
print (f"duplikaty = {duplicates}")

for a in numbers:
    x=0
    for b in numbers:
        if a == b:
            x += 1
    if x > 1 and a in numbers:
        numbers.remove (a)
print (f"bez duplikatow = {numbers}")

a = a**2
b = b**2
c = c**2
d = d**2
e = e**2

squares = [a,b,c,d,e]
print(f"kwadraty = {squares}")