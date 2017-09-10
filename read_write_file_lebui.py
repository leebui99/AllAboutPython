#CS-142 Lab 4
#Read and Write story.txt
#The number of Lines
#The number of Words
#The number of Characters


def main():
    fname = "story.txt"

    num_lines = 0
    num_words = 0
    num_chars = 0

    with open(fname, 'r') as f:
        for line in f:
            words = line.split()

            num_lines += 1
            num_words += len(words)
            num_chars += len(line)
        
    print("Lines ", num_lines) #Print out number of lines
    print("Words ", num_words) #Print out number of words
    print("Characters ", num_chars) #Print out number of characters
    
main()


