#Name: Nathan Edwards
#   Prog Purpose: This Magic 8-Ball code uses Python tuple since
#   the user does not have the ability to change the 8-ball answers
#   However, the program could have used a list instead of a tuple.
#   NOTE: Tuples use parenthese; lisrs use square braces

import random
answers_8_ball = ("As I see it, yes", "Ask agains later",
                  "Better not tell you now", "Cannot predict now",
                  "Concentrate and ask again", "Don't count on it",
                  "It is certain", "It is decidedly so",
                  "Most likely", "My reply is no",
                  "My sources say no", "Outlook good",
                  "Outlook not so good", "Reply hazy try again",
                  "Signs point to yes", "Very doubtful",
                  "without a doubt", "Yes",
                  "Yes definitely", "You may rely on it", )

def main():

    print("I am the MAGIC-8 BALL and can answer any YES or NO question!")

    another_question = True
    while another_question:
        answer = random.choice(answers_8_ball)

        print("\nShake the MAGIC-8 BALL")
        print("...and now...")
        question = input("\nWhat is your YES or NO questiom? ")
        print("The MAGIC-8 Bball says: " + answer)

        askAgain = input("\nWould you like to ask me another question (Y or N)?:")
        if askAgain.upper() == "N" or askAgain == "n":
            another_question = False

        print("\nCome back again when you have other imporatant questions.")
        print("...Magic-8 Ball OUT.")

main()
 
