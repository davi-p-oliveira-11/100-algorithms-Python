'''
2) Write a program that reads a person's name and displays a welcome message for them:  
Example:  
What is your name? João da Silva  
Hello João da Silva, it's a pleasure to meet you!
'''

def main():
    def say_hello():
        name = input("What is your name ?")
        print(f'Hello {name} nice to meet you !')

    say_hello()

main()
input('Press Enter to Exit ... ')