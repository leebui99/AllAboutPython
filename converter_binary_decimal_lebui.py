#CS-142 Lab 
#Convert Binary number to Decimal number

def binary_to_decimal(binary_list, binary_length):
    #We passed our list (array)
    index = 0
    power = binary_length - 1
    total = 0 #Decimal value

    while(power >= 0):
        total += (int(binary_list[index])) * (2**(power))
        index += 1
        power -= 1
    print(total)



def main():
    #Get out main loop ready     
    loop = 0
    while(loop == 0):
        switch = 0
        while(switch  == 0):
            binary_number = input("Please enter 8bit binary number: ")
            binary_number_list = list(binary_number)
            binary_length = len(binary_number_list)
            if(binary_length > 8):
                print("Please do not input a number longer than 8bits. ")
                print("")
            else:
                for bit in binary_number_list:
                    if(int(bit) > 1 or int(bit) < 0):
                        print("Invalid binary number, only use 0's and 1's")
                    else:
                        switch = 1
    #if all goes well
    binary_to_decimal(binary_number_list, binary_length)
       
        
main()
