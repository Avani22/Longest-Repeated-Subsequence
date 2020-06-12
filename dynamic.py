'''
Name: Avani Chandorkar
Student ID: 1001668554
'''

import sys
import time


if (len(sys.argv) < 2):
    print("INVALID INPUT. No String entered.")
    sys.exit()

arr = str(sys.argv[1])                                                  #taking string input from user
print("Input String is: ", arr)

len1 = len(arr)                                                         #calculating length of string input
print("Length of String is: ", len1)
if (len1 == 1):
    print("Only one input character entered. Please enter more characters")
    sys.exit()


def create_table(arr):                                                  #Creating storage as a table to store valid subsequences
    res = []
    res = [[0 for i in range(len1 + 1)] for j in range(len1 + 1)]

    for i in range(1, len1 + 1):
        flag = 0
        for j in range(1, len1 + 1):
            if (arr[i - 1] == arr[j - 1] and i != j and flag == 0):    #if characters match and indices are not same
                res[i][j] = 1 + res[i - 1][j - 1]
                flag = 1
            else:                                                       #if characters do not match
                res[i][j] = max(res[i - 1][j], res[i][j - 1])
    return res


def lrs(arr):                                                           #Finding subequence in storage which is longest and repeated most
    res = create_table(arr)

    i = len1
    j = len1
    ans = ''
    isAns = False
    while (i > 0 and j > 0):                                            #If this cell is same as diagonally adjacent cell just above it, then
                                                                        # same characters are present at  arr[i-1] and arr[j-1]. Append any of them to result.
        if (res[i][j] == res[i - 1][j - 1] + 1):
            ans += arr[i - 1]
            i -= 1
            j -= 1
            isAns = True
        elif (res[i][j] == res[i - 1][j]):                              #Otherwise we move to the side that gave us maximum result.
            i -= 1
        else:
            j -= 1

    ans = ''.join(reversed(ans))                                         # As we traverse res[][] from bottom, we get result in reverse order.

    if (not isAns):
        print("No sequence found!")
        sys.exit()

    return ans

print("Longest repeated subsequence is: ", lrs(arr))                    # Printing the lonest repeated subsequence
