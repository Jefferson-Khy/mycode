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
    
    while playAgain:
        while not acceptedOperation:
            userChoice = input("\nWhich operation would you like to practice? (addition, subtraction, multiplication, division): ").lower()

            if checkOperation(userChoice):
                acceptedOperation = True
                # Proceed with the operation if valid
            else:
                print("\nInvalid operation. Please choose one of the following: addition, subtraction, multiplication, division")

        while totalQuestionCounter < 6:
            number1 = random.randint(1, 30)
            number2 = random.randint(1, 30)
            if userChoice == "addition":
                questionGenerator(number1, number2, "+", addition)
            elif userChoice == "subtraction":
                questionGenerator(number1, number2, "-", subtraction)    
            elif userChoice == "multiplication":
                questionGenerator(number1, number2, "*", multiplication)
            elif userChoice == "division":
                questionGenerator(number1, number2, "/", division)

        print("\nQuiz Over")
        print(f"\nQuestions Correct: {correctQuestionCounter}\nQuestions Wrong: {wrongQuestionCounter}")
        while True:
            playAgainInput = input("\nDo you want to practice again?: Type [Y]es or [N]o \n")
            if playAgainInput.lower() == "no":
                print("\nGoodBye!")
                playAgain = False
                break
            elif playAgainInput.lower() == "yes":
                playAgain = True
                acceptedOperation = False
                wrongQuestionCounter = 0
                correctQuestionCounter = 0
                totalQuestionCounter = 0
                break
            else:
                print("\nInvalid input! Please enter yes or no")


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
