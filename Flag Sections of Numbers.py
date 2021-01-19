'''Return the sum of the numbers in the array/
except ignore the sections of numbers starting with a special number/
in this case is 6 to 9. Return 0 for no number
'''

def summer_69(arr):
    total = 0
    flag = True
    for num in arr:
        #another loop to add
        while flag:
            #this condition is handling total and find 6
            if num != 6:
                #if the number is not 6
                #add to the sum
                total += num
                #break out the loop
                break
            else:
                #if it is, flag it to false
                flag = False
                #break so it can go to other while loop
                break
        while not flag:
            #while this is not match with the first condition
            #we need to find other thing to handle this condition
            if num != 9:
                #if we cant find the 9
                #break
                break
            else:
                #if we found it then set the flag to True again
                #so it can be added to sum again
                flag = True
                break
    return total

if __name__ == "__main__":
    print(summer_69([1, 3, 5])) # 9
    print(summer_69([4, 5, 6, 7, 8, 9])) # 9
    print(summer_69([2, 1, 6, 9, 11])) # 14