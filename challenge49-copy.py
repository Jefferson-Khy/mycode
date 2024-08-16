import random

def main():
    """ math quiz based on user input of
        addition, subtraction, multiplication, division
    """
    global acceptedOperation, userChoice, playAgain, correctQuestionCounter
    global wrongQuestionCounter, totalQuestionCounter, currentUserAnswer
    global solution, number1, number2

    acceptedOperation = False
    userChoice = ""
    playAgain = True
    correctQuestionCounter = 0
    wrongQuestionCounter = 0
    totalQuestionCounter = 0
    currentUserAnswer = 0
    solution = 0
    number1 = 0
    number2 = 0
    
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)

    solution = addition(number1, number2)

    while True:
        input("YOU HAVE 5 SECONDS TO ANSWER THE FOLLOWING QUESTION, PRESS ANY KEY TO CONTINUE: ")
        while True:  # Loop until a valid integer is entered
            try:
                currentUserAnswer = float(input(f"\n {number1} + {number2} = "))
                break  # Exit the loop if input is valid
            except ValueError:
                print("Invalid input! Please enter a number.")
        if(currentUserAnswer != solution):
            print("~ ~ ~ ~ ~ ~ ~ Game Over ~ ~ ~ ~ ~ ~ ~")
        else:
            print("you survived for now....")






def addition(num1, num2):
    sum = int(num1) + int(num2)
    return sum

def subtraction(num1, num2):
    if num1 > num2:
        diff  = int(num1) - int(num2)
    else: diff = int(num2) - int(num1)
    return diff

def multiplication(num1, num2):
    product  = int(num1) * int(num2)
    return product

def division(num1, num2):
    quotient = int(num1) / int(num2)
    return round(quotient, 1)

def questionGenerator(num1, num2, sign, callback):
    global wrongQuestionCounter, correctQuestionCounter, totalQuestionCounter
    solution = callback(num1, num2)

    while True:  # Loop until a valid integer is entered
        try:
            currentUserAnswer = float(input(f"\n {num1} {sign} {num2} = "))
            break  # Exit the loop if input is valid
        except ValueError:
            print("Invalid input! Please enter a number.")

    if solution != currentUserAnswer:
        print(f"\n Wrong!!!,  Answer is {solution}, you entered {currentUserAnswer}")
        wrongQuestionCounter+= 1
    else:
        print(f"\n Correct!!!, Next question!")
        correctQuestionCounter+= 1
    totalQuestionCounter += 1


def checkOperation(userOperation):
    operations = ["addition", "subtraction", "multiplication", "division"]
    
    # Convert user input to lowercase and check if it's in the operations list
    if userOperation.lower() in operations:
        return True
    else:
        return False


main()
