""" 
https://www.codewars.com/kata/56f173a35b91399a05000cb7/solutions/python

Simple challenge - eliminate all bugs from the supplied code so that the code runs and 
outputs the expected value. Output should be the length of the longest word, as a number.

find_longest("The quick white fox jumped around the massive dog"), 7)

def find_longest(string):
    spl = str.split(" ")
    longest = 0
    i=0
    while (i > spl.length):
    if (spl(i).length > longest): longest = spl[i].length
    return longest """

def find_longest(string):
    spl = string.split(" ")
    longest = 0
    i=0
    while (i < len(spl)):
        if (len(spl[i]) > longest): 
            longest = len(spl[i])
        i += 1   
    return longest


x = find_longest("The quick white fox jumped around the massive dog")
print(x)