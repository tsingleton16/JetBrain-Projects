import random
name = input('Enter your name: ')
print(f'Hello, {name}')
user_options = input().split(',')
print("Okay, let's start")

score_file = open('rating.txt', 'r')
score = 0

for line in score_file:
    if name == line.split()[0]:
        score = int(line.split()[1])
        
if len(user_options) == 1:
    user_options = ['rock', 'paper', 'scissors']

def user_wins(user, computer):
    user_num = user_options.index(user)
    computer_num = user_options.index(computer)
    winner = (user_num - computer_num) % len(user_options)
    winner = winner <= len(user_options) // 2
    return winner

    
while True:
    computer_choice = random.choice(user_options)
    user_choice = input() 
    if user_choice == '!exit':
        print('Bye!')
        break
        
    elif user_choice == '!rating':
        print(f'Your rating: {score}')
        
    elif user_choice not in user_options:
        print('Invalid input')
       
    if user_choice in user_options:
        winner = user_wins(user_choice, computer_choice)
        
        if user_choice == computer_choice:
            score += 50
            print(f'There is a draw ({user_choice})')
        
        elif winner:
            score += 100
            print(f'Well done. Computer chose {computer_choice} and failed')
            
        elif not winner:
            print(f'Sorry, but computer chose {computer_choice}')
        
