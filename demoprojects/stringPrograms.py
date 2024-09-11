####### String Programs List
# reverse a string
# reverse each word of a string
# Reverse the string with preserving the position of spaces
# Program to reverse order of words.
# remove all white spaces from a string
# find duplicate characters in a string
# check whether two given strings are anagram or not
# count occurrences of each character in a string
# check whether one string is a rotation of another
# find longest substring without repeating characters in a string
# program to swap two string variables without using third or temp variable
# Find The First Repeated Character In A String
# Find The First Non-Repeated Character In A String
# How to remove all vowels from a string
# print common characters between two strings in alphabetical order.
# Most repetitive character in a string
# Write a program to remove duplicate characters from the given input string
# # Write a program to print characters at odd position and even position for the given String
# Program to merge characters of 2 strings into a single string by taking characters alternatively.
# Write a program to sort the characters of the string and first alphabet symbols followed by numeric values
# All permutations of a string
# print all sub strings of a string
# Write a program for the following requirement. Input: a4b3c2 and output: aaaabbbcc
# Write a program to perform the following activity. input: a4k3b2 and output: aeknbd

#################################################################
####1. reverse a string

# using for loop
def reverse_string_loop(s):
    reversed_string = ''
    for char in s:
        reversed_string = char + reversed_string
    return reversed_string

# print(reverse_string_loop("reverse the string 1"))

# Using Slicing
def reverse_string_slicing(s):
    return s[::-1]

#print(reverse_string_slicing("reverse the string 2"))

# Using the reversed() Function
def reverse_string_reversed(s):
    return ''.join(reversed(s))
#print(reverse_string_reversed("reverse the string 3"))

# Using Recursion
def reverse_string_recursion(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string_recursion(s[:-1])
    
#print(reverse_string_recursion("reverse the string 4"))    

#################################################################################
####2. reverse each word of a string

def reverse_words(input_string):
    # Split the input string into words
    words = input_string.split()
    # Reverse each word in the list
    reversed_words = [word[::-1] for word in words]
    # Join the reversed words back into a single string
    output_string = ' '.join(reversed_words)
    return output_string
#print(reverse_words("reverse each word of the string"))

#################################################################################
####3. Reverse the string with preserving the position of spaces

def preserveSpace(Str):
	n = len(Str)
	Str = list(Str)

	# Initialize two pointers as two corners 
	start = 0
	end = n - 1

	# Move both pointers toward each other
	while(start < end):
		# If character at start or end is space, ignore it
		if(Str[start] == ' '):
			start += 1
			continue
		elif(Str[end] == ' '):
			end -= 1
			continue	  
		# If both are not spaces, do swap 
		else:
			Str[start], Str[end] = (Str[end],
									Str[start])
			start += 1
			end -= 1
	return ''.join(Str)

#print(preserveSpace("internship at geeks for geeks")) 

#################################################################################
####4. Program to reverse order of words.

def reverse_order_words(str):
      s = "i like this program very much"
      words = str.split(' ')
      string =[]
      for word in words:
           string.insert(0, word)
      return " ".join(string)
#print(reverse_order_words("i like this program very much"))

#################################################################################
####5. remove all white spaces from a string

def removeAllWhiteSpaces(str):
      return str.replace(" ", "")

#print(removeAllWhiteSpaces(" remove all spaces "))
#print(" strip the spaces ".strip())

#################################################################################
####6. find duplicate characters in a string

def duplicate_characters(string):
    chars = {}
    for char in string:
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1
 
    # Create a list to store the duplicate characters
    duplicates = []
    for char, count in chars.items():
        if count > 1:
            duplicates.append(char)

    return duplicates
#print(duplicate_characters("geeksforgeeks"))

#################################################################################
####7. check whether two given strings are anagram or not

def checkAnagram(str1, str2):
    char_list_1 = list(str1)
    char_list_2 = list(str2)
    char_count = {}
    anagramFlag = False

    if(len(char_list_1) != len(char_list_2)):
        print("The strings are not anagrams, lengths are not equal")
        return anagramFlag

    for char in char_list_1:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
        
    for char in char_list_2:
        if char not in char_count:
            print("The strings are not anagrams.")
            return anagramFlag
        else:
            char_count[char] -= 1

    for count in char_count.values():
        if count != 0:
            print("The strings are not anagrams.")
            return anagramFlag
        else:
            continue
    anagramFlag = True
    return anagramFlag

#print(checkAnagram("test", "estt1"))

#################################################################################
####8. count occurrences of each character in a string

def charactersCount():
    inp_str = "find the occurences of all characters"
    freq = {} 
    for ele in inp_str: 
         if ele in freq: 
            freq[ele] += 1
         else:
            freq[ele] = 1
    print ("Occurrence of all characters is :\n "+ str(freq))

#charactersCount()

#################################################################################
####9. check whether one string is a rotation of another

def areRotations(string1, string2):
	size1 = len(string1)
	size2 = len(string2)
	temp = ''

	temp = string1 + string1

	# Now check if str2 is a substring of temp
	if (temp.count(string2)> 0):
		return True
	else:
		return False

#print(areRotations("abcd", "dabb"))

#################################################################################
####10. find longest substring without repeating characters in a string

#################################################################################
####11. program to swap two string variables without using third or temp variable

def swapTwoStrings(str1, str2):
    print("Strings before swapping: " + str1 + " " + str2);  
   
    #Concatenate both the string str1 and str2 and store it in str1  
    str1 = str1 + str2;  
    str2 = str1[0 : (len(str1) - len(str2))];  
    str1 = str1[len(str2):];  
    print("Strings after swapping: " + str1 + " " + str2)

#swapTwoStrings("test1", "test2")

#################################################################################
#### Find The First Non-Repeated Character In A String

def firstUniqChar(s):
    freq = [0] * 26
    for c in s:
        freq[ord(c) - ord('a')] += 1

    for i in range(len(s)):
        if freq[ord(s[i]) - ord('a')] == 1:
            return s[i]
    return -1

#print(firstUniqChar("teedt"))

#################################################################################
#### Find The First Repeated Character In A String

def firstRepChar(s):
    # Create an array to store the count of characters
    charCount = [0] * 26

    for ch in s:
        index = ord(ch) - ord('a')
        if charCount[index] != 0:
            return ch
        charCount[index] += 1

    return "-1"
#print(firstRepChar("ussdwerw"))


#################################################################################
#### remove all vowels from a string

def rem_vowel(string): 
	vowels = ['a','e','i','o','u'] 
	result = [letter for letter in string if letter.lower() not in vowels] 
	result = ''.join(result) 
	print(result) 

#rem_vowel("GeeksforGeeks - A Computer Science Portal for Geeks") 

##
#### using Regex ###########
import re 
def rem_vowel_regex(string): 
	return (re.sub("[aeiouAEIOU]","",string))			 

#print(rem_vowel_regex("GeeksforGeeks")) 

#################################################################################
# print all sub strings of a string

#################################################################################
# print common characters between two strings in alphabetical order.

#################################################################################
#### find most repetitive character in a string

def mostRepeatitiveChar(test_str):
    print ("The original string is : " + test_str)

    freq = {}
    for char in test_str:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    # finding the character with maximum frequency
    max_char = max(freq, key=freq.get)
    return max_char

#print(mostRepeatitiveChar("qweerttttup"))

#################################################################################
# Write a program to remove duplicate characters from the given input string
def removeDuplicates(str):
    p = ""
    for char in str:
        if char not in p:
            p = p+char
    print(p)

#removeDuplicates("geeksforgeeks")

#################################################################################
# # Write a program to print characters at odd position and even position for the given String

def evenOddPosUsingListComprehension(str):
    list2 = [x for ind, x in enumerate(str) if ind%2==0]
    list3 = [x for ind, x in enumerate(str) if ind%2!=0]
    print(list2)
    print(list3)

def evenOddPosUsingListSlicing(str):
    print("Even Characters:", str[::2]) # Characters at even index 
    print("Odd Characters:", str[1::2]) # Characters at odd index 

     
#evenOddPosUsingListComprehension("test at even odd position")
#evenOddPosUsingListSlicing("test second method")

#################################################################################
# Program to merge characters of 2 strings into a single string by taking characters alternatively.

#################################################################################
#### Write a program to sort the characters of the string and first alphabet symbols followed by numeric values

def sortCharsAndNumbers(input):
    print("The original string is : " + input)
    
    # separating numbers and alphabets
    num_list = [x for x in input if x.isnumeric()]
    alpha_list = [x for x in input if not x.isnumeric()]
    
    # sorting the lists
    num_list.sort()
    alpha_list.sort()
    
    # concatenating the lists
    res = alpha_list + num_list
    
    # printing result 
    print("The Custom sorted result : " + ''.join(res))

#sortCharsAndNumbers("weray451u")

#################################################################################
# Write a program for the following requirement. Input: a4b3c2 and output: aaaabbbcc

def charMultiplicationForDigits(input):
     output = ''
     for char in input:
          if char.isalpha():
               output = output + char
               prev = char
          else:
               output = output + prev*(int(char)-1)  
     print(output)
#charMultiplicationForDigits("a4b3c2")


#################################################################################
#### Write a program to perform the following activity. input: a4k3b2 and output: aeknbd

def charAdvancement(input):
     output = ''
     for char in input:
          if char.isalpha():
               output = output + char
               prev = char
          else:
               output = output + chr(ord(prev) + int(char)) 
     print(output)
charAdvancement("a4k3b2")