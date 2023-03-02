# Imports
import data

# Global Variables
points = 0
questions = []
correct = []
userValidated = False

# Validation for user info
while not userValidated:
    user = data.Questions(str(input("What is your first name: ")), input("What is your age: "))
    if not user.name.isalpha() or user.name == "":
        print('Please enter a valid name')
    elif not user.age.isnumeric() or user.age == "":
        print('Please enter a valid age')
    else:
        userValidated = True

# Saves the score to the txt file
def saveScore():
    # define the users info
    userinfo = [f"Name: {user.name}", f"Age: {user.age}"]
    with open("scores.txt", "w") as f:
        for line in userinfo:
            #write
            f.write(str(line))
            f.write("\n")
        # Questions
        f.write("Questions:\n")
        for question in questions:
            # write each question
            f.write(question)
            f.write("\n")
        # Write the total points the user has
        f.write(f"Points: {points}")

# uses the objects function to generate a sequence of 
# 10 random integers to use for both variables
randNum1 = user.generateQuestions()
randNum2 = user.generateQuestions()

# for loop to create the questions and check for answers
# (the main loop)
for i in range(10):
    answerValidated = False
    realAnswer = randNum1[i] * randNum2[i] # define the true answer to the equation on screen
    userAnswer = input(f"{randNum1[i]} x {randNum2[i]} = ") # get the users input for the question

    # Check that the answer is a numeric digit
    while not answerValidated:
        if userAnswer.isnumeric():
            answerValidated = True
        else:
            # Ask the user to give a valid answer if they didnt before
            print("Please give a valid answer")
            userAnswer = input(f"{randNum1[i]} x {randNum2[i]} = ")
    
    # Compare to the true answer and tell user the answer, then adjust points as such
    if int(userAnswer) == realAnswer:
        print("Correct!")
        points += 6
        status = 'Correct'
    else:
        print("Incorrect!")
        points -= 3
        if points < 0:
            points = 0
        status = 'Incorrect'
    
    # Add the question to the array to later be added to the txt file if applicable
    questions.append(f"{randNum1[i]} x {randNum2[i]} = {userAnswer} / {status}")

# Prompt to ask the user if the score should be saved
shouldSave = input("Would you like to save your score? [y,n]")
if shouldSave == 'y':
    # Run the saveScore function
    saveScore()
