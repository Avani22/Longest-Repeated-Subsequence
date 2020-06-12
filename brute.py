'''
Name: Avani Chandorkar
Student ID: 1001668554
'''

import time
import sys

if (len(sys.argv) < 2):
    print("INVALID INPUT. No String entered.")
    sys.exit()

input_arr = str(sys.argv[1])                                            #taking string input from user
print("Input String is: ", input_arr)

len1 = len(input_arr)                                                   #calculating length of string input
print("Length of String is: ", len1)
if (len1 == 1):
    print("Only one input character entered. Please enter more characters")
    sys.exit()

lst = []
lst = input_arr

def ntimes(lst, x):                                                # counting the number of times a letter is present in input
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count


repeated = []
l = []
left_over = []

for i in range(len1):                                                   # for loop for removing the unrepeated letters
    value = ntimes(input_arr, input_arr[i])
    if (value > 1):
        l.append(input_arr[i])
        for a in l:
            if a not in repeated:
                repeated.append(a)
    else:
        left_over.append(input_arr[i])

remaining = []

for i in range(0, len(repeated)):
    if (input_arr[0:i] == repeated[0:i]):
        remaining = repeated[i + 1:]

counter = 0
for k in range(0, len(remaining)):
    if input_arr[0:k + 1] == remaining[0:i + 1]:
        i += 1
        counter += 1

if counter == len(remaining) - 1:
    lrs = ''
    lrs = remaining
    print("Longest Repeated Sequence is: ", lrs)                            #Printing the lonest repeated subsequence

else:
    if (repeated == ''):                                                #if no repeated sequence
        print("No repeated sequence!")

    else:
        lrs = ''
        lrs = ''.join(repeated)
        print("Longest Repeated Sequence is: ", lrs)                        #Printing the lonest repeated subsequence

