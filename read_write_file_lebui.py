#CS-142 Lab 4
#Read and Write story.txt
#The number of characters
#The number of letters
#The number of lowercase letters
#The number of consonants


def main():
    searchFile = open("story.txt", "r")
    for line in searchFile:
        print(line) #Print out the file contains

main()


