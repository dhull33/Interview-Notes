"""
Given a string S, of length N that is indexed from 0 to N-1, print its even
indexed and odd-indexed characters as 2 space separated strings on a single
line. 0 is considered an even index in this exercise.

"""
def slice_my_string():
    test_cases = int(input('How many strings do you want to slice? '))
    for i in range(test_cases):
        my_string = input('Enter your string: ')
        n = len(my_string)
        # using string indexing where the first number is the inclusive
        # starting point; n+1 is the exclusive ending point; 2 is the steps
        # to take
        print(my_string[0:n+1:2], my_string[1:n+1:2])


""" 
Read an integer N. Without any string methods, print the following: 1234...N.
Note that "..." represents the values in between. 

"""
def print_number_as_string():
    n = int(input("Enter an integer: "))
    i_exponent = len(str(n))
    i = 10**i_exponent
    j = 1
    sum_total = n
    while j < n:
        sum_total = (sum_total + (n-j)*i)
        j += 1
        i_exponent = len(str(sum_total))
        i = 10**i_exponent
    print(sum_total)
