#arrays & hash


'''

nums = [2, 7, 11, 15]

for i, num in enumerate(nums):
    print(i, num)




#return the indices of the two numbers that add up 
#to the target 




def main():
    nums = [2,7,11,15] #array of numbers
    target = 9

    cage = {} #our dictionary 
    for i, num in enumerate(nums): #for loop 
        complemnt = target - num #what other number to look for
        if complemnt in cage: #looking for other number
           return [cage[complemnt], i]
        cage[num] = i


print(main())


'''


#more 


'''
Problem 2: Contains Duplicate

Given an array of integers nums, return True if any value appears at least twice, and False if every element is distinct.
Example: nums = [1,2,3,1] → True (1 appears twice)
Example: nums = [1,2,3,4] → False
'''


def main():

d

print(main())