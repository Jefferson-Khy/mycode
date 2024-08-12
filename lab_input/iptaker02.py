#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   print() - concatenate vs print a series of items"""

def main():

    # collect string input from the user
    user_input1 = input("Please enter an IPv4 IP address:")
    
    ## the line below creates a single string that is passed to print()
    # print("You told me the IPv4 address is: " + user_input)
    
    user_input2 = input("Please enter vendor name of your device: ")
    ## print() can be given a series of objects separated by a comma
    print("You told me the IPv4 address is:", user_input1)
    print("You told me the vendor name as:", user_input2)

main()

