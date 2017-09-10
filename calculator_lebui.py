#CS-142 Lab 1
#Simple console calculator

def calculate():
    calculation = input("Enter Your Calculation: ")
    calculation = calculation.split(" ")

    num1 = float(calculation[0])
    type = calculation[1]
    num2 = float(calculation[2])

    if type == "+":
        print (num1 + num2)
    elif type == "-":
        print (num1 - num2)
    elif type == "*":
        print (num1 * num2)
    elif type == "/":
        print (num1 / num2)

    again = input("Do you want to calculate another:(write y or n)")
    if again == "y":
      calculate()
    else:
      print ("Ok!")
                      
calculate()
        
