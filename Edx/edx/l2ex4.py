"""num = 0
while num <= 5:
    print (num)
    num += 1

print("outside of loop")
print(num)
"""

"""numberOfLoops = 0
numberOfApples = 2
# 0 1 2 3 4 5 6 7 8 9
while numberOfLoops < 10:
    numberOfApples *= 2
    numberOfApples += numberOfLoops
    numberOfLoops -= 1
print("number of apples; " + str(numberOfApples))
"""

num = 10
while num > 3:
    num -= 1
    # 10 9 8 7 6 5 4
    print (num)


'''num = 10
while True:
    if num < 7:
        print('Breaking out of loop')
        break
    print(num)
    num -= 1

print("Outside of loop")
'''
'''num = 100
while not False:
    if num < 0:
        break
print('num is: ' + str(num))
'''