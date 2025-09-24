#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    else:
        print("Happy New Year!")
happy_new_year()        

def square_integers(int_list):
    squared = list()
    for num in int_list:
         squarednum = num * num
         squared.append(squarednum)
    return squared
print(square_integers([1,2,3,4,5]))         

def fizzbuzz():
  for num in range(1,101):      
    if num % 3 == 0 and num % 5 == 0:
        print ("FizzBuzz")
    elif num % 3 == 0:
        print ("Fizz")
    elif num % 5 == 0:
        print ("Buzz")
    else:
        print (num)
fizzbuzz()


# player_heights = [0.008, 0.008, 0.008, 0.009, 0.008, 0.01, 0.009, 0.009, 0.01, 0.008, 0.009, 0.009, 0.008, 0.008, 0.008, 0.009, 0.008, 0.009, 0.01, 0.01]

# # inch_heights = list()
# # for height in player_heights:
# #     inch_height = height * 7920
# #     inch_heights.append(inch_height)

# # print(player_heights)
# # print(inch_heights)

# player_heights = [height * 7920 for height in player_heights]
# print(player_heights)