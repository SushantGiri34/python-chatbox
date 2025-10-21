import random

response = {
    "hello": ["Hi there!", "Hello!", "Hey! How are you?", "Hi! Nice to see you!", "Hey friend!"],
    "hi": ["Hello!", "Hey!", "Hi there!", "Hi! What’s up?"],
    "hey": ["Hey buddy!", "Hey there!", "What’s going on?"],
    "how are you": ["I'm just a bot, but I'm doing great!", "I'm fine, thank you!", "Feeling chatty today!"],
    "your name": ["I'm SimpleBot, your Python friend!", "My name is SimpleBot.", "You can call me PyBot!"],
    "bye": ["Goodbye!", "See you soon!", "Bye-bye!", "Take care!", "Come back soon!"],
    "good morning": ["Good morning! Have a great day!", "Morning sunshine!", "Good morning! Did you sleep well?"],
    "good night": ["Good night! Sweet dreams!", "Sleep well!", "Rest well, see you tomorrow!"],
    "thank": ["You're welcome!", "No problem!", "Glad to help!", "Anytime!", "You’re very welcome!"],
    "thanks": ["You're welcome!", "No worries!", "My pleasure!"],
    "who are you": ["I'm a simple chatbot made with Python!", "Just a friendly code robot!"],
    "what are you": ["I'm a chatbot program.", "I'm Python code with a big heart! ❤️"],
    "what is python": ["Python is a programming language — simple and powerful!", "Python helps you build apps, bots, and more!"],
    "i am fine": ["Good to hear that!", "Glad you are fine!", "Nice! Let’s keep chatting!"],
    "i am sad": ["Oh no! Don’t be sad. I’m here for you.", "Everything will be okay!", "Sending you a digital hug 🤗"],
    "i am happy": ["Yay! Happiness is awesome!", "That’s great!", "Keep smiling!"],
    "weather": ["I don’t have sensors, but I hope it’s nice outside!", "Weather is always perfect for coding!"],
    "time": ["Sorry, I can’t tell exact time yet.", "Time flies when we chat!"],
    "joke": ["Why did the computer sneeze? It had a virus! 😂", "Why was the math book sad? Too many problems!"],
    "funny": ["Haha! I try to be funny sometimes!", "Glad you liked that!"],
    "age": ["I was born when you ran this code!", "I don’t age — I’m forever young!"],
    "creator": ["I was created by a Python learner like you!", "Someone smart coded me in Python."],
    "where are you": ["I live inside your computer.", "In the code world!"],
    "love": ["Aww! Robots don’t love, but I like chatting with you!", "Love is beautiful! ❤️"],
    "i love you": ["That’s sweet! But I’m just a chatbot 😅", "Love you too… as a friend! ❤️"],
    "food": ["I don’t eat, but I love bytes!", "You should try pizza!"],
    "music": ["Music is amazing! Do you like songs?", "I can’t hear, but I can imagine tunes!"],
    "game": ["Games are fun! What’s your favorite?", "I like guessing games!"],
    "coding": ["Coding is fun and creative!", "Python coding makes life easy!", "I love coding too!"],
    "learn": ["Learning never stops!", "You can learn Python with practice.", "I can help you learn coding!"],
    "study": ["Study smart, not hard!", "Learning is a superpower!"],
    "motivation": ["Keep going! You are doing great!", "Believe in yourself!", "Don’t give up — success is near!"],
    "sleep": ["Sleep well and recharge!", "Good rest helps you learn better!"],
    "bored": ["Let’s talk then! I can tell jokes!", "Why not learn something new?"],
    "school": ["School is cool!", "Learning is the best part of growing!"],
    "teacher": ["Teachers are awesome!", "Without teachers, we can’t learn!"],
    "friend": ["Friends make life happy!", "You’re my friend now!"],
    "hobby": ["My hobby is chatting!", "What do you like to do?"],
    "favorite color": ["I like blue — it’s calm!", "Colors make life beautiful!"],
    "robot": ["Yes, I’m a robot made of code!", "Beep boop 🤖!"],
    "computer": ["Computers are my home!", "Without computers, I wouldn’t exist!"],
    "help": ["I can reply to your simple questions!", "Ask me about weather, time, jokes, or feelings!"],
    "default": ["I didn’t understand that yet!", "Can you say that again?", "I’m still learning new words!"],
    
    "python": ["Python is a popular programming language.", "Python is easy to learn and powerful."],
    "what is python": ["Python is a programming language — simple and powerful!", "Python helps you build apps, bots, and more!"],
    "data type": ["Python has types like int, float, str, list, tuple, set, dict."],
    "list": ["A list is a collection of items that is ordered and changeable.", "Example: [1, 2, 3]"],
    "tuple": ["A tuple is an ordered, immutable collection.", "Example: (1, 2, 3)"],
    "dictionary": ["A dict stores key-value pairs. Example: {'name':'Alice'}", "Use dicts to store structured data."],
    "loop": ["Python loops: for loops and while loops are used to repeat code.", "Example: for i in range(5): print(i)"],
    "function": ["Functions are reusable blocks of code. Example: def add(a,b): return a+b"],
    "variable": ["Variables store data. Example: x = 10"],
    "string": ["Strings store text. Example: 'Hello World'"],
    "if else": ["If-else is used for decision making. Example: if x>0: print('Positive') else: print('Negative')"],

    # Common interview questions
    "difference between list and tuple": ["List is mutable, tuple is immutable.", "Tuples are faster than lists for iteration."],
    "what is a dictionary": ["Dictionary is a key-value data structure.", "Use {} to create a dict."],
    "what is a set": ["Set is an unordered collection of unique items.", "Example: {1,2,3}"],
    "python loop types": ["Python has for and while loops.", "Use loops to repeat tasks."],
    "python function": ["Functions are blocks of code that perform tasks.", "Use def keyword to define a function."],
    "what is class": ["Class is a blueprint for objects.", "Use class to define custom data types."],
    "what is object": ["An object is an instance of a class.", "It contains data and methods."],
    "oop concepts": ["Python supports OOP: class, object, inheritance, polymorphism, encapsulation."],
    "inheritance": ["Inheritance allows a class to inherit properties of another class."],
    "polymorphism": ["Polymorphism means the same operation can behave differently in different classes."],
    "encapsulation": ["Encapsulation hides internal data. Use private variables with underscore _."],
    "exception": ["Exceptions are errors caught at runtime.", "Use try-except blocks to handle exceptions."],
    "file handling": ["Python can read/write files using open(), read(), write(), close()."],
    "lambda": ["Lambda is an anonymous function. Example: lambda x: x+2"],
    "map filter reduce": ["map applies a function to all items.", "filter selects items based on condition.", "reduce combines items into one value."],
    "list comprehension": ["A concise way to create lists. Example: [x*2 for x in range(5)]"],
    "python module": ["A module is a file with Python code that can be imported.", "Use import module_name"],
    "pip": ["pip is used to install Python packages.", "Example: pip install requests"],
    "python version": ["You can check Python version using python --version or sys.version"],

    # Fun / generic
    "joke": ["Why did the computer sneeze? It had a virus! 😂", "Why was the math book sad? Too many problems!"],
    "funny": ["Haha! I try to be funny sometimes!", "Glad you liked that!"],
    "default": ["I didn’t understand that yet!", "Can you say that again?", "I’m still learning new questions!"]
}
  # some pre-define words

def get_response(user_input):
    user_input = user_input.lower() #covert all taext into lower latter

    for key in response:
        if key in user_input:
            return random.choice(response[key])
    #if don't have matching word
    return "i don't understand yet"

print("SimpleBot: Hello! I am your Python chatbot.")
print("Type 'quit' or 'exit' to stop chatting.\n")

while True:
    user = input("You: ")
    if user.lower() in ["quit" , "exit"]:
        print("SimpleBot: Bye! Have a nice day!")
        break
    
    reply = get_response(user)
    print("SimpleBot:", reply)