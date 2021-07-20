import random

from questions import QUESTIONS


def isAnswerCorrect(question, answer):
    if question["answer"] == answer:
        return True
    else:
        return False

def lifeLine(ques):
    wrong_options = list(set([1, 2, 3, 4]) - set([ques["answer"]]))
    wrong_options = random.sample(wrong_options, 2)
    x = "option" + str(wrong_options[0])
    y = "option" + str(wrong_options[1])
    [ques.pop(key) for key in [x, y]]
    return ques


def kbc(i, total, lives):
    if i == 0:
        print("Welcome to the game!")

    price = QUESTIONS[i]["money"]
    
    if i < 5:
        padav = 0
    elif i < 10:
        padav = 10000
    else:
        padav = 320000

    print(f"Total Won Until Now : {total}")
    print(f"No. of Lifelines left : {lives}")
    print(f'\tQuestion {i+1}: {QUESTIONS[i]["name"]}' )
    print(f'\t\tOptions:')
    print(f'\t\t\tOption 1: {QUESTIONS[i]["option1"]}')
    print(f'\t\t\tOption 2: {QUESTIONS[i]["option2"]}')
    print(f'\t\t\tOption 3: {QUESTIONS[i]["option3"]}')
    print(f'\t\t\tOption 4: {QUESTIONS[i]["option4"]}')
    ans = input('Your choice ( 1-4 ) : ')

    try:
        int(ans)
    except ValueError:
        if ans.lower() == "quit":
            print(f"You won : {padav}")
            exit()

        if ans.lower() == "lifeline":

            if i == 14:
                print("Cannot use lifeline on last question.\n Disqualified!")
                print(f"You won : {padav}")
                exit()
            
            if lives < 1:
                print("Cannot use lifeline more than once.\n Disqualified")
                print(f"You won : {padav}")
                exit()

            lives = lives - 1
            question = lifeLine(QUESTIONS[i])
            temp_keys = list(question.keys())
            temp_keys.remove("name")
            temp_keys.remove("money")
            temp_keys.remove("answer")
            x = temp_keys[0][-1]
            y = temp_keys[1][-1]

            print(f'\tQuestion {i+1}: {QUESTIONS[i]["name"]}')
            print(f"\t\tOptions:")
            print(f'\t\t\tOption {x}: {QUESTIONS[i][f"option{x}"]}')
            print(f'\t\t\tOption {y}: {QUESTIONS[i][f"option{y}"]}')
            ans = input(f"Your choice ( {x} or {y} ) : ")

    if isAnswerCorrect(QUESTIONS[i], int(ans) ):
        total += price
        if i == 5:
            print("Level Crossed!")
            print("New Padav : 10000")
        if i == 10:
            print("Level Crossed!")
            print("New Padav : 320000")
        print(f"Total : {price}")
        print('\nCorrect !')

    else:
        print("\nIncorrect !")
        print(f"Correct Answer Was {QUESTIONS[i]['answer']}")
        exit()
    return total, lives

total = 0
lives = 1

for i in range(15):
    total, lives = kbc(i, total, lives)

print(f"You are taking {total} home, with you")
