#
# A solution to Task #1 for a job application for the company "FNTASTIC".
#
# Author:   alsergkir
# Language: Python v3.10.2
#

# Checks if char exists in a list and returns its place
def has_char(list, char) :
    for i in range(len(list)) :
        if list[i][0] == char :
            return True, i
            
    return False, 0

# Main function. Expects a string argument
def replace(input) :
    unique_chars = [] # list structure: [[char, amount]]
    output = input.lower() # switching to lowercase
    
    # we check if char already exists in the list
    # if yes - increment the amount
    # if not - add it to the list
    for char in output :
        has, i = has_char(unique_chars, char)
        if has :
            unique_chars[i][1] = unique_chars[i][1] + 1
        else :
            unique_chars.append([char, 1])
    
    # we iterate through the list and replace chars
    for element in unique_chars :
        if element[1] > 1 :
            output = output.replace(element[0], ')')
        else :
            output = output.replace(element[0], '(')
    
    # fancy output
    print("Input: " + input)
    print("\tchar\tamount")
    for element in unique_chars :
        print("\t " + element[0] + "\t  " + str(element[1]))
    print("Output: " + output + "\n")

# Calling main function
replace("din")
replace("recede")
replace("Success")
replace("(( @")