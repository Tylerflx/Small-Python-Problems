"""Problem 2: Pythagorean Numbers
formula : a**2 + b**2 = c **2

input : positive interger n
output: display all possible Pythagorean triples (a,b,c)
where 0 < a,b,c <= n
use funtion find_Pythagorean(n)
"""


def find_Pythagorean(n):
    tuples_of_number = []
    a = 1
    if n > 0:
        while a < n + 1:
            b = a + 1
            while b < n + 1:
                c = 1
                while c < n + 1:
                    c += 1
                    if (pow(a, 2)) + (pow(b, 2)) == (pow(c, 2)):
                        tuples_of_number.append([a, b, c])  #using tuple instead of list so that order cant be changed
                        # because it's addition
                        # so a + b = b + a
                        if len(tuples_of_number) >= 1:
                            a, b = b, a     # swap 2 variables
                            tuples_of_number.append([a, b, c])
                b += 1
            a += 1
        print(tuples_of_number)
    else:
        print('Please enter a possible number!')


n = int(input('Enter a positive number: '))
find_Pythagorean(n)
