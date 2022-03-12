# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#1 Naming
import random

print('Hello human what is you name?')
name = input()

print('Do you have nickname? (y/n)')
choice = input()

if 'y' in choice.lower():
    nickname = input('What your nickname : ')
    print('Nice to meet you, '+nickname)
else:
    nickname = name + name[-1] + 'yy'
    print('Okay then! I will call you '+nickname)

#2 Greeting selection

greetings = [
    'How are you today ' +nickname+ '?',
    'My dear '+nickname+ ', how are you feeling today ?',
    "What's up "+nickname+ ". Are you well?",
    'Greetings, '+nickname+'. All well ?',
    nickname+" How's everything going?"
]

print(random.choice(greetings))