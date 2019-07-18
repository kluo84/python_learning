'''
Using the Python language, have the function AlphabetSoup(str) take the str string parameter being passed and return 
the string with the letters in alphabetical order (ie. hello becomes ehllo). 
Assume numbers and punctuation symbols will not be included in the string.
Test case:

Input:"coderbyte"
Output:"bcdeeorty"

Input:"hooplah"
Output:"ahhloop"
'''

def AlphabetSoup(str):
    new_array = ""
    for char in str:
        new_array += char
    return "".join(sorted(new_array))
    
# keep this function call here  
print AlphabetSoup("coderbyte")  
