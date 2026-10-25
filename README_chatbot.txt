=====================================================
              BASIC CHATBOT (PYTHON)
=====================================================

1. ABOUT THE PROJECT
--------------------
A simple rule-based chatbot that runs in the console.
The user types a message and the bot replies based on
fixed rules. The conversation continues until the user
says "bye".

This project was built as part of a Python programming
internship task.


2. FEATURES
-----------
- Rule-based replies using if / elif / else
- Understands a few predefined messages
- Input is converted to lowercase and trimmed, so
  "Hello", "HELLO" and "  hello " all work
- Gives a random "I don't understand" reply for anything
  it does not recognise
- Ends the chat when the user types "bye"


3. WHAT THE BOT UNDERSTANDS
---------------------------
You type          Bot replies
--------------    ---------------------------------
hello / hi        Hi!
how are you       I am good, Thankyou
bye               Goodbye!  (chat ends)
anything else     Sorry! I can't Understand
                  OR  Sorry! Ask something else
                  (chosen randomly)


4. REQUIREMENTS
---------------
- Python 3.x
- No external libraries needed (only the built-in
  "random" module)


5. HOW TO RUN
-------------
1. Open a terminal / command prompt in the project folder
2. Run:

       python "basic chat bot.py"

   (On some systems use: python3 "basic chat bot.py")
   Note: the quotes are needed because the file name has
   spaces. If you rename it to basic_chat_bot.py, run:
   python basic_chat_bot.py
3. Type a message and press Enter
4. Type "bye" to exit


6. SAMPLE CHAT
--------------
Welcome...
hello
Hi!
how are you
I am good, Thankyou
what is your name
Sorry! Ask something else
bye
Goodbye!


7. PROGRAM STRUCTURE (FUNCTIONS)
--------------------------------
response(word)  - checks the user's message and returns
                  the matching reply
chat()          - loop that reads input, prints the reply
                  and stops when the user says "bye"


8. CONCEPTS USED
----------------
- Functions
- if / elif / else conditions
- while loop with break
- Strings and string methods (lower, strip)
- Lists
- random module (random.choice)
- Input and output


9. FILE STRUCTURE
-----------------
chatbot/
|-- basic chat bot.py    (main program)
|-- README_chatbot.txt   (this file)


10. POSSIBLE IMPROVEMENTS
-------------------------
- Add more questions and replies (e.g. "what is your name")
- Use a dictionary instead of many elif conditions
- Show a prompt such as "You: " before each input
- Handle "bye" variations like "goodbye" or "exit"


=====================================================
              Thank you for chatting!
=====================================================
