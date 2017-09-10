#CS-142 Lab 2.a
#Convert Decimal number to Binary number

def decimal_to_binary(number):
   binary_list = [] #make empty list
   old_number = number #Referance number
   while(number > .5):
       if(number % 2 != 0):
           binary_list.append(1)
       else:
           binary_list.append(0)
       number = number / 2 
       number = int(number)
   print(binary_list[::-1]) #print the list to show the correctly

def main():
    select = 0
    while(select == 0):
        number = int(input("Please input a decimal: "))
        decimal_to_binary(number)
        print()
        question = 1
        while(question == 1):
            user_reponse = input("Would you like to conver another? yes or no?")
            print()
            if (user_reponse == "yes"):
                select = 0
                question = 0
            elif (user_reponse == "no"):
                select = 1
                question = 0
            else:
                print("Invalid input, try again!")
                question = 1
    print("Finished")

main()
