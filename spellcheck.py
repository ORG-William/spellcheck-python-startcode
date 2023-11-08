# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression
import time

def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")

    # Print first 50 values of each list to verify contents
    print(dictionary[0:50])
    print(aliceWords[0:50])


# end main()
def linearSearch(arr, tar):

    for i in range (len(arr)):
        if arr[i] == tar:
            return i
    return -1

def binarySearch(arr, t):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2


        if arr[mid] == t:
            return mid
        elif arr[mid] < t:
            left = mid + 1
        else:
            right = mid - 1
       
    return -1
    
arr = input("Which Array: ")
print(arr)

def searchLin():
    tar = input("What Word: ")
    startTime = time.time()
    output = linearSearch(arr, tar)
    endTime = time.time()
    if output != -1:
        print(f"time to find object {endTime-startTime} (s)")
    else:
        print(f"Word not found at all: {endTime - startTime} (s)")

def searchBin():
    t = input("What Word: ")
    startTime = time.time()
    output = binarySearch(arr, t)
    endTime = time.time()
    if output != -1:
        print(f"time to find object {endTime-startTime} (s)")
    else:
        print(f"Word not found at all: {endTime - startTime} (s)")

def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()


# Call main() to begin program
main()

while True:
    print('\nMenu')
    print('1. Linear Search')
    print('2. Binary Search')
    print('3. Exit')
    choice = input("Enter your choice: ")

    if choice == "1": 
       searchLin()
    elif choice == "2":
       searchBin()
    elif choice == "3":
        print("Shutting Down")
        break
    else:
        print("Not a valid Choice")

