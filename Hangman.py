import random
from hangman_stages import stages

words_list = ["apple","goat","computer","laptop","english","time","game","live","setting",
         "aeroplane","water","food","music","application","mobile","box","love","hate","lazy"]

# here we generate random word from the above list 
random_word = random.choice(words_list)
#print(random_word)


lives = 7

display = [' _ ']*len(random_word)
print(display)
game_over = False
while True:
    guessed_word = input("Enter the word: ").lower()
    for index in range(len(random_word)):
        letter = random_word[index]
        if letter == guessed_word:
            display[index] = guessed_word
    print(display)       
    if guessed_word not in random_word:
        lives -= 1
        print("Your remaining lives are: ",lives)
        if lives == 0:
            game_over = True
            print("You loose ")
            break

    if ' _ ' not in display:
        print("YOU WIN...")   


    print(stages[lives])

