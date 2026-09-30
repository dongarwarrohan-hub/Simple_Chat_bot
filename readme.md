# Simple Python Chatbot

## Project Overview

**Simple Python Chatbot** is a beginner-friendly chatbot project developed using Python. It can handle basic conversation, answer common questions, display the current date and time, provide jokes and study tips, give motivation, and perform simple calculations.

The chatbot uses basic Python concepts such as functions, lists, conditional statements, loops, string methods, exception handling, the `random` module, and the `datetime` module.

## Features

- Welcome message when the chatbot starts
- Greeting responses for `hello`, `hi`, and `hey`
- Help menu
- Chatbot name and information
- Information about what the chatbot can do
- Current time display
- Today's date display
- Random jokes
- Random motivation messages
- Random study tips
- Simple calculator
- Answers to common questions
- Handles empty input
- Exit using `bye` or `exit`
- Basic error handling for invalid calculator input

## Python Concepts Used

- Functions
- Lists
- `if`, `elif`, and `else`
- `while` loop
- `break` and `continue`
- String methods such as `lower()` and `strip()`
- `random.choice()`
- `datetime.now()`
- `strftime()`
- `try-except`
- User input and output

## Modules Used

### random
Used to select random greetings, jokes, motivation messages, study tips, and replies.

### datetime
Used to display the current time and date.

## How to Run

1. Install Python 3 on your computer.
2. Save the program as a Python file, for example:
   `simple_chatbot.py`
3. Open a terminal or command prompt in the file location.
4. Run:

```bash
python simple_chatbot.py
```

## Example Commands

```text
hello
help
what is your name
what can you do
time
date
joke
motivation
study
calculator
thanks
bye
```

## Sample Interaction

```text
=======================================================
              SIMPLE PYTHON CHATBOT
=======================================================
Hello! I am a simple chatbot.
You can talk with me or ask me simple questions.
Type 'help' to see what I can do.
Type 'bye' to exit the chatbot.
=======================================================

You: hello
Bot: Hello! Nice to meet you.

You: time
Current time is: 09:30:15 PM

You: joke
Why did the computer go to the doctor?
Because it had a virus!

You: calculator
----- SIMPLE CALCULATOR -----
Available operations:
+  Addition
-  Subtraction
*  Multiplication
/  Division
Enter first number: 10
Enter operator: *
Enter second number: 5
Answer = 50.0

You: bye
Bot: Goodbye! Have a nice day.
```

*Note: The displayed time is only an example. The program shows the actual current time when it runs.*

## Project Limitations

- It is a rule-based chatbot, not an AI chatbot.
- It does not use APIs or online services.
- It can respond only to the commands and questions included in the program.
- It does not store chat history.

## Future Improvements

- Add more questions and responses
- Add a graphical user interface
- Add voice input and output
- Add more calculator operations
- Add file-based chat history
- Connect the chatbot to an AI or natural language processing system

## Conclusion

This project demonstrates how basic Python programming concepts can be combined to create an interactive command-line chatbot. It is suitable for beginners who want to understand functions, loops, conditions, modules, input handling, and exception handling through a practical project.
