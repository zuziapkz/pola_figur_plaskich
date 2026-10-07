# i = 0
# while i<10 :
#     i += 1
#     print(i)

# i = 10
# while i>0 :
#     print(i)
#     i -= 1

# tablica = [21,-1,54, 7]
# mks = tablica[0]
# for a in tablica:
#     print (f"mks = {mks}" )
#     print (f"a = {a}")
#     if a > mks:
#         mks = a

# print (mks)

# print(3%2)

# duplicates = []
# tablica = [1,4,6,4,8,7,5,6,7,6]
# for a in tablica:
#     x=0
#     for b in tablica:
#         if a == b:
#             x += 1
#     if x > 1 and a not in duplicates:
#         duplicates += [a]
# print (duplicates)

# duplicates = []
numbers = [3,5,3,7,7,7]
for a in numbers:
    x=0
    for b in numbers:
        if a == b:
            x += 1
    if x > 1 and a in numbers:
        numbers.remove (a)
print (f"numb = {numbers}")

