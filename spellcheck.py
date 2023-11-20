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
    while True:
        print('\nMenu')
        print('1. Spell Check a Word (Linear Search) ')
        print('2. Spell Check a Word (Binary Search) ')
        print('3. Spell Check Alice In Wonderland (Linear Search) ')
        print('4. Spell Check Alice In Wonderland (Binary Search)')
        print('5. Exit')
        choice = input("Enter your choice: ")

        if choice == "1":
            searchLin(dictionary)
        elif choice == "2":
            searchBin(dictionary)
        elif choice == "3":
            linAlice(dictionary, aliceWords)
        elif choice == "4":
            binAlice(dictionary, aliceWords)
        elif choice == "5":
            print("Shutting Down")
            break
        else:
            print("Not a valid Choice")


# end main()
def linearSearch(arr, tar):

    for i in range(len(arr)):
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


def searchLin(arr):
    tar = input("What Word: ")
    startTime = time.time()
    output = linearSearch(arr, tar)
    endTime = time.time()
    if output != -1:
        print(f"Object Found at pos: {output} ")
        print(f"time to find object {endTime - startTime} (s)")
    else:
        print(f"Word not found at all: {endTime - startTime} (s)")


def searchBin(arr):
    t = input("What Word: ")
    startTime = time.time()
    output = binarySearch(arr, t)
    endTime = time.time()
    if output != -1:
        print(f"Object Found at pos: {output} ")
        print(f"time to find object {endTime - startTime} (s)")
    else:
        print(f"Word not found at all: {endTime - startTime} (s)")


def linAlice(dict, alice):
    count = 0
    startTime = time.time()
    for i in range(len(alice)):
        t = linearSearch(dict, alice[i].lower())
        if t == -1:
            count += 1
    endTime = time.time()
    print(f"Not found:{count} ")
    print(f"{endTime - startTime} (s)")

def binAlice(dict, alice):
    count = 0
    startTime = time.time()
    for i in range(len(alice)):
        t = binarySearch(dict, alice[i].lower())
        if t == -1:
            count += 1
    endTime = time.time()
    print(f"Not found:{count} ")
    print(f"{endTime - startTime} (s)")


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
