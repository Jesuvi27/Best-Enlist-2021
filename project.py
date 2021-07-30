def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

# -------------------------
def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

# -------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

# -------------------------
def play_again():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
# -------------------------


questions = {
 "Who invented Coca-cola?: ": "C",
 "Who invented dynamite?: ": "A",
 "who invented light bulb?: ": "D",
 "Who invented vaccine?: ": "B",
 "Which two companies created the CD?: ": "B"
}

options = [["A. Caleb Bradham", "B. Charles Kingdom", "C. China", "D. India"],
          ["A. Alfred Nobel", "B. Orville Wright", "C. Alexender Graham Bell", "D. Benjamin"],
          ["A. Henry Ford", "B. Michael Bay", "C.Benjamin Franklin", "D. Thomas Edison"],
          ["A. Noot T.Issac","B. Edward Jenner", "C. Alexender Flemming", "D. Duffel"],
          ["A. Sony and Google","B. Sony and Philips", "C. Google and Yahoo", "D. Nintendo and Sony"]]
          

new_game()

while play_again():
    new_game()

print("Byeeeeee!")


OUTPUT:
  Who invented Coca-cola?:
A. Caleb Bradham
B. Charles Kingdom
C. China
D. India
Enter (A, B, C, or D): a
WRONG!
-------------------------
Who invented dynamite?:
A. Alfred Nobel
B. Orville Wright
C. Alexender Graham Bell
D. Benjamin
Enter (A, B, C, or D): a
CORRECT!
-------------------------
who invented light bulb?:
A. Henry Ford
B. Michael Bay
C.Benjamin Franklin
D. Thomas Edison
Enter (A, B, C, or D): d
CORRECT!
-------------------------
Who invented vaccine?:
A. Noot T.Issac
B. Edward Jenner
C. Alexender Flemming
D. Duffel
Enter (A, B, C, or D): b
CORRECT!
-------------------------
Which two companies created the CD?:
A. Sony and Google
B. Sony and Philips
C. Google and Yahoo
D. Nintendo and Sony
Enter (A, B, C, or D): b
CORRECT!
-------------------------
RESULTS
-------------------------
Answers: C A D B B
Guesses: A A D B B
Your score is: 80%
Do you want to play again? (yes or no): no
Byeeeeee!






















