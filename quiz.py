import random

def show_menu():
    """
        this function prints the menu for the user to see what selection
        is available to them.
        
        1. Ask question
        2. Add question
        3. Exit game
        
        it then asks the user for an input ans stores it in the option variable
        and returns it.
    
    """
    print('1. Ask question')
    print('2. Add a question')
    print('3. Delete a question')
    print('4. Exit game')
    
    option = input('Enter option: ')
    return option
    
def ask_questions():
    """
        this function acsseses the questions and answers stored in the 
        questions.txt file, and adds them to empty questions and answers lists. 
    
    """
    questions = []
    answers = []
    
    # closes the file automatically
    # reads the question file and splits the text into lines
    with open('questions.txt', 'r') as file: 
        lines = file.read().splitlines()
    
    # enumarate creates a tuple in memory with a line number and text
    for i, text in enumerate(lines):
        
        #if line numbers are even = question
        if i % 2 == 0:
            questions.append(text)
        #if line numbers are odd = answer
        else: 
            answers.append(text)
            
    number_of_questions = len(questions)
    
    # zip function to put everything into another tuple in memory
    questions_and_answers = zip(questions, answers)
    
    score = 0
            

    for question, answer in questions_and_answers:
        
        guess = input(question + '> ')
        if guess == answer:
            score += 1
            print('Right!')
            print(score)
        else:
            print('Wrong!')
            
    print('You got {0} correct out of {1}'.format(score, number_of_questions))
    
def add_question():
    print('')
    question = input('Enter question \n Here: ')
    
    print('')
    print('OK tell me the answer')
    answer = input('{0}\n> '.format(question))
    
    file = open('questions.txt', 'a')
    file.write(question + '\n')
    file.write(answer + '\n')
    file.close()
    
def delete_question():
    
    print('')
    delete = int(input('What question number do you want to delete ?\n>'))
    
    
    with open('questions.txt', 'r') as file: 
        lines = file.readlines()
    
    with open('questions.txt', 'w') as file: 
        for i, text in enumerate(lines):
            if delete % 2 == 0:
                delete = delete
                if i != delete and i != delete + 1:
                    file.write(text)
            elif delete % 2 != 0:
                delete = delete - 1
                if i != delete and i != delete + 1: 
                    file.write(text)
                    
def game_loop():
    while True:
        option = show_menu()
        if option == '1':
            ask_questions()
        elif option == '2':
            add_question()
        elif option == '3':
            delete_question()
        elif option == '4':
            break
        else: 
            print('Invalid option')
        print("")
        
game_loop()

