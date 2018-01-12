"""num = 10
for num in range (5):
    print(num)
print (num)
"""

"""divisor = 2
for num in range(0, 10, 2):
    print(num / divisor)

#result
#0, 0, 2, 3, 4, 5,
"""

"""for variablke in range (20):
    if variablke % 4 == 0:
        print ("variable")
    if variablke % 16 == 0:
        print("Foo!")

letter # 1 is S
letter # 2 is n
letter # 3 is o
letter # 4 is w
letter # 5 is !
"""
count = 0
for letter in "Snow!":
    print("Letter" + str(count) + "is" + str(letter))
    count += 1
    break
print (count)
