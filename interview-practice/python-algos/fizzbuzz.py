# From: https://realpython.com/python-coding-interview-tips/


""" 
    In FizzBuzz, you are given a list of integers. Your task is to do the following:

    Replace all integers that are evenly divisible by 3 with "fizz"
    Replace all integers divisible by 5 with "buzz"
    Replace all integers divisible by both 3 and 5 with "fizzbuzz"   

"""


def fizzbuzz(listofnum):
    for idx, num in enumerate(listofnum):
        if (num % 3 == 0 and num % 5 == 0):
            listofnum[idx] = "fizzbuzz"
        elif (num % 5 == 0):
            listofnum[idx] = "buzz"
        elif (num % 3 == 0):
            listofnum[idx] = "fizz"
    print(listofnum)
    
list = [45, 22, 14, 65, 97, 72] 
fizzbuzz(list)


# TESTS
# check given multiple inputs
# invalid input test

