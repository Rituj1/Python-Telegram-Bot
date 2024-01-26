from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes,filters

TOKEN: Final = '6927548304:AAHerw3Sd_Lz9-HIGb2lCdto_Im9K1mvZZQ'

BOT_USERNAME: Final = '@Ask_me_py_bot'


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""Hello! Thanks for chatting with me! I am a Python_Bot!""")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""Hello! This is help command! How can i help!
If you are facing any problem or having problem related to Bot then you can mail on xyz987@gmail.com.""")


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""This is a custom command!
    Here are some predefined commands that can be answered by Python_Bot.
    1.What is python?
    2.Comment in python?
    3.Variables in python?
    4.Data types in python?
    5.What is a tuple in python and how do you create one?
    6.What is a list in python and how do you create one?
    7.What is a dictionary in python and how do you create one?
    8.What is a set in python and how do you create one?
    9.Functions in python?
    10.Name some libraries of python?
    11.Exception handling in python?
    12.File handling in python?
    13.Lambda function in python?
    14.What is the difference between python 2 and python 3?
    15.How do I install a python package?
    16.What is a virtual environment in python?
    17.How do I read user input in python?
    18.What is the purpose of the if statement in python?
    19.How do I open and read a file in python?
    20.What is the purpose of the len() function in python?
    21.How can you check the type of a variable in python?
    22.What is the purpose of the else statement in python's?
    23.How do you iterate over items in a list in python?
    24.What is the purpose of the __init__ method in a python class?
    25.How do you check if a number is even or odd in python?
    26.How do you determine if a number is prime in python?
    27.How do you check if a word or number is a palindrome in python?
    28.How do you generate the Fibonacci sequence in python?
    29.How do you generate a random number between 1 and 100 in python?
    30. How to check python version?
    31. Learn more about python.
    """)
    



# responses

def handle_response(text: str) -> str:
    processed: str = text.lower()
    

    if "hello" in processed:
        return 'Hey there!'

    if 'how are you' in processed:
        return 'I am good!'

    if 'i love python' in processed:
        return 'I love too!'
    
    if 'i want to learn' in processed:
        return 'Great! lets start from basics.'

    if 'what can you do?' in processed:
        return 'Currently, we can only provide answers to custom questions! Please look into help section to know more.'
    
    if 'what is your name' in processed:
        return 'I am a python bot.'
    
    if 'who made you' in processed:
        return 'I am created as part of a project. Created by Aman Kumar, Mukesh Kumar Baitha, Rituj Srivastava.'
    
    if 'thank you' in processed:
        return 'Welcome! Feel free to ask anything.'
    
    if 'hi' in processed:
        return 'Hey there!'
    
    if 'i want to play games' in processed:
        return 'Sorry! We dont have games right now.'
    
    if 'bye' in processed:
        return 'Bye! Have a good day.'
    
    if 'what is python?' in processed:
        return (' Python is a high-level programming language known for its simplicity and readability. Its versatile,'
                ' used in web development, data analysis, artificial intelligence, and more.'
                '\nKey features of Python:'
                '\n1.Readability and Simplicity.'
                '\n2.Extensive Standard Library.'
                '\n3.Dynamic Typing and High-level Language.'
                '\n4.Interpreted and Cross-platform.'
                '\n5.Community and Ecosystem.'
                )
    
    if 'comment in python?' in processed:
        return """for multiple line (""" """ or ''' ''') and '#' for single line comment."""
        
    if 'data types in python?' in processed:
        return ("Python has several data types including int for integers, float for floating-point numbers,"
                " str for strings, bool for Boolean values, list, tuple, and dict for data structures, among others.")
        
    if 'variables in python?' in processed:
        return """You can declare a variable in Python by assigning a value to a name.
        Like x=5,abc1=10, etc. But never start a variable name with digit.
        We can start a variable name with _ , a1 , a not like 12a. """
    
    if 'what is a tuple in python and how do you create one?' in processed:
        return """A tuple in Python is an ordered and immutable collection of elements. Once created, the elements cannot be changed.
               # Creating a tuple
               my_tuple = (1, 2, 3, 4, 5)"""
    
    if 'what is a list in python and how do you create one?' in processed:
        return """A list in Python is an ordered collection of elements. It can contain elements of different data types and is mutable,
                  meaning you can modify its contents.
                  # Creating a list
                  my_list = [1, 2, 3, 4, 5]"""
    
    if 'what is a dictionary in python and how do you create one?' in processed:
        return """A dictionary in Python is an unordered collection of key-value pairs. It is mutable and allows quick access to values using unique keys.
                  # Creating a dictionary
                  my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
"""
    
    if 'what is a set in python and how do you create one?' in processed:
        return """A set in Python is an unordered collection of unique elements. It is mutable and does not allow duplicate values.
                  # Creating a set
                  my_set = {1, 2, 3, 4, 5}"""
    
        
    if 'functions in python?' in processed:
        return """By using 'def' keyword we can create function.
        There are two types of functions in python 1. Built in function and 2. User define function.
        Built in function:- The functions which are coming along with Python software automatically, are called built in functions or predefined functionsExample: id() , type() , input() , eval() , etc..
        User define function:- The functions which are developed by programmer explicitly according to business requirements, are called user defined functions.
        Syntax to create user defined functions:
        Like this- def function_name(parameters):"""
        
    if 'name some libraries of python?' in processed:
        return """A Python library is a collection of functions and methods that allow you to perform many actions without writing your own code.
        Some of the python libraries are Pandas, Numpy, turtle, time and many more."""
    
    if 'exception handling in python?' in processed:
        return """Exceptions in Python can be handled using try, except, and optionally 'finally' blocks. For example
            try:
            # code that might raise an exception
            result = 10 / 0
            except ZeroDivisionError:
            print("Cannot divide by zero!")
            """
        
    if 'file handling in python?' in processed:
        return """ You can open a file using the open() function, read or write content, and close the file using close(). For instance:
            file = open('example.txt', 'r')  # 'r' for reading, 'w' for writing
              content = file.read()  # read file content
              file.close()  # close the file
              """
    if 'lamda function in python?' in processed:
        return """A lambda function, also known as an anonymous function, is a concise way to create small, unnamed functions. It
              is defined using the lambda keyword, often for short-term use. For example:
              add = lambda x, y: x + y
              result = add(3, 5)  # result is 8
              """
    if 'what is the difference between python 2 and python 3?' in processed:
        return """Python 3 is the latest version and has improvements over Python 2. Some key differences include print syntax,
              integer division, and Unicode support.
              """
    if 'how do i install a python package?' in processed:
        return """Use the pip command (in the terminal, inside your python project folder) followed by the package name. For example,
              pip install package_name.
              """
    if 'what is a virtual environment in python?' in processed:
        return """A virtual environment is a tool that helps manage dependencies for different Python projects, 
        preventing conflicts between packages."""
    
    if 'how do i read user input in python?' in processed:
        return """Use the input() function. For example, user_input = input("Enter something: ")."""
    
    if 'what is the purpose of the if statement in python?' in processed:
        return """The if statement is used for conditional execution. It allows you to execute a block of code 
        only if a certain condition is true."""
    
    if 'how do i open and read a file in python?' in processed:
        return """Use the open() function to open a file and methods like read(), readline(), 
        or readlines() to read its content."""
    
    if 'what is the purpose of the len() function in python?' in processed:
        return """The len() function returns the length (the number of items) of an object, 
        such as a string, list, or tuple."""
    
    if 'how can you check the type of a variable in python?' in processed:
        return """You can use the type() function to check the type of a variable. For example:
               my_variable = 42
            print(type(my_variable))  # Output: <class 'int'>
            """
    
    if "what is the purpose of the else statement in python's?" in processed:
        return """" The else statement is used to specify a block of code that should be executed if the 
        condition in the if statement is false."""
    
    if 'how do you iterate over items in a list in python?' in processed:
        return """You can use a for loop to iterate over items in a list. For example:
               my_list = [1, 2, 3, 4]
               for item in my_list:
               print(item)
               """
    
    if 'what is the purpose of the __init__ method in a python class?' in processed:
        return """The __init__ method is a special method in Python classes that is automatically called
         when an object is created.
                  It is used to initialize the object's attributes. For example:
                  class MyClass:
                      def __init__(self, value):
                          self.value = value
                  obj = MyClass(42)
                  print(obj.value)
                  # Output: 42
                  """
    
    if 'how do you check if a number is even or odd in python?' in processed:
        return """You can use the module operator (%) to check if a number is divisible by 2. If the result is 0,
         the number is even; otherwise,
                  it's odd.
                  # Checking if a number is even or odd
                  num = 7

                 if num % 2 == 0:
                     print(f"{num} is even.")
                 else:
                     print(f"{num} is odd.")"""
    
    if 'how do you determine if a number is prime in python?' in processed:
        return """ You can use a loop to check for divisibility. A prime number is one that is only divisible by 1 and itself.

                   # Checking if a number is prime
                   def is_prime(number):
                       if number < 2:
                           return False
                       for i in range(2, int(number**0.5) + 1):
                           if number % i == 0:
                               return False
                           return True

                           num = 13
                           if is_prime(num):
                               print(f"{num} is a prime number.")
                           else:
                               print(f"{num} is not a prime number.")"""
    
    if 'how do you check if a word or number is a palindrome in python?' in processed:
        return """You can compare the string with its reverse to check if it reads the same backward as forward.
                  # Checking if a word or number is a palindrome
                  def is_palindrome(word):
                  return word == word[::-1]

                  my_word = "radar"
                  if is_palindrome(my_word):
                  print(f"{my_word} is a palindrome.")
                  else:
                  print(f"{my_word} is not a palindrome.")
                  """
    
    if 'how do you generate the fibonacci sequence in python?' in processed:
        return """You can use a loop or recursion to generate the Fibonacci sequence.
                  # Generating the Fibonacci sequence
                  def fibonacci(n):
                  fib_sequence = [0, 1]
                  while len(fib_sequence) < n:
                  fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
                  return fib_sequence

                  n = 8
                  print(f"The first {n} numbers in the Fibonacci sequence are: {fibonacci(n)}")
                  """
    
    if 'how do you generate a random number between 1 and 100 in python?' in processed:
        return """ You can use the random module to generate a random integer within a specified range.
                   # Generating a random number between 1 and 100
                   import random

                   random_number = random.randint(1, 100)
                   print(f"Random number between 1 and 100: {random_number}")
               """

    if 'how to check python version?' in processed:
        return 'Simple open your terminal and type - "python --version" and hit enter.'

    if 'learn more about python.' in processed:
        return 'Visit the site "https://docs.python.org/3/". Choose your Python Version and follow the documentation.'
    
    
    
    return "I do not understand what you wrote...."

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
        else:
            return
    else:
        response: str = handle_response(text)
    print('Bot:',  response)
    await update.message.reply_text(response)

    async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
        print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    print("starting bot...")
    app = Application.builder().token(TOKEN).build()

    #commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    #messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))


    #polls the bot
    print("polling...")
    app.run_polling(poll_interval=3)
