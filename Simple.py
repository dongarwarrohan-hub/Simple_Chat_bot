# ============================================================
#                 SIMPLE PYTHON CHATBOT
# ============================================================
# This is a basic chatbot made using Python.
# It can answer simple questions and perform small tasks.
# ============================================================

import random
from datetime import datetime


# ------------------------------------------------------------
# Function to display the welcome message
# ------------------------------------------------------------

def welcome():
    print("=" * 55)
    print("              SIMPLE PYTHON CHATBOT")
    print("=" * 55)
    print("Hello! I am a simple chatbot.")
    print("You can talk with me or ask me simple questions.")
    print("Type 'help' to see what I can do.")
    print("Type 'bye' to exit the chatbot.")
    print("=" * 55)


# ------------------------------------------------------------
# Function to display help
# ------------------------------------------------------------

def show_help():
    print("\nHere are some things you can ask me:")
    print("1. hello / hi")
    print("2. how are you")
    print("3. what is your name")
    print("4. who made you")
    print("5. what can you do")
    print("6. time")
    print("7. date")
    print("8. joke")
    print("9. study")
    print("10. motivation")
    print("11. calculator")
    print("12. bye")


# ------------------------------------------------------------
# Function for greetings
# ------------------------------------------------------------

def greeting():
    messages = [
        "Hello! Nice to meet you.",
        "Hi! How are you?",
        "Hey! What can I do for you?",
        "Hello bro! How can I help you?"
    ]

    print(random.choice(messages))


# ------------------------------------------------------------
# Function for telling about the chatbot
# ------------------------------------------------------------

def chatbot_info():
    print("\nMy name is SimpleBot.")
    print("I am a basic Python chatbot.")
    print("I use simple functions and basic logic.")
    print("I don't use artificial intelligence or APIs.")
    print("I was created as a beginner Python project.")


# ------------------------------------------------------------
# Function to tell what chatbot can do
# ------------------------------------------------------------

def chatbot_work():
    print("\nI can do some basic things:")
    print("- Have a simple conversation")
    print("- Tell the current time")
    print("- Tell today's date")
    print("- Tell a joke")
    print("- Give study tips")
    print("- Give motivation")
    print("- Perform simple calculations")
    print("- Answer some common questions")


# ------------------------------------------------------------
# Function for jokes
# ------------------------------------------------------------

def tell_joke():
    jokes = [
        "Why did the computer go to the doctor?",
        "Because it had a virus!",
        "",
        "Why was the math book sad?",
        "Because it had too many problems!",
        "",
        "Why do programmers prefer dark mode?",
        "Because light attracts bugs!"
    ]

    print()
    for joke in jokes:
        print(joke)


# ------------------------------------------------------------
# Function for motivation
# ------------------------------------------------------------

def motivation():
    quotes = [
        "Small progress is still progress.",
        "Don't wait for motivation. Start working.",
        "Consistency is more important than perfection.",
        "One good day can change your whole week.",
        "Keep learning and keep improving."
    ]

    print(random.choice(quotes))


# ------------------------------------------------------------
# Function for study tips
# ------------------------------------------------------------

def study_tips():
    tips = [
        "Make a small timetable before studying.",
        "Keep your phone away while studying.",
        "Study one topic at a time.",
        "Take short breaks between study sessions.",
        "Revise what you studied at the end of the day."
    ]

    print("\nStudy Tip:")
    print(random.choice(tips))


# ------------------------------------------------------------
# Function to display current time
# ------------------------------------------------------------

def show_time():
    current_time = datetime.now()

    print("\nCurrent time is:",
          current_time.strftime("%I:%M:%S %p"))


# ------------------------------------------------------------
# Function to display current date
# ------------------------------------------------------------

def show_date():
    current_date = datetime.now()

    print("\nToday's date is:",
          current_date.strftime("%d-%m-%Y"))


# ------------------------------------------------------------
# Function for simple calculator
# ------------------------------------------------------------

def calculator():

    print("\n----- SIMPLE CALCULATOR -----")
    print("Available operations:")
    print("+  Addition")
    print("-  Subtraction")
    print("*  Multiplication")
    print("/  Division")

    try:
        number1 = float(input("Enter first number: "))
        operator = input("Enter operator: ")
        number2 = float(input("Enter second number: "))

        if operator == "+":
            answer = number1 + number2
            print("Answer =", answer)

        elif operator == "-":
            answer = number1 - number2
            print("Answer =", answer)

        elif operator == "*":
            answer = number1 * number2
            print("Answer =", answer)

        elif operator == "/":

            if number2 == 0:
                print("Cannot divide by zero.")

            else:
                answer = number1 / number2
                print("Answer =", answer)

        else:
            print("Invalid operator.")

    except ValueError:
        print("Please enter numbers correctly.")


# ------------------------------------------------------------
# Function for common questions
# ------------------------------------------------------------

def common_questions(user_input):

    if "your age" in user_input:
        print("I don't have an age because I am a program.")

    elif "where are you" in user_input:
        print("I live inside this Python program.")

    elif "favorite color" in user_input:
        print("I like blue, but I don't really have preferences.")

    elif "favorite food" in user_input:
        print("I can't eat food, but pizza sounds good!")

    elif "thank" in user_input:
        print("You're welcome!")

    else:
        print("Sorry, I don't understand that question.")


# ------------------------------------------------------------
# Main chatbot function
# ------------------------------------------------------------

def chatbot():

    welcome()

    while True:

        user_input = input("\nYou: ")

        # Convert everything to lowercase
        user_input = user_input.lower().strip()

        # Check for empty input
        if user_input == "":
            print("Bot: Please type something.")
            continue

        # ----------------------------------------------------
        # Exit commands
        # ----------------------------------------------------

        if user_input == "bye" or user_input == "exit":
            print("Bot: Goodbye! Have a nice day.")
            break

        # ----------------------------------------------------
        # Greeting commands
        # ----------------------------------------------------

        elif user_input == "hello" or user_input == "hi":
            print("Bot:", end=" ")
            greeting()

        elif "hey" in user_input:
            print("Bot:", end=" ")
            greeting()

        # ----------------------------------------------------
        # Help command
        # ----------------------------------------------------

        elif user_input == "help":
            show_help()

        # ----------------------------------------------------
        # Name questions
        # ----------------------------------------------------

        elif "your name" in user_input:
            chatbot_info()

        # ----------------------------------------------------
        # Creator questions
        # ----------------------------------------------------

        elif "who made you" in user_input:
            print("Bot: I was made using Python as a simple project.")

        elif "who created you" in user_input:
            print("Bot: A Python student created me.")

        # ----------------------------------------------------
        # How are you
        # ----------------------------------------------------

        elif "how are you" in user_input:
            replies = [
                "I am doing great!",
                "I am fine. Thanks for asking.",
                "I am ready to chat!",
                "Everything is working perfectly."
            ]

            print("Bot:", random.choice(replies))

        # ----------------------------------------------------
        # What can you do
        # ----------------------------------------------------

        elif "what can you do" in user_input:
            chatbot_work()

        # ----------------------------------------------------
        # Time command
        # ----------------------------------------------------

        elif user_input == "time" or "current time" in user_input:
            show_time()

        # ----------------------------------------------------
        # Date command
        # ----------------------------------------------------

        elif user_input == "date" or "today date" in user_input:
            show_date()

        # ----------------------------------------------------
        # Joke command
        # ----------------------------------------------------

        elif user_input == "joke" or "tell me a joke" in user_input:
            tell_joke()

        # ----------------------------------------------------
        # Motivation command
        # ----------------------------------------------------

        elif "motivate" in user_input:
            motivation()

        elif "motivation" in user_input:
            motivation()

        # ----------------------------------------------------
        # Study command
        # ----------------------------------------------------

        elif "study" in user_input:
            study_tips()

        # ----------------------------------------------------
        # Calculator command
        # ----------------------------------------------------

        elif user_input == "calculator":
            calculator()

        # ----------------------------------------------------
        # Simple thanks
        # ----------------------------------------------------

        elif user_input == "thanks":
            print("Bot: You're welcome!")

        # ----------------------------------------------------
        # Common questions
        # ----------------------------------------------------

        elif ("your age" in user_input or
              "where are you" in user_input or
              "favorite color" in user_input or
              "favorite food" in user_input):
            common_questions(user_input)

        # ----------------------------------------------------
        # Unknown question
        # ----------------------------------------------------

        else:
            common_questions(user_input)


# ------------------------------------------------------------
# Starting the chatbot
# ------------------------------------------------------------

if __name__ == "__main__":
    chatbot()
