#two pointers

'''
two pointers mean using two index variables that
move through a data structure 
(usually an array or string)
to avoid nested loops
instead of checking every pari of elements (O(n^2))

you move two pointers toward each other based on 
some condition 
getting the answer in O(n)


The most classic setup:
one pointer starts at the beginning
one starts at the end
and they move toward each other

left = 0
right = len(arr) - 1

while left < right:
    #do something based on arr[left] and arr[right]
    #then move left forward, right backward, or both



Given a sorted array of integers numbers
and a target, return the indices
(1-indexed this time) of the two
numbers that add up to target.
Assume exactly one solution exists,
and you can't use the same element twice.
Example: numbers = [2,7,11,15], 
target = 9 → [1,2] (1-indexed, so index 0 and 1 → 1 and 2)

'''

def two_sum_sorted(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right: #stops once left has touch the right side
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left +1, right+1]
        elif current_sum > target: 
            right -= 1
        else:
            left += 1
