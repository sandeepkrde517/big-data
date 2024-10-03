################################################################
#### Array programs List

# How to find the most frequent element in an array
# How to find duplicate elements in an array
# How to remove duplicate elements from Array
# How to find second largest number in an integer array
# How to find third largest number in an integer array
# find smallest and second smallest element in an integer array
# How to find all pairs of elements in an array whose sum is equal to given number
# How to separate zeros from non-zeros in an array
# How to sort an array of 0s and 1s
# How to sort an array of 0s, 1s and 2s

# Find missing number in an array
# How do you count occurrences of each element in an array
# Reverse an array.
# Array Rotation Program
# Contiguous sub arrays with given sum
# Contiguous sub array with maximum sum

# How to find intersection of two arrays
# How to find union and intersection of multiple arrays
# How do you check the equality of two arrays
# How to merge two sorted arrays
# How to merge two unsorted arrays in sorted order
# How to merge two sorted or unsorted arrays into single sorted array without duplicates
# How to sort array elements by frequency
# How to find all the leaders in an integer array

################################################################
# How to find the most frequent element in an array

# Brute force approach
def most_frequent(List):
    counter = 0
    num = List[0]
    
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i

    return num

#print(most_frequent([2, 1, 2, 2, 1, 3]))

########
# using Counter 

from collections import Counter

def most_frequent(List):
    occurence_count = Counter(List)
    return occurence_count.most_common(1)[0][0]
  
# print(most_frequent([2, 1, 2, 2, 1, 3,3,3,3,3]))

################################################################

def findDuplicates():
    input_list = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
    print(list(set([x for i,x in enumerate(input_list) if input_list.count(x) > 1])))

#findDuplicates()

################################################################
# How to remove duplicate elements from Array

def Remove(duplicate):
	final_list = []
	for num in duplicate:
		if num not in final_list:
			final_list.append(num)
	return final_list
	
# print(Remove([2, 4, 10, 20, 5, 2, 20, 4]))

###############
## using set

# print(list(set([2, 4, 10, 20, 5, 2, 20, 4])))

################################################################
# How to find second largest number in an integer array

def find_second_largest(numbers):
    largest = second_largest = float('-inf')
    
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    
    return second_largest

# print("The second largest number is:", find_second_largest([10, 20, 4, 45, 99]))

##########
## using max function
def second_largest(numbers):
    largest = max(numbers)
    numbers.remove(largest)
    return max(numbers)

# print("The second largest number is:", second_largest([10, 20, 4, 45, 99,97]))

################################################################
# How to find third largest number in an integer array

import sys
def thirdLargest(arr):
        arr_size = len(arr)
        if (arr_size < 3):
        
            print(" Invalid Input ")
            return

        first = arr[0]
        second = -sys.maxsize
        third = -sys.maxsize

        for i in range(1, arr_size):
                
            if (arr[i] > first):
            
                third = second
                second = first
                first = arr[i]
            
            elif (arr[i] > second):
            
                third = second
                second = arr[i]

            elif (arr[i] > third):
                third = arr[i]
        
        print("The third Largest element is", third)

# thirdLargest([12, 13, 1, 10, 34, 16])

############
# using sort method :: check the error
def third_highest_using_sort(arr):
     sorted_array = arr.sort()
     return sorted_array[-3]

# print(third_highest_using_sort([12, 13, 15,1,10, 34, 16]))

################################################################
# Python program to find smallest and second smallest elements

import math
def print2Smallest(arr):

	arr_size = len(arr)
	if arr_size < 2:
		print("Invalid Input")
		return

	first = second = math.inf
	for i in range(0, arr_size):

		if arr[i] < first:
			second = first
			first = arr[i]

		elif (arr[i] < second and arr[i] != first):
			second = arr[i]

	if (second == math.inf):
		print("No second smallest element")
	else:
		print('The smallest element is', first, 'and',
			' second smallest element is', second)

# print2Smallest([111, 13, 25, 9, 34, 1])

################################################################
# How to find all pairs of elements in an array whose sum is equal to given number

def findPairs(lst, K): 
	res = []
	while lst:
		num = lst.pop()
		diff = K - num
		if diff in lst:
			res.append((diff, num))
		
	res.reverse()
	return res
	
# print(findPairs([1, 5, 3, 7, 9], 12))

################################################################
# How to sort an array of 0s and 1s

def segregate0and1(arr):
      
        n = len(arr)
        count = 0
        for i in range(0, n): 
            if (arr[i] == 0): 
                count = count + 1

        for i in range(0, count):
                
            arr[i] = 0

        for i in range(count, n): 
            arr[i] = 1
        print(arr)   

# segregate0and1([1,0,1,0,1,1,1,0,0,0,0])       

################################################################
# How to separate zeros from non-zeros in an array
def pushZerosToEnd(arr):
    count = 0 # Count of non-zero elements
    n = len(arr)
    print("Before: ", arr)
    for i in range(n):
        if arr[i] != 0:
            
            # here count is incremented
            arr[count] = arr[i]
            count+=1

    while count < n:
        arr[count] = 0
        count += 1

    print("After: ", arr)    

# pushZerosToEnd([1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9])
################################################################
# How to sort an array of 0s, 1s and 2s

def sortArr(arr): 
        n = len(arr)
        cnt0 = 0
        cnt1 = 0
        cnt2 = 0
        
        for i in range(n): 
            if arr[i] == 0: 
                cnt0+=1
            
            elif arr[i] == 1: 
                cnt1+=1
                
            elif arr[i] == 2: 
                cnt2+=1
        
        # Update the array 
        i = 0
        
        # Store all the 0s in the 
        # beginning 
        while (cnt0 > 0): 
            arr[i] = 0
            i+=1
            cnt0-=1
        
        # Then all the 1s 
        while (cnt1 > 0): 
            arr[i] = 1
            i+=1
            cnt1-=1
        
        # Finally all the 2s 
        while (cnt2 > 0): 
            arr[i] = 2
            i+=1
            cnt2-=1
        print(arr)

# sortArr([0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]) 

################################################################
# Find missing number in an array

def missing_number(n, arr):
    # Create hash array of size n+1
    hash = [0] * (n + 1)

    # Store frequencies of elements
    for num in arr:
        hash[num] += 1

    # Find the missing number
    for i in range(1, n + 1):
        if hash[i] == 0:
            return i

    # Edge case handling (though problem guarantees a solution)
    return -1

# print(missing_number(6,[1, 2, 3,4,6]))

################################################################


################################################################


################################################################



################################################################


################################################################


################################################################


################################################################