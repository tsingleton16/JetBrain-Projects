from random import choice
import string  

print('H A N G M A N')
print()
word_list = ['python', 'java', 'kotlin', 'javascript']
chosen_word = choice(word_list)
output = ['-'] * len(chosen_word)
turns = 8
used_letters = ''
correct  = 0
length = len(set(chosen_word))


while True:
    user_input = input('Type "play" to play the game, "exit" to quit: ')
    if user_input not in ['play', 'exit']:
        print('Input something esle')
    else:
        break

while user_input == 'play':
    print(''.join(output))
    print(turns)
    if correct == length:
        print('You guessed the word!')
        print('You survived!')
        break
    
    guess = input('Input a letter: ')
       
    if len(guess) != 1:
         print('You should input a single letter') 
    
    elif guess not in string.ascii_lowercase:
        print('It is not an ASCII lowercase letter')
    
    elif guess in used_letters:
        print('You already typed this letter')
    
    elif guess not in chosen_word:
        used_letters += guess
        turns -=1 
        print('No such letter in the word')
        if turns == 0:
            print('You are hanged!')
            break
        print()
        
    else:
        used_letters += guess
        correct +=1
        for i,letter in enumerate(chosen_word):
            if guess is letter:
                output[i] = guess
            
    print()

