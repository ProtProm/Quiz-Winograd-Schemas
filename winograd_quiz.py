
import random

#string displayed when user_level_choice in function level_choice is equal to easy
easy_question = '''
The city councilmen refused the demonstrators a permit because they feared violence. (__1__) feared violence.
The city councilmen refused the demonstrators a permit because they advocated violence. (__2__) advocated violence.
Sam and Amy are passionately in love, but Amy's parents are unhappy about it. It is because (__3__) are snobs.
Sam and Amy are passionately in love, but Amy's parents are unhappy about it. It is because (__4__) are fifteen.
'''
#list that correlates with the blank spaces un easy_question
easy_answer = ["The city councilmen","the demonstrators","Amy's parents","Sam and Amy"]

#string displayed when user_level_choice in function level_choice is equal to hard
medium_question = '''
John was doing research in the library when he heard a man humming and whistling. He was very annoyed. (__1__) was annoyed.
John was doing research in the library when he heard a man humming and whistling. He was very annoying. (__2__) was annoying.
Mary took out her flute and played one of her favorite pieces. Mary has loved (__3__) since she was a child.
Mary took out her flute and played one of her favorite pieces. Mary has had (__4__) since she was a child.
'''
#list that correlates with the blank spaces un medium_question
medium_answer = ["John","the hummer","the piece","the flute"]

#string displayed when user_level_choice in function level_choice is equal to hard
hard_question = '''
Jane gave Joan candy because she was hungry. (__1__) was hungry.
Jane gave Joan candy because she was not hungry. (__2__) was not hungry.
At the Loebner competition the judges couldn't figure out which respondents were the chatbots because they were so advanced. (__3__) were so advanced.
At the Loebner competition the judges couldn't figure out which respondents were the chatbots because they were so stupid. (__4__) were so stupid.
'''

#list that correlates with the blank spaces un hard_question
hard_answer = ["Joan","Jane","the chatbots","the judges"]

#blanks that the user will be asked to substitute
blanks_to_fill = ["__1__","__2__", "__3__", "__4__"]

#title
print ('''

>>> WINOGRAD SCHEMAS CHALLENGE <<<

''')

#user writes the word in order to choose difficulty, the question is printed as well as what is needed to be done and the challenge() is ran
#if the input is not right, it runs again level_choice()
def level_choice():
    user_level_choice = input("Write difficulty: easy, medium or hard: ")
    if user_level_choice == "easy":
        print (easy_question)
        print ("Fill in the blanks.")
        return challenge(easy_question, easy_answer)
    elif user_level_choice == "medium":
        print (medium_question)
        print ("Fill in the blanks.")
        return challenge(medium_question, medium_answer)
    elif user_level_choice == "hard":
        print (hard_question)
        print ("Fill in the blanks.")
        return challenge(hard_question, hard_answer)
    else:
        return level_choice()


#index in 0 in order to keep track to know when are all the blanks filled correctly
#if the user input is the same as the answer numered the blank numered will be replaced by it and the index will increase in one in order to pass to the next blank to filled
#if the length of answer is the same as index means that there are no more blanks to fill, meaning the user has passed the test in the difficulty chossen
#if not, the question with the blanks correctly anwsered having been substituted will be ran, and the user will be asked to write the next blank to fill
#At the end the user is asked to try again, if so he will start from the beggininng of the choosen difficulty

def challenge(question, answer):
    index = 0
    while index < len(answer):
        user_input = input("Write word (exactly as it appears on the text) to fill:" + str(blanks_to_fill[index]) + ": ")
        if user_input == answer[index]:
            question = question.replace(blanks_to_fill[index], answer[index])
            index += 1
            if len(answer) == index:
                print (" ")
                print (question)
                print (" ")
                print (">>> PASSED.")
                print (" ")
                user_again = input("Do you want to try another difficulty? Write: y/n ")
                if user_again == "y":
                    return level_choice()
                elif user_aga == "n":
                    return "Don't forget to come back if you change your mind."
                else:
                    return "Well done anyways!"
            print ("Correct. Running next:")
            print (question)
        else:
            user_choice = input("Wrong. Want to try again? Write: y/n ")
            if user_choice == "y":
                return challenge(question, answer)
            elif user_choice == "n":
                return "Cool. Till next time!"
            else:
                return level_choice()

print (level_choice())
