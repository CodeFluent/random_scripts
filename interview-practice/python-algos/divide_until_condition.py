# From: https://stackoverflow.com/questions/40330623/keep-on-halving-by-integer-division-until-x-1/40330685

def keep_dividing(x):
    num = x   # temp variable 
    count = 0 # number of times divided
    while num > 1:
        num //= 2
        print(num)
        count += 1
   
    print("number of times divided = ", count) 

keep_dividing(128)

# TESTS
# check divide by 0