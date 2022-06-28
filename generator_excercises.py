#Generator Excercises

#Problem 1
#Create a generator, primes_gen that generates prime numbers starting from 2.
"""
def primes_gen():
    num = [2]
    prime = []
    while True:
        for i in num:
            if i % i == 0:
                prime.append(i)
                num.append[i + 1]
            else:
                num.append[i + 1]
        yield prime

gen = primes_gen()
for _ in range(10):
    print(next(gen), end=' ')
"""
# Expected output
# 2 3 5 7 11 13 17 19 23 29
#----------------------------------------------------------------------------
#Problem 2
#Create a generator, unique_letters that generates unique letters from
#the input string. It should generate the letters in the same order as
#from the input string.
def unique_letters(letter):
    n = 0
    while n <= len(letter):
        #for i in 
        yield letter[n]
        n += 1
        

for letter in unique_letters('hello'):
    print(letter, end=' ')
# Expected output
# h e l o
